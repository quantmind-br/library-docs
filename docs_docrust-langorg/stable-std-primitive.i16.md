---
title: i16 - Rust
url: https://doc.rust-lang.org/stable/std/primitive.i16.html
source: crawler
fetched_at: 2026-05-06T21:28:17.679816847-03:00
rendered_js: false
word_count: 12345
summary: This document provides the API reference for the Rust 16-bit signed integer type (i16), detailing its properties, bitwise manipulation methods, and endianness conversion functions.
tags:
    - rust
    - i16
    - integer-types
    - bitwise-operations
    - api-reference
    - primitive-types
category: reference
---

Expand description

The 16-bit signed integer type.

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#369)[§](#impl-i16)

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

The smallest value that can be represented by this integer type (−215).

##### [§](#examples)Examples

```rust
assert_eq!(i16::MIN, -32768);
```

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

The largest value that can be represented by this integer type (215 − 1).

##### [§](#examples-1)Examples

```rust
assert_eq!(i16::MAX, 32767);
```

1.53.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

The size of this integer type in bits.

##### [§](#examples-2)Examples

```rust
assert_eq!(i16::BITS, 16);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the number of ones in the binary representation of `self`.

##### [§](#examples-3)Examples

```rust
let n = 0b100_0000i16;

assert_eq!(n.count_ones(), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the number of zeros in the binary representation of `self`.

##### [§](#examples-4)Examples

```rust
assert_eq!(i16::MAX.count_zeros(), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the number of leading zeros in the binary representation of `self`.

Depending on what you’re doing with the value, you might also be interested in the [`ilog2`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.ilog2 "method i16::ilog2") function which returns a consistent number, even if the type widens.

##### [§](#examples-5)Examples

```rust
let n = -1i16;

assert_eq!(n.leading_zeros(), 0);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the number of trailing zeros in the binary representation of `self`.

##### [§](#examples-6)Examples

```rust
let n = -4i16;

assert_eq!(n.trailing_zeros(), 2);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the number of leading ones in the binary representation of `self`.

##### [§](#examples-7)Examples

```rust
let n = -1i16;

assert_eq!(n.leading_ones(), 16);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the number of trailing ones in the binary representation of `self`.

##### [§](#examples-8)Examples

```rust
let n = 3i16;

assert_eq!(n.trailing_ones(), 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Returns `self` with only the most significant bit set, or `0` if the input is `0`.

##### [§](#examples-9)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: i16 = 0b_01100100;

assert_eq!(n.isolate_highest_one(), 0b_01000000);
assert_eq!(0_i16.isolate_highest_one(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Returns `self` with only the least significant bit set, or `0` if the input is `0`.

##### [§](#examples-10)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: i16 = 0b_01100100;

assert_eq!(n.isolate_lowest_one(), 0b_00000100);
assert_eq!(0_i16.isolate_lowest_one(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Returns the index of the highest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-11)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_i16.highest_one(), None);
assert_eq!(0b1_i16.highest_one(), Some(0));
assert_eq!(0b1_0000_i16.highest_one(), Some(4));
assert_eq!(0b1_1111_i16.highest_one(), Some(4));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Returns the index of the lowest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-12)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_i16.lowest_one(), None);
assert_eq!(0b1_i16.lowest_one(), Some(0));
assert_eq!(0b1_0000_i16.lowest_one(), Some(4));
assert_eq!(0b1_1111_i16.lowest_one(), Some(0));
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the bit pattern of `self` reinterpreted as an unsigned integer of the same size.

This produces the same result as an `as` cast, but ensures that the bit-width remains the same.

##### [§](#examples-13)Examples

```rust
let n = -1i16;

assert_eq!(n.cast_unsigned(), u16::MAX);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Shifts the bits to the left by a specified amount, `n`, wrapping the truncated bits to the end of the resulting integer.

`rotate_left(n)` is equivalent to applying `rotate_left(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `<<` shifting operator!

##### [§](#examples-14)Examples

```rust
let n = -0x5ffdi16;
let m = 0x3a;

assert_eq!(n.rotate_left(4), m);
assert_eq!(n.rotate_left(1024), n);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Shifts the bits to the right by a specified amount, `n`, wrapping the truncated bits to the beginning of the resulting integer.

`rotate_right(n)` is equivalent to applying `rotate_right(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `>>` shifting operator!

##### [§](#examples-15)Examples

```rust
let n = 0x3ai16;
let m = -0x5ffd;

assert_eq!(n.rotate_right(4), m);
assert_eq!(n.rotate_right(1024), n);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Reverses the byte order of the integer.

##### [§](#examples-16)Examples

```rust
let n = 0x1234i16;

let m = n.swap_bytes();

assert_eq!(m, 0x3412);
```

1.37.0 (const: 1.37.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Reverses the order of bits in the integer. The least significant bit becomes the most significant bit, second least-significant bit becomes second most-significant bit, etc.

##### [§](#examples-17)Examples

```rust
let n = 0x1234i16;
let m = n.reverse_bits();

assert_eq!(m, 0x2c48);
assert_eq!(0, 0i16.reverse_bits());
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Converts an integer from big endian to the target’s endianness.

On big endian this is a no-op. On little endian the bytes are swapped.

See also [from\_be\_bytes()](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.from_be_bytes "associated function i16::from_be_bytes").

##### [§](#examples-18)Examples

```rust
let n = 0x1Ai16;

if cfg!(target_endian = "big") {
    assert_eq!(i16::from_be(n), n)
} else {
    assert_eq!(i16::from_be(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Converts an integer from little endian to the target’s endianness.

On little endian this is a no-op. On big endian the bytes are swapped.

See also [from\_le\_bytes()](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.from_le_bytes "associated function i16::from_le_bytes").

##### [§](#examples-19)Examples

```rust
let n = 0x1Ai16;

if cfg!(target_endian = "little") {
    assert_eq!(i16::from_le(n), n)
} else {
    assert_eq!(i16::from_le(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Swaps bytes of `self` on little endian targets.

On big endian this is a no-op.

The returned value has the same type as `self`, and will be interpreted as (a potentially different) value of a native-endian `i16`.

See [`to_be_bytes()`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.to_be_bytes "method i16::to_be_bytes") for a type-safe alternative.

##### [§](#examples-20)Examples

```rust
let n = 0x1Ai16;

if cfg!(target_endian = "big") {
    assert_eq!(n.to_be(), n)
} else {
    assert_eq!(n.to_be(), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Swaps bytes of `self` on big endian targets.

On little endian this is a no-op.

The returned value has the same type as `self`, and will be interpreted as (a potentially different) value of a native-endian `i16`.

See [`to_le_bytes()`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.to_le_bytes "method i16::to_le_bytes") for a type-safe alternative.

##### [§](#examples-21)Examples

```rust
let n = 0x1Ai16;

if cfg!(target_endian = "little") {
    assert_eq!(n.to_le(), n)
} else {
    assert_eq!(n.to_le(), n.swap_bytes())
}
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked integer addition. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-22)Examples

```rust
assert_eq!((i16::MAX - 2).checked_add(1), Some(i16::MAX - 1));
assert_eq!((i16::MAX - 2).checked_add(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict integer addition. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics)Panics

###### [§](#overflow-behavior)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-23)Examples

```rust
assert_eq!((i16::MAX - 2).strict_add(1), i16::MAX - 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (i16::MAX - 2).strict_add(3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unchecked integer addition. Computes `self + rhs`, assuming overflow cannot occur.

Calling `x.unchecked_add(y)` is semantically equivalent to calling `x.`[`checked_add`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_add "method i16::checked_add")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_add`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.wrapping_add "method i16::wrapping_add").

##### [§](#safety)Safety

This results in undefined behavior when `self + rhs > i16::MAX` or `self + rhs < i16::MIN`, i.e. when [`checked_add`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_add "method i16::checked_add") would return `None`.

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked addition with an unsigned integer. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-24)Examples

```rust
assert_eq!(1i16.checked_add_unsigned(2), Some(3));
assert_eq!((i16::MAX - 2).checked_add_unsigned(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict addition with an unsigned integer. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics-1)Panics

###### [§](#overflow-behavior-1)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-25)Examples

```rust
assert_eq!(1i16.strict_add_unsigned(2), 3);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (i16::MAX - 2).strict_add_unsigned(3);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked integer subtraction. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-26)Examples

```rust
assert_eq!((i16::MIN + 2).checked_sub(1), Some(i16::MIN + 1));
assert_eq!((i16::MIN + 2).checked_sub(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict integer subtraction. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-2)Panics

###### [§](#overflow-behavior-2)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-27)Examples

```rust
assert_eq!((i16::MIN + 2).strict_sub(1), i16::MIN + 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (i16::MIN + 2).strict_sub(3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unchecked integer subtraction. Computes `self - rhs`, assuming overflow cannot occur.

Calling `x.unchecked_sub(y)` is semantically equivalent to calling `x.`[`checked_sub`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_sub "method i16::checked_sub")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_sub`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.wrapping_sub "method i16::wrapping_sub").

##### [§](#safety-1)Safety

This results in undefined behavior when `self - rhs > i16::MAX` or `self - rhs < i16::MIN`, i.e. when [`checked_sub`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_sub "method i16::checked_sub") would return `None`.

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked subtraction with an unsigned integer. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-28)Examples

```rust
assert_eq!(1i16.checked_sub_unsigned(2), Some(-1));
assert_eq!((i16::MIN + 2).checked_sub_unsigned(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict subtraction with an unsigned integer. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-3)Panics

###### [§](#overflow-behavior-3)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-29)Examples

```rust
assert_eq!(1i16.strict_sub_unsigned(2), -1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (i16::MIN + 2).strict_sub_unsigned(3);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked integer multiplication. Computes `self * rhs`, returning `None` if overflow occurred.

##### [§](#examples-30)Examples

```rust
assert_eq!(i16::MAX.checked_mul(1), Some(i16::MAX));
assert_eq!(i16::MAX.checked_mul(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict integer multiplication. Computes `self * rhs`, panicking if overflow occurred.

##### [§](#panics-4)Panics

###### [§](#overflow-behavior-4)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-31)Examples

```rust
assert_eq!(i16::MAX.strict_mul(1), i16::MAX);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MAX.strict_mul(2);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unchecked integer multiplication. Computes `self * rhs`, assuming overflow cannot occur.

Calling `x.unchecked_mul(y)` is semantically equivalent to calling `x.`[`checked_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_mul "method i16::checked_mul")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.wrapping_mul "method i16::wrapping_mul").

##### [§](#safety-2)Safety

This results in undefined behavior when `self * rhs > i16::MAX` or `self * rhs < i16::MIN`, i.e. when [`checked_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_mul "method i16::checked_mul") would return `None`.

1.0.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked integer division. Computes `self / rhs`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-32)Examples

```rust
assert_eq!((i16::MIN + 1).checked_div(-1), Some(32767));
assert_eq!(i16::MIN.checked_div(-1), None);
assert_eq!((1i16).checked_div(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict integer division. Computes `self / rhs`, panicking if overflow occurred.

##### [§](#panics-5)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-5)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is when one divides `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type); this is equivalent to `-MIN`, a positive value that is too large to represent in the type.

##### [§](#examples-33)Examples

```rust
assert_eq!((i16::MIN + 1).strict_div(-1), 32767);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.strict_div(-1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1i16).strict_div(0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked Euclidean division. Computes `self.div_euclid(rhs)`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-34)Examples

```rust
assert_eq!((i16::MIN + 1).checked_div_euclid(-1), Some(32767));
assert_eq!(i16::MIN.checked_div_euclid(-1), None);
assert_eq!((1i16).checked_div_euclid(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict Euclidean division. Computes `self.div_euclid(rhs)`, panicking if overflow occurred.

##### [§](#panics-6)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-6)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is when one divides `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type); this is equivalent to `-MIN`, a positive value that is too large to represent in the type.

##### [§](#examples-35)Examples

```rust
assert_eq!((i16::MIN + 1).strict_div_euclid(-1), 32767);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.strict_div_euclid(-1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1i16).strict_div_euclid(0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Checked integer division without remainder. Computes `self / rhs`, returning `None` if `rhs == 0`, the division results in overflow, or `self % rhs != 0`.

##### [§](#examples-36)Examples

```rust
#![feature(exact_div)]
assert_eq!((i16::MIN + 1).checked_div_exact(-1), Some(32767));
assert_eq!((-5i16).checked_div_exact(2), None);
assert_eq!(i16::MIN.checked_div_exact(-1), None);
assert_eq!((1i16).checked_div_exact(0), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Integer division without remainder. Computes `self / rhs`, returning `None` if `self % rhs != 0`.

##### [§](#panics-7)Panics

This function will panic if `rhs == 0`.

###### [§](#overflow-behavior-7)Overflow behavior

On overflow, this function will panic if overflow checks are enabled (default in debug mode) and wrap if overflow checks are disabled (default in release mode).

##### [§](#examples-37)Examples

```rust
#![feature(exact_div)]
assert_eq!(64i16.div_exact(2), Some(32));
assert_eq!(64i16.div_exact(32), Some(2));
assert_eq!((i16::MIN + 1).div_exact(-1), Some(32767));
assert_eq!(65i16.div_exact(2), None);
```

[ⓘ](# "This example panics")

```rust
#![feature(exact_div)]
let _ = 64i16.div_exact(0);
```

[ⓘ](# "This example panics")

```rust
#![feature(exact_div)]
let _ = i16::MIN.div_exact(-1);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Unchecked integer division without remainder. Computes `self / rhs`.

##### [§](#safety-3)Safety

This results in undefined behavior when `rhs == 0`, `self % rhs != 0`, or `self == i16::MIN && rhs == -1`, i.e. when [`checked_div_exact`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_div_exact "method i16::checked_div_exact") would return `None`.

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked integer remainder. Computes `self % rhs`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-38)Examples

```rust
assert_eq!(5i16.checked_rem(2), Some(1));
assert_eq!(5i16.checked_rem(0), None);
assert_eq!(i16::MIN.checked_rem(-1), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict integer remainder. Computes `self % rhs`, panicking if the division results in overflow.

##### [§](#panics-8)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-8)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is `x % y` for `MIN / -1` on a signed type (where `MIN` is the negative minimal value), which is invalid due to implementation artifacts.

##### [§](#examples-39)Examples

```rust
assert_eq!(5i16.strict_rem(2), 1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5i16.strict_rem(0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.strict_rem(-1);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked Euclidean remainder. Computes `self.rem_euclid(rhs)`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-40)Examples

```rust
assert_eq!(5i16.checked_rem_euclid(2), Some(1));
assert_eq!(5i16.checked_rem_euclid(0), None);
assert_eq!(i16::MIN.checked_rem_euclid(-1), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict Euclidean remainder. Computes `self.rem_euclid(rhs)`, panicking if the division results in overflow.

##### [§](#panics-9)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-9)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is `x % y` for `MIN / -1` on a signed type (where `MIN` is the negative minimal value), which is invalid due to implementation artifacts.

##### [§](#examples-41)Examples

```rust
assert_eq!(5i16.strict_rem_euclid(2), 1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5i16.strict_rem_euclid(0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.strict_rem_euclid(-1);
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked negation. Computes `-self`, returning `None` if `self == MIN`.

##### [§](#examples-42)Examples

```rust
assert_eq!(5i16.checked_neg(), Some(-5));
assert_eq!(i16::MIN.checked_neg(), None);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unchecked negation. Computes `-self`, assuming overflow cannot occur.

##### [§](#safety-4)Safety

This results in undefined behavior when `self == i16::MIN`, i.e. when [`checked_neg`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_neg "method i16::checked_neg") would return `None`.

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict negation. Computes `-self`, panicking if `self == MIN`.

##### [§](#panics-10)Panics

###### [§](#overflow-behavior-10)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-43)Examples

```rust
assert_eq!(5i16.strict_neg(), -5);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.strict_neg();
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked shift left. Computes `self << rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-44)Examples

```rust
assert_eq!(0x1i16.checked_shl(4), Some(0x10));
assert_eq!(0x1i16.checked_shl(129), None);
assert_eq!(0x10i16.checked_shl(15), Some(0));
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict shift left. Computes `self << rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-11)Panics

###### [§](#overflow-behavior-11)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-45)Examples

```rust
assert_eq!(0x1i16.strict_shl(4), 0x10);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x1i16.strict_shl(129);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unchecked shift left. Computes `self << rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-5)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shl`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_shl "method i16::checked_shl") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unbounded shift left. Computes `self << rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, and `0` is returned.

##### [§](#examples-46)Examples

```rust
assert_eq!(0x1_i16.unbounded_shl(4), 0x10);
assert_eq!(0x1_i16.unbounded_shl(129), 0);
assert_eq!(0b101_i16.unbounded_shl(0), 0b101);
assert_eq!(0b101_i16.unbounded_shl(1), 0b1010);
assert_eq!(0b101_i16.unbounded_shl(2), 0b10100);
assert_eq!(42_i16.unbounded_shl(16), 0);
assert_eq!(42_i16.unbounded_shl(1).unbounded_shl(15), 0);
assert_eq!((-13_i16).unbounded_shl(16), 0);
assert_eq!((-13_i16).unbounded_shl(1).unbounded_shl(15), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Exact shift left. Computes `self << rhs` as long as it can be reversed losslessly.

Returns `None` if any bits that would be shifted out differ from the resulting sign bit or if `rhs` &gt;= `i16::BITS`. Otherwise, returns `Some(self << rhs)`.

##### [§](#examples-47)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x1i16.shl_exact(4), Some(0x10));
assert_eq!(0x1i16.shl_exact(i16::BITS - 2), Some(1 << i16::BITS - 2));
assert_eq!(0x1i16.shl_exact(i16::BITS - 1), None);
assert_eq!((-0x2i16).shl_exact(i16::BITS - 2), Some(-0x2 << i16::BITS - 2));
assert_eq!((-0x2i16).shl_exact(i16::BITS - 1), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Unchecked exact shift left. Computes `self << rhs`, assuming the operation can be losslessly reversed and `rhs` cannot be larger than `i16::BITS`.

##### [§](#safety-6)Safety

This results in undefined behavior when `rhs >= self.leading_zeros() && rhs >= self.leading_ones()` i.e. when [`i16::shl_exact`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.shl_exact "method i16::shl_exact") would return `None`.

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked shift right. Computes `self >> rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-48)Examples

```rust
assert_eq!(0x10i16.checked_shr(4), Some(0x1));
assert_eq!(0x10i16.checked_shr(128), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict shift right. Computes `self >> rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-12)Panics

###### [§](#overflow-behavior-12)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-49)Examples

```rust
assert_eq!(0x10i16.strict_shr(4), 0x1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x10i16.strict_shr(128);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unchecked shift right. Computes `self >> rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-7)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shr`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.checked_shr "method i16::checked_shr") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Unbounded shift right. Computes `self >> rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, which yields `0` for a positive number, and `-1` for a negative number.

##### [§](#examples-50)Examples

```rust
assert_eq!(0x10_i16.unbounded_shr(4), 0x1);
assert_eq!(0x10_i16.unbounded_shr(129), 0);
assert_eq!(i16::MIN.unbounded_shr(129), -1);
assert_eq!(0b1010_i16.unbounded_shr(0), 0b1010);
assert_eq!(0b1010_i16.unbounded_shr(1), 0b101);
assert_eq!(0b1010_i16.unbounded_shr(2), 0b10);
assert_eq!(42_i16.unbounded_shr(16), 0);
assert_eq!(42_i16.unbounded_shr(1).unbounded_shr(15), 0);
assert_eq!((-13_i16).unbounded_shr(16), -1);
assert_eq!((-13_i16).unbounded_shr(1).unbounded_shr(15), -1);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Exact shift right. Computes `self >> rhs` as long as it can be reversed losslessly.

Returns `None` if any non-zero bits would be shifted out or if `rhs` &gt;= `i16::BITS`. Otherwise, returns `Some(self >> rhs)`.

##### [§](#examples-51)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x10i16.shr_exact(4), Some(0x1));
assert_eq!(0x10i16.shr_exact(5), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Unchecked exact shift right. Computes `self >> rhs`, assuming the operation can be losslessly reversed and `rhs` cannot be larger than `i16::BITS`.

##### [§](#safety-8)Safety

This results in undefined behavior when `rhs > self.trailing_zeros() || rhs >= i16::BITS` i.e. when [`i16::shr_exact`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.shr_exact "method i16::shr_exact") would return `None`.

1.13.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked absolute value. Computes `self.abs()`, returning `None` if `self == MIN`.

##### [§](#examples-52)Examples

```rust
assert_eq!((-5i16).checked_abs(), Some(5));
assert_eq!(i16::MIN.checked_abs(), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict absolute value. Computes `self.abs()`, panicking if `self == MIN`.

##### [§](#panics-13)Panics

###### [§](#overflow-behavior-13)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-53)Examples

```rust
assert_eq!((-5i16).strict_abs(), 5);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.strict_abs();
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Checked exponentiation. Computes `self.pow(exp)`, returning `None` if overflow occurred.

##### [§](#examples-54)Examples

```rust
assert_eq!(8i16.checked_pow(2), Some(64));
assert_eq!(0_i16.checked_pow(0), Some(1));
assert_eq!(i16::MAX.checked_pow(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Strict exponentiation. Computes `self.pow(exp)`, panicking if overflow occurred.

##### [§](#panics-14)Panics

###### [§](#overflow-behavior-14)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-55)Examples

```rust
assert_eq!(8i16.strict_pow(2), 64);
assert_eq!(0_i16.strict_pow(0), 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = i16::MAX.strict_pow(2);
```

1.84.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the square root of the number, rounded down.

Returns `None` if `self` is negative.

##### [§](#examples-56)Examples

```rust
assert_eq!(10i16.checked_isqrt(), Some(3));
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating integer addition. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-57)Examples

```rust
assert_eq!(100i16.saturating_add(1), 101);
assert_eq!(i16::MAX.saturating_add(100), i16::MAX);
assert_eq!(i16::MIN.saturating_add(-1), i16::MIN);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating addition with an unsigned integer. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-58)Examples

```rust
assert_eq!(1i16.saturating_add_unsigned(2), 3);
assert_eq!(i16::MAX.saturating_add_unsigned(100), i16::MAX);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating integer subtraction. Computes `self - rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-59)Examples

```rust
assert_eq!(100i16.saturating_sub(127), -27);
assert_eq!(i16::MIN.saturating_sub(100), i16::MIN);
assert_eq!(i16::MAX.saturating_sub(-1), i16::MAX);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating subtraction with an unsigned integer. Computes `self - rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-60)Examples

```rust
assert_eq!(100i16.saturating_sub_unsigned(127), -27);
assert_eq!(i16::MIN.saturating_sub_unsigned(100), i16::MIN);
```

1.45.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating integer negation. Computes `-self`, returning `MAX` if `self == MIN` instead of overflowing.

##### [§](#examples-61)Examples

```rust
assert_eq!(100i16.saturating_neg(), -100);
assert_eq!((-100i16).saturating_neg(), 100);
assert_eq!(i16::MIN.saturating_neg(), i16::MAX);
assert_eq!(i16::MAX.saturating_neg(), i16::MIN + 1);
```

1.45.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating absolute value. Computes `self.abs()`, returning `MAX` if `self == MIN` instead of overflowing.

##### [§](#examples-62)Examples

```rust
assert_eq!(100i16.saturating_abs(), 100);
assert_eq!((-100i16).saturating_abs(), 100);
assert_eq!(i16::MIN.saturating_abs(), i16::MAX);
assert_eq!((i16::MIN + 1).saturating_abs(), i16::MAX);
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating integer multiplication. Computes `self * rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-63)Examples

```rust
assert_eq!(10i16.saturating_mul(12), 120);
assert_eq!(i16::MAX.saturating_mul(10), i16::MAX);
assert_eq!(i16::MIN.saturating_mul(10), i16::MIN);
```

1.58.0 (const: 1.58.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating integer division. Computes `self / rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#panics-15)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-64)Examples

```rust
assert_eq!(5i16.saturating_div(2), 2);
assert_eq!(i16::MAX.saturating_div(-1), i16::MIN + 1);
assert_eq!(i16::MIN.saturating_div(-1), i16::MAX);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Saturating integer exponentiation. Computes `self.pow(exp)`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-65)Examples

```rust
assert_eq!((-4i16).saturating_pow(3), -64);
assert_eq!(0_i16.saturating_pow(0), 1);
assert_eq!(i16::MIN.saturating_pow(2), i16::MAX);
assert_eq!(i16::MIN.saturating_pow(3), i16::MIN);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) addition. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-66)Examples

```rust
assert_eq!(100i16.wrapping_add(27), 127);
assert_eq!(i16::MAX.wrapping_add(2), i16::MIN + 1);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) addition with an unsigned integer. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-67)Examples

```rust
assert_eq!(100i16.wrapping_add_unsigned(27), 127);
assert_eq!(i16::MAX.wrapping_add_unsigned(2), i16::MIN + 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) subtraction. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-68)Examples

```rust
assert_eq!(0i16.wrapping_sub(127), -127);
assert_eq!((-2i16).wrapping_sub(i16::MAX), i16::MAX);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) subtraction with an unsigned integer. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-69)Examples

```rust
assert_eq!(0i16.wrapping_sub_unsigned(127), -127);
assert_eq!((-2i16).wrapping_sub_unsigned(u16::MAX), -1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) multiplication. Computes `self * rhs`, wrapping around at the boundary of the type.

##### [§](#examples-70)Examples

```rust
assert_eq!(10i16.wrapping_mul(12), 120);
assert_eq!(11i8.wrapping_mul(12), -124);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) division. Computes `self / rhs`, wrapping around at the boundary of the type.

The only case where such wrapping can occur is when one divides `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type); this is equivalent to `-MIN`, a positive value that is too large to represent in the type. In such a case, this function returns `MIN` itself.

##### [§](#panics-16)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-71)Examples

```rust
assert_eq!(100i16.wrapping_div(10), 10);
assert_eq!((-128i8).wrapping_div(-1), -128);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping Euclidean division. Computes `self.div_euclid(rhs)`, wrapping around at the boundary of the type.

Wrapping will only occur in `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type). This is equivalent to `-MIN`, a positive value that is too large to represent in the type. In this case, this method returns `MIN` itself.

##### [§](#panics-17)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-72)Examples

```rust
assert_eq!(100i16.wrapping_div_euclid(10), 10);
assert_eq!((-128i8).wrapping_div_euclid(-1), -128);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) remainder. Computes `self % rhs`, wrapping around at the boundary of the type.

Such wrap-around never actually occurs mathematically; implementation artifacts make `x % y` invalid for `MIN / -1` on a signed type (where `MIN` is the negative minimal value). In such a case, this function returns `0`.

##### [§](#panics-18)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-73)Examples

```rust
assert_eq!(100i16.wrapping_rem(10), 0);
assert_eq!((-128i8).wrapping_rem(-1), 0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping Euclidean remainder. Computes `self.rem_euclid(rhs)`, wrapping around at the boundary of the type.

Wrapping will only occur in `MIN % -1` on a signed type (where `MIN` is the negative minimal value for the type). In this case, this method returns 0.

##### [§](#panics-19)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-74)Examples

```rust
assert_eq!(100i16.wrapping_rem_euclid(10), 0);
assert_eq!((-128i8).wrapping_rem_euclid(-1), 0);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) negation. Computes `-self`, wrapping around at the boundary of the type.

The only case where such wrapping can occur is when one negates `MIN` on a signed type (where `MIN` is the negative minimal value for the type); this is a positive value that is too large to represent in the type. In such a case, this function returns `MIN` itself.

##### [§](#examples-75)Examples

```rust
assert_eq!(100i16.wrapping_neg(), -100);
assert_eq!((-100i16).wrapping_neg(), 100);
assert_eq!(i16::MIN.wrapping_neg(), i16::MIN);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Panic-free bitwise shift-left; yields `self << mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `<<` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shl`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.unbounded_shl "method i16::unbounded_shl") which has nicer behaviour.

Note that this is *not* the same as a rotate-left; the RHS of a wrapping shift-left is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_left`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.rotate_left "method i16::rotate_left") function, which may be what you want instead.

##### [§](#examples-76)Examples

```rust
assert_eq!((-1_i16).wrapping_shl(7), -128);
assert_eq!(42_i16.wrapping_shl(16), 42);
assert_eq!(42_i16.wrapping_shl(1).wrapping_shl(15), 0);
assert_eq!((-1_i16).wrapping_shl(128), -1);
assert_eq!(5_i16.wrapping_shl(1025), 10);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Panic-free bitwise shift-right; yields `self >> mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `>>` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shr`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.unbounded_shr "method i16::unbounded_shr") which has nicer behaviour.

Note that this is *not* the same as a rotate-right; the RHS of a wrapping shift-right is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_right`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.rotate_right "method i16::rotate_right") function, which may be what you want instead.

##### [§](#examples-77)Examples

```rust
assert_eq!((-128_i16).wrapping_shr(7), -1);
assert_eq!(42_i16.wrapping_shr(16), 42);
assert_eq!(42_i16.wrapping_shr(1).wrapping_shr(15), 0);
assert_eq!((-128_i16).wrapping_shr(64), -128);
assert_eq!(10_i16.wrapping_shr(1025), 5);
```

1.13.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) absolute value. Computes `self.abs()`, wrapping around at the boundary of the type.

The only case where such wrapping can occur is when one takes the absolute value of the negative minimal value for the type; this is a positive value that is too large to represent in the type. In such a case, this function returns `MIN` itself.

##### [§](#examples-78)Examples

```rust
assert_eq!(100i16.wrapping_abs(), 100);
assert_eq!((-100i16).wrapping_abs(), 100);
assert_eq!(i16::MIN.wrapping_abs(), i16::MIN);
assert_eq!((-128i8).wrapping_abs() as u8, 128);
```

1.51.0 (const: 1.51.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Computes the absolute value of `self` without any wrapping or panicking.

##### [§](#examples-79)Examples

```rust
assert_eq!(100i16.unsigned_abs(), 100u16);
assert_eq!((-100i16).unsigned_abs(), 100u16);
assert_eq!((-128i8).unsigned_abs(), 128u8);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Wrapping (modular) exponentiation. Computes `self.pow(exp)`, wrapping around at the boundary of the type.

##### [§](#examples-80)Examples

```rust
assert_eq!(3i16.wrapping_pow(4), 81);
assert_eq!(3i8.wrapping_pow(5), -13);
assert_eq!(3i8.wrapping_pow(6), -39);
assert_eq!(0_i16.wrapping_pow(0), 1);
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates `self` + `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MAX "associated constant i16::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MIN "associated constant i16::MIN")).

##### [§](#examples-81)Examples

```rust
assert_eq!(5i16.overflowing_add(2), (7, false));
assert_eq!(i16::MAX.overflowing_add(1), (i16::MIN, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Calculates `self` + `rhs` + `carry` and checks for overflow.

Performs “ternary addition” of two integer operands and a carry-in bit, and returns a tuple of the sum along with a boolean indicating whether an arithmetic overflow would occur. On overflow, the wrapped value is returned.

This allows chaining together multiple additions to create a wider addition, and can be useful for bignum addition. This method should only be used for the most significant word; for the less significant words the unsigned method [`u16::carrying_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.carrying_add "method u16::carrying_add") should be used.

The output boolean returned by this method is *not* a carry flag, and should *not* be added to a more significant word.

If overflow occurred, the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MAX "associated constant i16::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MIN "associated constant i16::MIN")).

If the input carry is false, this method is equivalent to [`overflowing_add`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.overflowing_add "method i16::overflowing_add").

##### [§](#examples-82)Examples

```rust
#![feature(signed_bigint_helpers)]
// Only the most significant word is signed.
//
//   10  MAX    (a = 10 × 2^16 + 2^16 - 1)
// + -5    9    (b = -5 × 2^16 + 9)
// ---------
//    6    8    (sum = 6 × 2^16 + 8)

let (a1, a0): (i16, u16) = (10, u16::MAX);
let (b1, b0): (i16, u16) = (-5, 9);
let carry0 = false;

// u16::carrying_add for the less significant words
let (sum0, carry1) = a0.carrying_add(b0, carry0);
assert_eq!(carry1, true);

// i16::carrying_add for the most significant word
let (sum1, overflow) = a1.carrying_add(b1, carry1);
assert_eq!(overflow, false);

assert_eq!((sum1, sum0), (6, 8));
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates `self` + `rhs` with an unsigned `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-83)Examples

```rust
assert_eq!(1i16.overflowing_add_unsigned(2), (3, false));
assert_eq!((i16::MIN).overflowing_add_unsigned(u16::MAX), (i16::MAX, false));
assert_eq!((i16::MAX - 2).overflowing_add_unsigned(3), (i16::MIN, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates `self` - `rhs`.

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MAX "associated constant i16::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MIN "associated constant i16::MIN")).

##### [§](#examples-84)Examples

```rust
assert_eq!(5i16.overflowing_sub(2), (3, false));
assert_eq!(i16::MIN.overflowing_sub(1), (i16::MAX, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Calculates `self` − `rhs` − `borrow` and checks for overflow.

Performs “ternary subtraction” by subtracting both an integer operand and a borrow-in bit from `self`, and returns a tuple of the difference along with a boolean indicating whether an arithmetic overflow would occur. On overflow, the wrapped value is returned.

This allows chaining together multiple subtractions to create a wider subtraction, and can be useful for bignum subtraction. This method should only be used for the most significant word; for the less significant words the unsigned method [`u16::borrowing_sub`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.borrowing_sub "method u16::borrowing_sub") should be used.

The output boolean returned by this method is *not* a borrow flag, and should *not* be subtracted from a more significant word.

If overflow occurred, the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MAX "associated constant i16::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MIN "associated constant i16::MIN")).

If the input borrow is false, this method is equivalent to [`overflowing_sub`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.overflowing_sub "method i16::overflowing_sub").

##### [§](#examples-85)Examples

```rust
#![feature(signed_bigint_helpers)]
// Only the most significant word is signed.
//
//    6    8    (a = 6 × 2^16 + 8)
// - -5    9    (b = -5 × 2^16 + 9)
// ---------
//   10  MAX    (diff = 10 × 2^16 + 2^16 - 1)

let (a1, a0): (i16, u16) = (6, 8);
let (b1, b0): (i16, u16) = (-5, 9);
let borrow0 = false;

// u16::borrowing_sub for the less significant words
let (diff0, borrow1) = a0.borrowing_sub(b0, borrow0);
assert_eq!(borrow1, true);

// i16::borrowing_sub for the most significant word
let (diff1, overflow) = a1.borrowing_sub(b1, borrow1);
assert_eq!(overflow, false);

assert_eq!((diff1, diff0), (10, u16::MAX));
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates `self` - `rhs` with an unsigned `rhs`.

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-86)Examples

```rust
assert_eq!(1i16.overflowing_sub_unsigned(2), (-1, false));
assert_eq!((i16::MAX).overflowing_sub_unsigned(u16::MAX), (i16::MIN, false));
assert_eq!((i16::MIN + 2).overflowing_sub_unsigned(3), (i16::MAX, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates the multiplication of `self` and `rhs`.

Returns a tuple of the multiplication along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-87)Examples

```rust
assert_eq!(5i16.overflowing_mul(2), (10, false));
assert_eq!(1_000_000_000i32.overflowing_mul(10), (1410065408, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`widening_mul` [#152016](https://github.com/rust-lang/rust/issues/152016))

Calculates the complete product `self * rhs` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

If you also need to add a carry to the wide result, then you want [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.carrying_mul "method i16::carrying_mul") instead.

##### [§](#examples-88)Examples

Please note that this example is shared among integer types, which is why `i32` is used.

```rust
#![feature(widening_mul)]
assert_eq!(5i32.widening_mul(-2), (4294967286, -1));
assert_eq!(1_000_000_000i32.widening_mul(-10), (2884901888, -3));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Calculates the “full multiplication” `self * rhs + carry` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you don’t need the `carry`, then you can use [`Self::widening_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.widening_mul "method i16::widening_mul") instead.

##### [§](#examples-89)Examples

Please note that this example is shared among integer types, which is why `i32` is used.

```rust
#![feature(signed_bigint_helpers)]
assert_eq!(5i32.carrying_mul(-2, 0), (4294967286, -1));
assert_eq!(5i32.carrying_mul(-2, 10), (0, 0));
assert_eq!(1_000_000_000i32.carrying_mul(-10, 0), (2884901888, -3));
assert_eq!(1_000_000_000i32.carrying_mul(-10, 10), (2884901898, -3));
assert_eq!(i16::MAX.carrying_mul(i16::MAX, i16::MAX), (i16::MAX.unsigned_abs() + 1, i16::MAX / 2));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Calculates the “full multiplication” `self * rhs + carry + add` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you don’t need either `carry`, then you can use [`Self::widening_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.widening_mul "method i16::widening_mul") instead, and if you only need one `carry`, then you can use [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.carrying_mul "method i16::carrying_mul") instead.

##### [§](#examples-90)Examples

Please note that this example is shared among integer types, which is why `i32` is used.

```rust
#![feature(signed_bigint_helpers)]
assert_eq!(5i32.carrying_mul_add(-2, 0, 0), (4294967286, -1));
assert_eq!(5i32.carrying_mul_add(-2, 10, 10), (10, 0));
assert_eq!(1_000_000_000i32.carrying_mul_add(-10, 0, 0), (2884901888, -3));
assert_eq!(1_000_000_000i32.carrying_mul_add(-10, 10, 10), (2884901908, -3));
assert_eq!(i16::MAX.carrying_mul_add(i16::MAX, i16::MAX, i16::MAX), (u16::MAX, i16::MAX / 2));
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates the divisor when `self` is divided by `rhs`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then self is returned.

##### [§](#panics-20)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-91)Examples

```rust
assert_eq!(5i16.overflowing_div(2), (2, false));
assert_eq!(i16::MIN.overflowing_div(-1), (i16::MIN, true));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates the quotient of Euclidean division `self.div_euclid(rhs)`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then `self` is returned.

##### [§](#panics-21)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-92)Examples

```rust
assert_eq!(5i16.overflowing_div_euclid(2), (2, false));
assert_eq!(i16::MIN.overflowing_div_euclid(-1), (i16::MIN, true));
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates the remainder when `self` is divided by `rhs`.

Returns a tuple of the remainder after dividing along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then 0 is returned.

##### [§](#panics-22)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-93)Examples

```rust
assert_eq!(5i16.overflowing_rem(2), (1, false));
assert_eq!(i16::MIN.overflowing_rem(-1), (0, true));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Overflowing Euclidean remainder. Calculates `self.rem_euclid(rhs)`.

Returns a tuple of the remainder after dividing along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then 0 is returned.

##### [§](#panics-23)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-94)Examples

```rust
assert_eq!(5i16.overflowing_rem_euclid(2), (1, false));
assert_eq!(i16::MIN.overflowing_rem_euclid(-1), (0, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Negates self, overflowing if this is equal to the minimum value.

Returns a tuple of the negated version of self along with a boolean indicating whether an overflow happened. If `self` is the minimum value (e.g., `i32::MIN` for values of type `i32`), then the minimum value will be returned again and `true` will be returned for an overflow happening.

##### [§](#examples-95)Examples

```rust
assert_eq!(2i16.overflowing_neg(), (-2, false));
assert_eq!(i16::MIN.overflowing_neg(), (i16::MIN, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Shifts self left by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-96)Examples

```rust
assert_eq!(0x1i16.overflowing_shl(4), (0x10, false));
assert_eq!(0x1i32.overflowing_shl(36), (0x10, true));
assert_eq!(0x10i16.overflowing_shl(15), (0, false));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Shifts self right by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-97)Examples

```rust
assert_eq!(0x10i16.overflowing_shr(4), (0x1, false));
assert_eq!(0x10i32.overflowing_shr(36), (0x1, true));
```

1.13.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Computes the absolute value of `self`.

Returns a tuple of the absolute version of self along with a boolean indicating whether an overflow happened. If self is the minimum value (e.g., i16::MIN for values of type i16), then the minimum value will be returned again and true will be returned for an overflow happening.

##### [§](#examples-98)Examples

```rust
assert_eq!(10i16.overflowing_abs(), (10, false));
assert_eq!((-10i16).overflowing_abs(), (10, false));
assert_eq!((i16::MIN).overflowing_abs(), (i16::MIN, true));
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Raises self to the power of `exp`, using exponentiation by squaring.

Returns a tuple of the exponentiation along with a bool indicating whether an overflow happened.

##### [§](#examples-99)Examples

```rust
assert_eq!(3i16.overflowing_pow(4), (81, false));
assert_eq!(0_i16.overflowing_pow(0), (1, false));
assert_eq!(3i8.overflowing_pow(5), (-13, true));
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Raises self to the power of `exp`, using exponentiation by squaring.

##### [§](#examples-100)Examples

```rust
let x: i16 = 2; // or any other integer type

assert_eq!(x.pow(5), 32);
assert_eq!(0_i16.pow(0), 1);
```

1.84.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the square root of the number, rounded down.

##### [§](#panics-24)Panics

This function will panic if `self` is negative.

##### [§](#examples-101)Examples

```rust
assert_eq!(10i16.isqrt(), 3);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates the quotient of Euclidean division of `self` by `rhs`.

This computes the integer `q` such that `self = q * rhs + r`, with `r = self.rem_euclid(rhs)` and `0 <= r < abs(rhs)`.

In other words, the result is `self / rhs` rounded to the integer `q` such that `self >= q * rhs`. If `self > 0`, this is equal to rounding towards zero (the default in Rust); if `self < 0`, this is equal to rounding away from zero (towards +/- infinity). If `rhs > 0`, this is equal to rounding towards -infinity; if `rhs < 0`, this is equal to rounding towards +infinity.

##### [§](#panics-25)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-102)Examples

```rust
let a: i16 = 7; // or any other integer type
let b = 4;

assert_eq!(a.div_euclid(b), 1); // 7 >= 4 * 1
assert_eq!(a.div_euclid(-b), -1); // 7 >= -4 * -1
assert_eq!((-a).div_euclid(b), -2); // -7 >= 4 * -2
assert_eq!((-a).div_euclid(-b), 2); // -7 >= -4 * 2
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Calculates the least nonnegative remainder of `self` when divided by `rhs`.

This is done as if by the Euclidean division algorithm – given `r = self.rem_euclid(rhs)`, the result satisfies `self = rhs * self.div_euclid(rhs) + r` and `0 <= r < abs(rhs)`.

##### [§](#panics-26)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-103)Examples

```rust
let a: i16 = 7; // or any other integer type
let b = 4;

assert_eq!(a.rem_euclid(b), 3);
assert_eq!((-a).rem_euclid(b), 1);
assert_eq!(a.rem_euclid(-b), 3);
assert_eq!((-a).rem_euclid(-b), 1);
```

This will panic:

[ⓘ](# "This example panics")

```rust
let _ = i16::MIN.rem_euclid(-1);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Calculates the quotient of `self` and `rhs`, rounding the result towards negative infinity.

##### [§](#panics-27)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-104)Examples

```rust
#![feature(int_roundings)]
let a: i16 = 8;
let b = 3;

assert_eq!(a.div_floor(b), 2);
assert_eq!(a.div_floor(-b), -3);
assert_eq!((-a).div_floor(b), -3);
assert_eq!((-a).div_floor(-b), 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Calculates the quotient of `self` and `rhs`, rounding the result towards positive infinity.

##### [§](#panics-28)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-105)Examples

```rust
#![feature(int_roundings)]
let a: i16 = 8;
let b = 3;

assert_eq!(a.div_ceil(b), 3);
assert_eq!(a.div_ceil(-b), -2);
assert_eq!((-a).div_ceil(b), -2);
assert_eq!((-a).div_ceil(-b), 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

If `rhs` is positive, calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`. If `rhs` is negative, calculates the largest value less than or equal to `self` that is a multiple of `rhs`.

##### [§](#panics-29)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-15)Overflow behavior

On overflow, this function will panic if overflow checks are enabled (default in debug mode) and wrap if overflow checks are disabled (default in release mode).

##### [§](#examples-106)Examples

```rust
#![feature(int_roundings)]
assert_eq!(16_i16.next_multiple_of(8), 16);
assert_eq!(23_i16.next_multiple_of(8), 24);
assert_eq!(16_i16.next_multiple_of(-8), 16);
assert_eq!(23_i16.next_multiple_of(-8), 16);
assert_eq!((-16_i16).next_multiple_of(8), -16);
assert_eq!((-23_i16).next_multiple_of(8), -16);
assert_eq!((-16_i16).next_multiple_of(-8), -16);
assert_eq!((-23_i16).next_multiple_of(-8), -24);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

If `rhs` is positive, calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`. If `rhs` is negative, calculates the largest value less than or equal to `self` that is a multiple of `rhs`. Returns `None` if `rhs` is zero or the operation would result in overflow.

##### [§](#examples-107)Examples

```rust
#![feature(int_roundings)]
assert_eq!(16_i16.checked_next_multiple_of(8), Some(16));
assert_eq!(23_i16.checked_next_multiple_of(8), Some(24));
assert_eq!(16_i16.checked_next_multiple_of(-8), Some(16));
assert_eq!(23_i16.checked_next_multiple_of(-8), Some(16));
assert_eq!((-16_i16).checked_next_multiple_of(8), Some(-16));
assert_eq!((-23_i16).checked_next_multiple_of(8), Some(-16));
assert_eq!((-16_i16).checked_next_multiple_of(-8), Some(-16));
assert_eq!((-23_i16).checked_next_multiple_of(-8), Some(-24));
assert_eq!(1_i16.checked_next_multiple_of(0), None);
assert_eq!(i16::MAX.checked_next_multiple_of(2), None);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

This method might not be optimized owing to implementation details; `ilog2` can produce results more efficiently for base 2, and `ilog10` can produce results more efficiently for base 10.

##### [§](#panics-30)Panics

This function will panic if `self` is less than or equal to zero, or if `base` is less than 2.

##### [§](#examples-108)Examples

```rust
assert_eq!(5i16.ilog(5), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the base 2 logarithm of the number, rounded down.

##### [§](#panics-31)Panics

This function will panic if `self` is less than or equal to zero.

##### [§](#examples-109)Examples

```rust
assert_eq!(2i16.ilog2(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the base 10 logarithm of the number, rounded down.

##### [§](#panics-32)Panics

This function will panic if `self` is less than or equal to zero.

##### [§](#example)Example

```rust
assert_eq!(10i16.ilog10(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

Returns `None` if the number is negative or zero, or if the base is not at least 2.

This method might not be optimized owing to implementation details; `checked_ilog2` can produce results more efficiently for base 2, and `checked_ilog10` can produce results more efficiently for base 10.

##### [§](#examples-110)Examples

```rust
assert_eq!(5i16.checked_ilog(5), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the base 2 logarithm of the number, rounded down.

Returns `None` if the number is negative or zero.

##### [§](#examples-111)Examples

```rust
assert_eq!(2i16.checked_ilog2(), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the base 10 logarithm of the number, rounded down.

Returns `None` if the number is negative or zero.

##### [§](#example-1)Example

```rust
assert_eq!(10i16.checked_ilog10(), Some(1));
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Computes the absolute value of `self`.

##### [§](#overflow-behavior-16)Overflow behavior

The absolute value of `i16::MIN` cannot be represented as an `i16`, and attempting to calculate it will cause an overflow. This means that code in debug mode will trigger a panic on this case and optimized code will return `i16::MIN` without a panic. If you do not want this behavior, consider using [`unsigned_abs`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.unsigned_abs "method i16::unsigned_abs") instead.

##### [§](#examples-112)Examples

```rust
assert_eq!(10i16.abs(), 10);
assert_eq!((-10i16).abs(), 10);
```

1.60.0 (const: 1.60.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Computes the absolute difference between `self` and `other`.

This function always returns the correct answer without overflow or panics by returning an unsigned integer.

##### [§](#examples-113)Examples

```rust
assert_eq!(100i16.abs_diff(80), 20u16);
assert_eq!(100i16.abs_diff(110), 10u16);
assert_eq!((-100i16).abs_diff(80), 180u16);
assert_eq!((-100i16).abs_diff(-120), 20u16);
assert_eq!(i16::MIN.abs_diff(i16::MAX), u16::MAX);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns a number representing sign of `self`.

- `0` if the number is zero
- `1` if the number is positive
- `-1` if the number is negative

##### [§](#examples-114)Examples

```rust
assert_eq!(10i16.signum(), 1);
assert_eq!(0i16.signum(), 0);
assert_eq!((-10i16).signum(), -1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns `true` if `self` is positive and `false` if the number is zero or negative.

##### [§](#examples-115)Examples

```rust
assert!(10i16.is_positive());
assert!(!(-10i16).is_positive());
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns `true` if `self` is negative and `false` if the number is zero or positive.

##### [§](#examples-116)Examples

```rust
assert!((-10i16).is_negative());
assert!(!10i16.is_negative());
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the memory representation of this integer as a byte array in big-endian (network) byte order.

##### [§](#examples-117)Examples

```rust
let bytes = 0x1234i16.to_be_bytes();
assert_eq!(bytes, [0x12, 0x34]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the memory representation of this integer as a byte array in little-endian byte order.

##### [§](#examples-118)Examples

```rust
let bytes = 0x1234i16.to_le_bytes();
assert_eq!(bytes, [0x34, 0x12]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Returns the memory representation of this integer as a byte array in native byte order.

As the target platform’s native endianness is used, portable code should use [`to_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.to_be_bytes "method i16::to_be_bytes") or [`to_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.to_le_bytes "method i16::to_le_bytes"), as appropriate, instead.

##### [§](#examples-119)Examples

```rust
let bytes = 0x1234i16.to_ne_bytes();
assert_eq!(
    bytes,
    if cfg!(target_endian = "big") {
        [0x12, 0x34]
    } else {
        [0x34, 0x12]
    }
);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Creates an integer value from its representation as a byte array in big endian.

##### [§](#examples-120)Examples

```rust
let value = i16::from_be_bytes([0x12, 0x34]);
assert_eq!(value, 0x1234);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_be_i16(input: &mut &[u8]) -> i16 {
    let (int_bytes, rest) = input.split_at(size_of::<i16>());
    *input = rest;
    i16::from_be_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Creates an integer value from its representation as a byte array in little endian.

##### [§](#examples-121)Examples

```rust
let value = i16::from_le_bytes([0x34, 0x12]);
assert_eq!(value, 0x1234);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_le_i16(input: &mut &[u8]) -> i16 {
    let (int_bytes, rest) = input.split_at(size_of::<i16>());
    *input = rest;
    i16::from_le_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

Creates an integer value from its memory representation as a byte array in native endianness.

As the target platform’s native endianness is used, portable code likely wants to use [`from_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.from_be_bytes "associated function i16::from_be_bytes") or [`from_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.from_le_bytes "associated function i16::from_le_bytes"), as appropriate instead.

##### [§](#examples-122)Examples

```rust
let value = i16::from_ne_bytes(if cfg!(target_endian = "big") {
    [0x12, 0x34]
} else {
    [0x34, 0x12]
});
assert_eq!(value, 0x1234);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_ne_i16(input: &mut &[u8]) -> i16 {
    let (int_bytes, rest) = input.split_at(size_of::<i16>());
    *input = rest;
    i16::from_ne_bytes(int_bytes.try_into().unwrap())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

👎Deprecating in a future version: replaced by the `MIN` associated constant on this type

New code should prefer to use [`i16::MIN`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MIN "associated constant i16::MIN") instead.

Returns the smallest value that can be represented by this integer type.

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

👎Deprecating in a future version: replaced by the `MAX` associated constant on this type

New code should prefer to use [`i16::MAX`](https://doc.rust-lang.org/stable/std/primitive.i16.html#associatedconstant.MAX "associated constant i16::MAX") instead.

Returns the largest value that can be represented by this integer type.

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#370-389)

🔬This is a nightly-only experimental API. (`clamp_magnitude` [#148519](https://github.com/rust-lang/rust/issues/148519))

Clamps this number to a symmetric range centred around zero.

The method clamps the number’s magnitude (absolute value) to be at most `limit`.

This is functionally equivalent to `self.clamp(-limit, limit)`, but is more explicit about the intent.

##### [§](#examples-123)Examples

```rust
#![feature(clamp_magnitude)]
assert_eq!(120i16.clamp_magnitude(100), 100);
assert_eq!(-120i16.clamp_magnitude(100), -100);
assert_eq!(80i16.clamp_magnitude(100), 80);
assert_eq!(-80i16.clamp_magnitude(100), -80);
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#390)

Calculates the midpoint (average) between `self` and `rhs`.

`midpoint(a, b)` is `(a + b) / 2` as if it were performed in a sufficiently-large signed integral type. This implies that the result is always rounded towards zero and that no overflow will ever occur.

##### [§](#examples-124)Examples

```rust
assert_eq!(0i16.midpoint(4), 2);
assert_eq!((-1i16).midpoint(2), 0);
assert_eq!((-7i16).midpoint(0), -3);
assert_eq!(0i16.midpoint(-7), -3);
assert_eq!(0i16.midpoint(7), 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#impl-i16-1)

1.0.0 (const: 1.82.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)

Parses an integer from a string slice with digits in a given base.

The string is expected to be an optional `+` or `-` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

Digits are a subset of these characters, depending on `radix`:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#panics-33)Panics

This function panics if `radix` is not in the range from 2 to 36.

##### [§](#see-also)See also

If the string to be parsed is in base 10 (decimal), [`from_str`](#method.from_str) or [`str::parse`](https://doc.rust-lang.org/stable/std/primitive.str.html#method.parse) can also be used.

##### [§](#examples-125)Examples

```rust
assert_eq!(i16::from_str_radix("A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(i16::from_str_radix("1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with decimal digits.

The characters are expected to be an optional `+` or `-` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#examples-126)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(i16::from_ascii(b"+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(i16::from_ascii(b"1 ").is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with digits in a given base.

The characters are expected to be an optional `+` or `-` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

Digits are a subset of these characters, depending on `radix`:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#panics-34)Panics

This function panics if `radix` is not in the range from 2 to 36.

##### [§](#examples-127)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(i16::from_ascii_radix(b"A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(i16::from_ascii_radix(b"1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)[§](#impl-i16-2)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Allows users to write an integer (in signed decimal format) into a variable `buf` of type [`NumBuffer`](https://doc.rust-lang.org/stable/core/fmt/num_buffer/struct.NumBuffer.html "struct core::fmt::num_buffer::NumBuffer") that is passed by the caller by mutable reference.

##### [§](#examples-128)Examples

```rust
#![feature(int_format_into)]
use core::fmt::NumBuffer;

let n = 0i16;
let mut buf = NumBuffer::new();
assert_eq!(n.format_into(&mut buf), "0");

let n1 = 32i16;
assert_eq!(n1.format_into(&mut buf), "32");

let n2 = i16 :: MAX;
assert_eq!(n2.format_into(&mut buf), i16 :: MAX.to_string());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-17)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-16)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-15)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-14)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#300)[§](#impl-AtomicPrimitive-for-i16)

Available on **`target_has_atomic_load_store=16`** only.

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#300)[§](#associatedtype.AtomicInner)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-Binary-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-2)

Format signed integers in the two’s-complement form.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-35)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-34)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-33)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-32)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-3)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-2)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-1)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-31)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-30)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-29)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-28)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#impl-CarryingMulAdd-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#associatedtype.Unsigned)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#method.carrying_mul_add-1)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-i16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#589-592)[§](#impl-Debug-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#178)[§](#impl-Default-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#178)[§](#method.default)

Returns the default value of `0`

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#impl-DisjointBitOr-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#method.disjoint_bitor)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::disjoint_bitor`](https://doc.rust-lang.org/stable/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)[§](#impl-Display-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#52)[§](#impl-Distribution%3Ci16%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#52)[§](#method.sample)

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Samples a random value from the distribution, using the specified random source.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-7)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-6)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-5)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-i16)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-35)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-4)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign-for-i16)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`i16`](https://doc.rust-lang.org/stable/std/primitive.i16.html "primitive i16") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-130)Examples

```rust
assert_eq!(i16::from(false), 0);

assert_eq!(i16::from(true), 1);
```

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3634-3651)[§](#impl-From%3Ci16%3E-for-AtomicI16)

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3634-3651)[§](#method.from-10)

Converts an `i16` into an `AtomicI16`.

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#157)[§](#impl-From%3Ci16%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#155)[§](#impl-From%3Ci16%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#156)[§](#impl-From%3Ci16%3E-for-f64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#109)[§](#impl-From%3Ci16%3E-for-i128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#107)[§](#impl-From%3Ci16%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#108)[§](#impl-From%3Ci16%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#131)[§](#impl-From%3Ci16%3E-for-isize)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#102)[§](#impl-From%3Ci8%3E-for-i16)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#115)[§](#impl-From%3Cu8%3E-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#impl-FromStr-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#method.from_str)

Parses an integer from a string slice with decimal digits.

The characters are expected to be an optional `+` or `-` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#see-also-1)See also

For parsing numbers in other bases, such as binary or hexadecimal, see [`from_str_radix`](https://doc.rust-lang.org/stable/std/primitive.i16.html#method.from_str_radix "associated function i16::from_str_radix").

##### [§](#examples-129)Examples

```rust
use std::str::FromStr;

assert_eq!(i16::from_str("+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(i16::from_str("1 ").is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-i16)

1.42.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#600)[§](#impl-LowerExp-for-i16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-LowerHex-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-4)

Format signed integers in the two’s-complement form.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-25)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-24)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-23)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-22)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-%26i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-%26i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num_buffer.rs.html#26-33)[§](#impl-NumBufferTrait-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num_buffer.rs.html#26-33)[§](#associatedconstant.BUF_SIZE)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Maximum number of digits in decimal base of the implemented integer.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-Octal-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-3)

Format signed integers in the two’s-complement form.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#impl-Ord-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#impl-PartialOrd-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.product-1)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.product)

Takes an iterator and generates `Self` from the elements by multiplying the items.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#impl-RangePattern-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#associatedconstant.MIN-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#associatedconstant.MAX-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#method.sub_one)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

A compile-time helper to subtract 1 for exclusive ranges.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-11)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-10)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-9)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem-for-i16)

This operation satisfies `n % d == n - (n / d) * d`. The result has the same sign as the left operand.

#### [§](#panics-36)Panics

This operation will panic if `other == 0` or if `self / other` results in overflow.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-8)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-107)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-106)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-70)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26i16%3E-for-%26Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-131)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-123)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-95)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-115)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-119)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-63)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-127)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-55)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-43)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-47)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-51)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-39)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-59)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-23)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26i16%3E-for-Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-129)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-122)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-94)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-114)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-118)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-62)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-126)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-54)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-42)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-46)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-50)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-38)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-58)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-22)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-99)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-98)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-103)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-67)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-102)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-91)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-90)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-111)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-110)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-83)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-82)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-71)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-70)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-75)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-74)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-79)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-78)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-67)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-66)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-87)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-86)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-105)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-104)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-68)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Ci16%3E-for-%26Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-130)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-121)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-93)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-113)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-117)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-61)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-125)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-53)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-41)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-45)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-49)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-37)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-57)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-21)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Ci16%3E-for-Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-128)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-120)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-112)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-116)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-60)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-124)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-88)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-52)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-40)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-44)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-48)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-36)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-56)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-20)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-97)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-96)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-101)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-65)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-100)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-89)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-88)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-109)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-108)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-81)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-80)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-69)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-68)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-73)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-72)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-77)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-76)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-65)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-64)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-85)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-84)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-92)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-56)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i128%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i32%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i64%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i8%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u128%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u32%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u64%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26usize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci128%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci32%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci64%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci8%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu128%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu32%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu64%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cusize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-203)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-202)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-70)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26i16%3E-for-%26Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-227)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-219)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-191)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-211)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-215)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-159)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-223)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-151)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-139)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-143)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-147)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-135)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-155)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-23)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26i16%3E-for-Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-225)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-218)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-190)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-210)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-214)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-158)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-222)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-150)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-138)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-142)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-146)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-134)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-154)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-22)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-195)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-194)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-199)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-67)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-198)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-187)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-186)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-207)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-206)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-179)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-178)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-167)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-166)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-171)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-170)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-175)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-174)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-163)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-162)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-183)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-182)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-201)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-200)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-68)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Ci16%3E-for-%26Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-226)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-217)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-189)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-209)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-213)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-157)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-221)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-149)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-137)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-141)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-145)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-133)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-153)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-21)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Ci16%3E-for-Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-224)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-216)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-208)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-212)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-156)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-220)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-88)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-148)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-136)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-140)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-144)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-132)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-152)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-20)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-193)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-192)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-197)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-65)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-196)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-185)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-184)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-205)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-204)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-177)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-176)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-165)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-164)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-169)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-168)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-173)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-172)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-161)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-160)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-181)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-180)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-188)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-56)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i128%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i32%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i64%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i8%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u128%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u32%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u64%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26usize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci128%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci32%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci64%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci8%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu128%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu32%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu64%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cusize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1125)[§](#impl-SimdElement-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1126)[§](#associatedtype.Mask)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#impl-Step-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.forward)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#method.forward)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.backward)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#method.backward)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.forward_unchecked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#method.forward_unchecked)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.backward_unchecked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#method.backward_unchecked)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.steps_between)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the bounds on the number of *successor* steps required to get from `start` to `end` like [`Iterator::size_hint()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.size_hint "method std::iter::Iterator::size_hint"). [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#tymethod.steps_between)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.forward_checked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#tymethod.forward_checked)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#method.backward_checked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Step.html#tymethod.backward_checked)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-21)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-20)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-19)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-18)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3C%26i16%3E-for-Saturating%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3C%26i16%3E-for-Wrapping%3Ci16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign%3C%26i16%3E-for-i16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3Ci16%3E-for-Saturating%3Ci16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3Ci16%3E-for-Wrapping%3Ci16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign-for-i16)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.sum-1)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.sum)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#384)[§](#impl-TryFrom%3Ci128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#384)[§](#method.try_from-4)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#384)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#569)[§](#impl-TryFrom%3Ci16%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#569)[§](#method.try_from-17)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#569)[§](#associatedtype.Error-17)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci16%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#method.try_from)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-131)Examples

```rust
assert_eq!(0_i16.try_into(), Ok(false));

assert_eq!(1_i16.try_into(), Ok(true));

assert!(<i16 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#381)[§](#impl-TryFrom%3Ci16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#381)[§](#method.try_from-1)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#381)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#method.try_from-13)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-13)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#method.try_from-10)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-10)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#method.try_from-11)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-11)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#method.try_from-12)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-12)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#395)[§](#impl-TryFrom%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#395)[§](#method.try_from-9)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#395)[§](#associatedtype.Error-9)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#471)[§](#impl-TryFrom%3Ci16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#471)[§](#method.try_from-16)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#471)[§](#associatedtype.Error-16)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#382)[§](#impl-TryFrom%3Ci32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#382)[§](#method.try_from-2)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#382)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#383)[§](#impl-TryFrom%3Ci64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#383)[§](#method.try_from-3)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#383)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#method.try_from-15)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-15)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#391)[§](#impl-TryFrom%3Cu128%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#391)[§](#method.try_from-8)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#391)[§](#associatedtype.Error-8)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#impl-TryFrom%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#method.try_from-5)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#389)[§](#impl-TryFrom%3Cu32%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#389)[§](#method.try_from-6)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#389)[§](#associatedtype.Error-6)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#390)[§](#impl-TryFrom%3Cu64%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#390)[§](#method.try_from-7)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#390)[§](#associatedtype.Error-7)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#461)[§](#impl-TryFrom%3Cusize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#461)[§](#method.try_from-14)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#461)[§](#associatedtype.Error-14)

The type returned in the event of a conversion error.

1.42.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#600)[§](#impl-UpperExp-for-i16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-UpperHex-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-5)

Format signed integers in the two’s-complement form.

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#69-83)[§](#impl-ZeroablePrimitive-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#69-83)[§](#associatedtype.NonZeroInner)

🔬This is a nightly-only experimental API. (`nonzero_internals`)

A type like `Self` but with a niche that includes zero.

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-i16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-i16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#40)[§](#impl-FloatToInt%3Ci16%3E-for-f128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Ci16%3E-for-f16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Ci16%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#39)[§](#impl-FloatToInt%3Ci16%3E-for-f64)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#109)[§](#impl-MaskElement-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/cast.rs.html#21)[§](#impl-SimdCast-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#17)[§](#impl-TrustedStep-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-i16)

[§](#impl-Freeze-for-i16)

[§](#impl-RefUnwindSafe-for-i16)

[§](#impl-Send-for-i16)

[§](#impl-Sync-for-i16)

[§](#impl-Unpin-for-i16)

[§](#impl-UnsafeUnpin-for-i16)

[§](#impl-UnwindSafe-for-i16)