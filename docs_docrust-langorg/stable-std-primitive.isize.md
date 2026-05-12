---
title: isize - Rust
url: https://doc.rust-lang.org/stable/std/primitive.isize.html
source: crawler
fetched_at: 2026-05-06T21:28:17.584868116-03:00
rendered_js: false
word_count: 13130
summary: This document provides the reference documentation for the Rust 'isize' primitive type, a pointer-sized signed integer that varies based on the target architecture.
tags:
    - rust
    - primitive-types
    - integer
    - isize
    - memory-layout
    - bit-manipulation
category: reference
---

## Primitive Type isize

1.0.0

Expand description

The pointer-sized signed integer type.

The size of this primitive is how many bytes it takes to reference any location in memory. For example, on a 32 bit target, this is 4 bytes and on a 64 bit target, this is 8 bytes.

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#518)[§](#impl-isize)

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

The smallest value that can be represented by this integer type (−263 on 64-bit targets).

##### [§](#examples)Examples

```rust
assert_eq!(isize::MIN, -9223372036854775808);
```

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

The largest value that can be represented by this integer type (263 − 1 on 64-bit targets).

##### [§](#examples-1)Examples

```rust
assert_eq!(isize::MAX, 9223372036854775807);
```

1.53.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

The size of this integer type in bits.

##### [§](#examples-2)Examples

```rust
assert_eq!(isize::BITS, 64);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the number of ones in the binary representation of `self`.

##### [§](#examples-3)Examples

```rust
let n = 0b100_0000isize;

assert_eq!(n.count_ones(), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the number of zeros in the binary representation of `self`.

##### [§](#examples-4)Examples

```rust
assert_eq!(isize::MAX.count_zeros(), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the number of leading zeros in the binary representation of `self`.

Depending on what you’re doing with the value, you might also be interested in the [`ilog2`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.ilog2 "method isize::ilog2") function which returns a consistent number, even if the type widens.

##### [§](#examples-5)Examples

```rust
let n = -1isize;

assert_eq!(n.leading_zeros(), 0);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the number of trailing zeros in the binary representation of `self`.

##### [§](#examples-6)Examples

```rust
let n = -4isize;

assert_eq!(n.trailing_zeros(), 2);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the number of leading ones in the binary representation of `self`.

##### [§](#examples-7)Examples

```rust
let n = -1isize;

assert_eq!(n.leading_ones(), 64);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the number of trailing ones in the binary representation of `self`.

##### [§](#examples-8)Examples

```rust
let n = 3isize;

assert_eq!(n.trailing_ones(), 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Available on **64-bit** only.

Returns `self` with only the most significant bit set, or `0` if the input is `0`.

##### [§](#examples-9)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: isize = 0b_01100100;

assert_eq!(n.isolate_highest_one(), 0b_01000000);
assert_eq!(0_isize.isolate_highest_one(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Available on **64-bit** only.

Returns `self` with only the least significant bit set, or `0` if the input is `0`.

##### [§](#examples-10)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: isize = 0b_01100100;

assert_eq!(n.isolate_lowest_one(), 0b_00000100);
assert_eq!(0_isize.isolate_lowest_one(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Available on **64-bit** only.

Returns the index of the highest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-11)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_isize.highest_one(), None);
assert_eq!(0b1_isize.highest_one(), Some(0));
assert_eq!(0b1_0000_isize.highest_one(), Some(4));
assert_eq!(0b1_1111_isize.highest_one(), Some(4));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Available on **64-bit** only.

Returns the index of the lowest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-12)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_isize.lowest_one(), None);
assert_eq!(0b1_isize.lowest_one(), Some(0));
assert_eq!(0b1_0000_isize.lowest_one(), Some(4));
assert_eq!(0b1_1111_isize.lowest_one(), Some(0));
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the bit pattern of `self` reinterpreted as an unsigned integer of the same size.

This produces the same result as an `as` cast, but ensures that the bit-width remains the same.

##### [§](#examples-13)Examples

```rust
let n = -1isize;

assert_eq!(n.cast_unsigned(), usize::MAX);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Shifts the bits to the left by a specified amount, `n`, wrapping the truncated bits to the end of the resulting integer.

`rotate_left(n)` is equivalent to applying `rotate_left(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `<<` shifting operator!

##### [§](#examples-14)Examples

```rust
let n = 0xaa00000000006e1isize;
let m = 0x6e10aa;

assert_eq!(n.rotate_left(12), m);
assert_eq!(n.rotate_left(1024), n);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Shifts the bits to the right by a specified amount, `n`, wrapping the truncated bits to the beginning of the resulting integer.

`rotate_right(n)` is equivalent to applying `rotate_right(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `>>` shifting operator!

##### [§](#examples-15)Examples

```rust
let n = 0x6e10aaisize;
let m = 0xaa00000000006e1;

assert_eq!(n.rotate_right(12), m);
assert_eq!(n.rotate_right(1024), n);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Reverses the byte order of the integer.

##### [§](#examples-16)Examples

```rust
let n = 0x1234567890123456isize;

let m = n.swap_bytes();

assert_eq!(m, 0x5634129078563412);
```

1.37.0 (const: 1.37.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Reverses the order of bits in the integer. The least significant bit becomes the most significant bit, second least-significant bit becomes second most-significant bit, etc.

##### [§](#examples-17)Examples

```rust
let n = 0x1234567890123456isize;
let m = n.reverse_bits();

assert_eq!(m, 0x6a2c48091e6a2c48);
assert_eq!(0, 0isize.reverse_bits());
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Converts an integer from big endian to the target’s endianness.

On big endian this is a no-op. On little endian the bytes are swapped.

See also [from\_be\_bytes()](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.from_be_bytes "associated function isize::from_be_bytes").

##### [§](#examples-18)Examples

```rust
let n = 0x1Aisize;

if cfg!(target_endian = "big") {
    assert_eq!(isize::from_be(n), n)
} else {
    assert_eq!(isize::from_be(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Converts an integer from little endian to the target’s endianness.

On little endian this is a no-op. On big endian the bytes are swapped.

See also [from\_le\_bytes()](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.from_le_bytes "associated function isize::from_le_bytes").

##### [§](#examples-19)Examples

```rust
let n = 0x1Aisize;

if cfg!(target_endian = "little") {
    assert_eq!(isize::from_le(n), n)
} else {
    assert_eq!(isize::from_le(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Swaps bytes of `self` on little endian targets.

On big endian this is a no-op.

The returned value has the same type as `self`, and will be interpreted as (a potentially different) value of a native-endian `isize`.

See [`to_be_bytes()`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.to_be_bytes "method isize::to_be_bytes") for a type-safe alternative.

##### [§](#examples-20)Examples

```rust
let n = 0x1Aisize;

if cfg!(target_endian = "big") {
    assert_eq!(n.to_be(), n)
} else {
    assert_eq!(n.to_be(), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Swaps bytes of `self` on big endian targets.

On little endian this is a no-op.

The returned value has the same type as `self`, and will be interpreted as (a potentially different) value of a native-endian `isize`.

See [`to_le_bytes()`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.to_le_bytes "method isize::to_le_bytes") for a type-safe alternative.

##### [§](#examples-21)Examples

```rust
let n = 0x1Aisize;

if cfg!(target_endian = "little") {
    assert_eq!(n.to_le(), n)
} else {
    assert_eq!(n.to_le(), n.swap_bytes())
}
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked integer addition. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-22)Examples

```rust
assert_eq!((isize::MAX - 2).checked_add(1), Some(isize::MAX - 1));
assert_eq!((isize::MAX - 2).checked_add(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict integer addition. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics)Panics

###### [§](#overflow-behavior)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-23)Examples

```rust
assert_eq!((isize::MAX - 2).strict_add(1), isize::MAX - 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (isize::MAX - 2).strict_add(3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unchecked integer addition. Computes `self + rhs`, assuming overflow cannot occur.

Calling `x.unchecked_add(y)` is semantically equivalent to calling `x.`[`checked_add`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_add "method isize::checked_add")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_add`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.wrapping_add "method isize::wrapping_add").

##### [§](#safety)Safety

This results in undefined behavior when `self + rhs > isize::MAX` or `self + rhs < isize::MIN`, i.e. when [`checked_add`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_add "method isize::checked_add") would return `None`.

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked addition with an unsigned integer. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-24)Examples

```rust
assert_eq!(1isize.checked_add_unsigned(2), Some(3));
assert_eq!((isize::MAX - 2).checked_add_unsigned(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict addition with an unsigned integer. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics-1)Panics

###### [§](#overflow-behavior-1)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-25)Examples

```rust
assert_eq!(1isize.strict_add_unsigned(2), 3);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (isize::MAX - 2).strict_add_unsigned(3);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked integer subtraction. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-26)Examples

```rust
assert_eq!((isize::MIN + 2).checked_sub(1), Some(isize::MIN + 1));
assert_eq!((isize::MIN + 2).checked_sub(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict integer subtraction. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-2)Panics

###### [§](#overflow-behavior-2)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-27)Examples

```rust
assert_eq!((isize::MIN + 2).strict_sub(1), isize::MIN + 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (isize::MIN + 2).strict_sub(3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unchecked integer subtraction. Computes `self - rhs`, assuming overflow cannot occur.

Calling `x.unchecked_sub(y)` is semantically equivalent to calling `x.`[`checked_sub`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_sub "method isize::checked_sub")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_sub`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.wrapping_sub "method isize::wrapping_sub").

##### [§](#safety-1)Safety

This results in undefined behavior when `self - rhs > isize::MAX` or `self - rhs < isize::MIN`, i.e. when [`checked_sub`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_sub "method isize::checked_sub") would return `None`.

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked subtraction with an unsigned integer. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-28)Examples

```rust
assert_eq!(1isize.checked_sub_unsigned(2), Some(-1));
assert_eq!((isize::MIN + 2).checked_sub_unsigned(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict subtraction with an unsigned integer. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-3)Panics

###### [§](#overflow-behavior-3)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-29)Examples

```rust
assert_eq!(1isize.strict_sub_unsigned(2), -1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (isize::MIN + 2).strict_sub_unsigned(3);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked integer multiplication. Computes `self * rhs`, returning `None` if overflow occurred.

##### [§](#examples-30)Examples

```rust
assert_eq!(isize::MAX.checked_mul(1), Some(isize::MAX));
assert_eq!(isize::MAX.checked_mul(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict integer multiplication. Computes `self * rhs`, panicking if overflow occurred.

##### [§](#panics-4)Panics

###### [§](#overflow-behavior-4)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-31)Examples

```rust
assert_eq!(isize::MAX.strict_mul(1), isize::MAX);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MAX.strict_mul(2);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unchecked integer multiplication. Computes `self * rhs`, assuming overflow cannot occur.

Calling `x.unchecked_mul(y)` is semantically equivalent to calling `x.`[`checked_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_mul "method isize::checked_mul")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.wrapping_mul "method isize::wrapping_mul").

##### [§](#safety-2)Safety

This results in undefined behavior when `self * rhs > isize::MAX` or `self * rhs < isize::MIN`, i.e. when [`checked_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_mul "method isize::checked_mul") would return `None`.

1.0.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked integer division. Computes `self / rhs`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-32)Examples

```rust
assert_eq!((isize::MIN + 1).checked_div(-1), Some(9223372036854775807));
assert_eq!(isize::MIN.checked_div(-1), None);
assert_eq!((1isize).checked_div(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict integer division. Computes `self / rhs`, panicking if overflow occurred.

##### [§](#panics-5)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-5)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is when one divides `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type); this is equivalent to `-MIN`, a positive value that is too large to represent in the type.

##### [§](#examples-33)Examples

```rust
assert_eq!((isize::MIN + 1).strict_div(-1), 9223372036854775807);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.strict_div(-1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1isize).strict_div(0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked Euclidean division. Computes `self.div_euclid(rhs)`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-34)Examples

```rust
assert_eq!((isize::MIN + 1).checked_div_euclid(-1), Some(9223372036854775807));
assert_eq!(isize::MIN.checked_div_euclid(-1), None);
assert_eq!((1isize).checked_div_euclid(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict Euclidean division. Computes `self.div_euclid(rhs)`, panicking if overflow occurred.

##### [§](#panics-6)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-6)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is when one divides `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type); this is equivalent to `-MIN`, a positive value that is too large to represent in the type.

##### [§](#examples-35)Examples

```rust
assert_eq!((isize::MIN + 1).strict_div_euclid(-1), 9223372036854775807);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.strict_div_euclid(-1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1isize).strict_div_euclid(0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Available on **64-bit** only.

Checked integer division without remainder. Computes `self / rhs`, returning `None` if `rhs == 0`, the division results in overflow, or `self % rhs != 0`.

##### [§](#examples-36)Examples

```rust
#![feature(exact_div)]
assert_eq!((isize::MIN + 1).checked_div_exact(-1), Some(9223372036854775807));
assert_eq!((-5isize).checked_div_exact(2), None);
assert_eq!(isize::MIN.checked_div_exact(-1), None);
assert_eq!((1isize).checked_div_exact(0), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Available on **64-bit** only.

Integer division without remainder. Computes `self / rhs`, returning `None` if `self % rhs != 0`.

##### [§](#panics-7)Panics

This function will panic if `rhs == 0`.

###### [§](#overflow-behavior-7)Overflow behavior

On overflow, this function will panic if overflow checks are enabled (default in debug mode) and wrap if overflow checks are disabled (default in release mode).

##### [§](#examples-37)Examples

```rust
#![feature(exact_div)]
assert_eq!(64isize.div_exact(2), Some(32));
assert_eq!(64isize.div_exact(32), Some(2));
assert_eq!((isize::MIN + 1).div_exact(-1), Some(9223372036854775807));
assert_eq!(65isize.div_exact(2), None);
```

[ⓘ](# "This example panics")

```rust
#![feature(exact_div)]
let _ = 64isize.div_exact(0);
```

[ⓘ](# "This example panics")

```rust
#![feature(exact_div)]
let _ = isize::MIN.div_exact(-1);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Available on **64-bit** only.

Unchecked integer division without remainder. Computes `self / rhs`.

##### [§](#safety-3)Safety

This results in undefined behavior when `rhs == 0`, `self % rhs != 0`, or `self == isize::MIN && rhs == -1`, i.e. when [`checked_div_exact`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_div_exact "method isize::checked_div_exact") would return `None`.

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked integer remainder. Computes `self % rhs`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-38)Examples

```rust
assert_eq!(5isize.checked_rem(2), Some(1));
assert_eq!(5isize.checked_rem(0), None);
assert_eq!(isize::MIN.checked_rem(-1), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict integer remainder. Computes `self % rhs`, panicking if the division results in overflow.

##### [§](#panics-8)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-8)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is `x % y` for `MIN / -1` on a signed type (where `MIN` is the negative minimal value), which is invalid due to implementation artifacts.

##### [§](#examples-39)Examples

```rust
assert_eq!(5isize.strict_rem(2), 1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5isize.strict_rem(0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.strict_rem(-1);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked Euclidean remainder. Computes `self.rem_euclid(rhs)`, returning `None` if `rhs == 0` or the division results in overflow.

##### [§](#examples-40)Examples

```rust
assert_eq!(5isize.checked_rem_euclid(2), Some(1));
assert_eq!(5isize.checked_rem_euclid(0), None);
assert_eq!(isize::MIN.checked_rem_euclid(-1), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict Euclidean remainder. Computes `self.rem_euclid(rhs)`, panicking if the division results in overflow.

##### [§](#panics-9)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-9)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

The only case where such an overflow can occur is `x % y` for `MIN / -1` on a signed type (where `MIN` is the negative minimal value), which is invalid due to implementation artifacts.

##### [§](#examples-41)Examples

```rust
assert_eq!(5isize.strict_rem_euclid(2), 1);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5isize.strict_rem_euclid(0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.strict_rem_euclid(-1);
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked negation. Computes `-self`, returning `None` if `self == MIN`.

##### [§](#examples-42)Examples

```rust
assert_eq!(5isize.checked_neg(), Some(-5));
assert_eq!(isize::MIN.checked_neg(), None);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unchecked negation. Computes `-self`, assuming overflow cannot occur.

##### [§](#safety-4)Safety

This results in undefined behavior when `self == isize::MIN`, i.e. when [`checked_neg`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_neg "method isize::checked_neg") would return `None`.

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict negation. Computes `-self`, panicking if `self == MIN`.

##### [§](#panics-10)Panics

###### [§](#overflow-behavior-10)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-43)Examples

```rust
assert_eq!(5isize.strict_neg(), -5);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.strict_neg();
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked shift left. Computes `self << rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-44)Examples

```rust
assert_eq!(0x1isize.checked_shl(4), Some(0x10));
assert_eq!(0x1isize.checked_shl(129), None);
assert_eq!(0x10isize.checked_shl(63), Some(0));
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict shift left. Computes `self << rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-11)Panics

###### [§](#overflow-behavior-11)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-45)Examples

```rust
assert_eq!(0x1isize.strict_shl(4), 0x10);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x1isize.strict_shl(129);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unchecked shift left. Computes `self << rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-5)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shl`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_shl "method isize::checked_shl") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unbounded shift left. Computes `self << rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, and `0` is returned.

##### [§](#examples-46)Examples

```rust
assert_eq!(0x1_isize.unbounded_shl(4), 0x10);
assert_eq!(0x1_isize.unbounded_shl(129), 0);
assert_eq!(0b101_isize.unbounded_shl(0), 0b101);
assert_eq!(0b101_isize.unbounded_shl(1), 0b1010);
assert_eq!(0b101_isize.unbounded_shl(2), 0b10100);
assert_eq!(42_isize.unbounded_shl(64), 0);
assert_eq!(42_isize.unbounded_shl(1).unbounded_shl(63), 0);
assert_eq!((-13_isize).unbounded_shl(64), 0);
assert_eq!((-13_isize).unbounded_shl(1).unbounded_shl(63), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Available on **64-bit** only.

Exact shift left. Computes `self << rhs` as long as it can be reversed losslessly.

Returns `None` if any bits that would be shifted out differ from the resulting sign bit or if `rhs` &gt;= `isize::BITS`. Otherwise, returns `Some(self << rhs)`.

##### [§](#examples-47)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x1isize.shl_exact(4), Some(0x10));
assert_eq!(0x1isize.shl_exact(isize::BITS - 2), Some(1 << isize::BITS - 2));
assert_eq!(0x1isize.shl_exact(isize::BITS - 1), None);
assert_eq!((-0x2isize).shl_exact(isize::BITS - 2), Some(-0x2 << isize::BITS - 2));
assert_eq!((-0x2isize).shl_exact(isize::BITS - 1), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Available on **64-bit** only.

Unchecked exact shift left. Computes `self << rhs`, assuming the operation can be losslessly reversed and `rhs` cannot be larger than `isize::BITS`.

##### [§](#safety-6)Safety

This results in undefined behavior when `rhs >= self.leading_zeros() && rhs >= self.leading_ones()` i.e. when [`isize::shl_exact`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.shl_exact "method isize::shl_exact") would return `None`.

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked shift right. Computes `self >> rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-48)Examples

```rust
assert_eq!(0x10isize.checked_shr(4), Some(0x1));
assert_eq!(0x10isize.checked_shr(128), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict shift right. Computes `self >> rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-12)Panics

###### [§](#overflow-behavior-12)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-49)Examples

```rust
assert_eq!(0x10isize.strict_shr(4), 0x1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x10isize.strict_shr(128);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unchecked shift right. Computes `self >> rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-7)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shr`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.checked_shr "method isize::checked_shr") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Unbounded shift right. Computes `self >> rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, which yields `0` for a positive number, and `-1` for a negative number.

##### [§](#examples-50)Examples

```rust
assert_eq!(0x10_isize.unbounded_shr(4), 0x1);
assert_eq!(0x10_isize.unbounded_shr(129), 0);
assert_eq!(isize::MIN.unbounded_shr(129), -1);
assert_eq!(0b1010_isize.unbounded_shr(0), 0b1010);
assert_eq!(0b1010_isize.unbounded_shr(1), 0b101);
assert_eq!(0b1010_isize.unbounded_shr(2), 0b10);
assert_eq!(42_isize.unbounded_shr(64), 0);
assert_eq!(42_isize.unbounded_shr(1).unbounded_shr(63), 0);
assert_eq!((-13_isize).unbounded_shr(64), -1);
assert_eq!((-13_isize).unbounded_shr(1).unbounded_shr(63), -1);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Available on **64-bit** only.

Exact shift right. Computes `self >> rhs` as long as it can be reversed losslessly.

Returns `None` if any non-zero bits would be shifted out or if `rhs` &gt;= `isize::BITS`. Otherwise, returns `Some(self >> rhs)`.

##### [§](#examples-51)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x10isize.shr_exact(4), Some(0x1));
assert_eq!(0x10isize.shr_exact(5), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Available on **64-bit** only.

Unchecked exact shift right. Computes `self >> rhs`, assuming the operation can be losslessly reversed and `rhs` cannot be larger than `isize::BITS`.

##### [§](#safety-8)Safety

This results in undefined behavior when `rhs > self.trailing_zeros() || rhs >= isize::BITS` i.e. when [`isize::shr_exact`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.shr_exact "method isize::shr_exact") would return `None`.

1.13.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked absolute value. Computes `self.abs()`, returning `None` if `self == MIN`.

##### [§](#examples-52)Examples

```rust
assert_eq!((-5isize).checked_abs(), Some(5));
assert_eq!(isize::MIN.checked_abs(), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict absolute value. Computes `self.abs()`, panicking if `self == MIN`.

##### [§](#panics-13)Panics

###### [§](#overflow-behavior-13)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-53)Examples

```rust
assert_eq!((-5isize).strict_abs(), 5);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.strict_abs();
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Checked exponentiation. Computes `self.pow(exp)`, returning `None` if overflow occurred.

##### [§](#examples-54)Examples

```rust
assert_eq!(8isize.checked_pow(2), Some(64));
assert_eq!(0_isize.checked_pow(0), Some(1));
assert_eq!(isize::MAX.checked_pow(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Strict exponentiation. Computes `self.pow(exp)`, panicking if overflow occurred.

##### [§](#panics-14)Panics

###### [§](#overflow-behavior-14)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-55)Examples

```rust
assert_eq!(8isize.strict_pow(2), 64);
assert_eq!(0_isize.strict_pow(0), 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = isize::MAX.strict_pow(2);
```

1.84.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the square root of the number, rounded down.

Returns `None` if `self` is negative.

##### [§](#examples-56)Examples

```rust
assert_eq!(10isize.checked_isqrt(), Some(3));
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating integer addition. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-57)Examples

```rust
assert_eq!(100isize.saturating_add(1), 101);
assert_eq!(isize::MAX.saturating_add(100), isize::MAX);
assert_eq!(isize::MIN.saturating_add(-1), isize::MIN);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating addition with an unsigned integer. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-58)Examples

```rust
assert_eq!(1isize.saturating_add_unsigned(2), 3);
assert_eq!(isize::MAX.saturating_add_unsigned(100), isize::MAX);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating integer subtraction. Computes `self - rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-59)Examples

```rust
assert_eq!(100isize.saturating_sub(127), -27);
assert_eq!(isize::MIN.saturating_sub(100), isize::MIN);
assert_eq!(isize::MAX.saturating_sub(-1), isize::MAX);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating subtraction with an unsigned integer. Computes `self - rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-60)Examples

```rust
assert_eq!(100isize.saturating_sub_unsigned(127), -27);
assert_eq!(isize::MIN.saturating_sub_unsigned(100), isize::MIN);
```

1.45.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating integer negation. Computes `-self`, returning `MAX` if `self == MIN` instead of overflowing.

##### [§](#examples-61)Examples

```rust
assert_eq!(100isize.saturating_neg(), -100);
assert_eq!((-100isize).saturating_neg(), 100);
assert_eq!(isize::MIN.saturating_neg(), isize::MAX);
assert_eq!(isize::MAX.saturating_neg(), isize::MIN + 1);
```

1.45.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating absolute value. Computes `self.abs()`, returning `MAX` if `self == MIN` instead of overflowing.

##### [§](#examples-62)Examples

```rust
assert_eq!(100isize.saturating_abs(), 100);
assert_eq!((-100isize).saturating_abs(), 100);
assert_eq!(isize::MIN.saturating_abs(), isize::MAX);
assert_eq!((isize::MIN + 1).saturating_abs(), isize::MAX);
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating integer multiplication. Computes `self * rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-63)Examples

```rust
assert_eq!(10isize.saturating_mul(12), 120);
assert_eq!(isize::MAX.saturating_mul(10), isize::MAX);
assert_eq!(isize::MIN.saturating_mul(10), isize::MIN);
```

1.58.0 (const: 1.58.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating integer division. Computes `self / rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#panics-15)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-64)Examples

```rust
assert_eq!(5isize.saturating_div(2), 2);
assert_eq!(isize::MAX.saturating_div(-1), isize::MIN + 1);
assert_eq!(isize::MIN.saturating_div(-1), isize::MAX);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Saturating integer exponentiation. Computes `self.pow(exp)`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-65)Examples

```rust
assert_eq!((-4isize).saturating_pow(3), -64);
assert_eq!(0_isize.saturating_pow(0), 1);
assert_eq!(isize::MIN.saturating_pow(2), isize::MAX);
assert_eq!(isize::MIN.saturating_pow(3), isize::MIN);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) addition. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-66)Examples

```rust
assert_eq!(100isize.wrapping_add(27), 127);
assert_eq!(isize::MAX.wrapping_add(2), isize::MIN + 1);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) addition with an unsigned integer. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-67)Examples

```rust
assert_eq!(100isize.wrapping_add_unsigned(27), 127);
assert_eq!(isize::MAX.wrapping_add_unsigned(2), isize::MIN + 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) subtraction. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-68)Examples

```rust
assert_eq!(0isize.wrapping_sub(127), -127);
assert_eq!((-2isize).wrapping_sub(isize::MAX), isize::MAX);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) subtraction with an unsigned integer. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-69)Examples

```rust
assert_eq!(0isize.wrapping_sub_unsigned(127), -127);
assert_eq!((-2isize).wrapping_sub_unsigned(usize::MAX), -1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) multiplication. Computes `self * rhs`, wrapping around at the boundary of the type.

##### [§](#examples-70)Examples

```rust
assert_eq!(10isize.wrapping_mul(12), 120);
assert_eq!(11i8.wrapping_mul(12), -124);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) division. Computes `self / rhs`, wrapping around at the boundary of the type.

The only case where such wrapping can occur is when one divides `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type); this is equivalent to `-MIN`, a positive value that is too large to represent in the type. In such a case, this function returns `MIN` itself.

##### [§](#panics-16)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-71)Examples

```rust
assert_eq!(100isize.wrapping_div(10), 10);
assert_eq!((-128i8).wrapping_div(-1), -128);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping Euclidean division. Computes `self.div_euclid(rhs)`, wrapping around at the boundary of the type.

Wrapping will only occur in `MIN / -1` on a signed type (where `MIN` is the negative minimal value for the type). This is equivalent to `-MIN`, a positive value that is too large to represent in the type. In this case, this method returns `MIN` itself.

##### [§](#panics-17)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-72)Examples

```rust
assert_eq!(100isize.wrapping_div_euclid(10), 10);
assert_eq!((-128i8).wrapping_div_euclid(-1), -128);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) remainder. Computes `self % rhs`, wrapping around at the boundary of the type.

Such wrap-around never actually occurs mathematically; implementation artifacts make `x % y` invalid for `MIN / -1` on a signed type (where `MIN` is the negative minimal value). In such a case, this function returns `0`.

##### [§](#panics-18)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-73)Examples

```rust
assert_eq!(100isize.wrapping_rem(10), 0);
assert_eq!((-128i8).wrapping_rem(-1), 0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping Euclidean remainder. Computes `self.rem_euclid(rhs)`, wrapping around at the boundary of the type.

Wrapping will only occur in `MIN % -1` on a signed type (where `MIN` is the negative minimal value for the type). In this case, this method returns 0.

##### [§](#panics-19)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-74)Examples

```rust
assert_eq!(100isize.wrapping_rem_euclid(10), 0);
assert_eq!((-128i8).wrapping_rem_euclid(-1), 0);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) negation. Computes `-self`, wrapping around at the boundary of the type.

The only case where such wrapping can occur is when one negates `MIN` on a signed type (where `MIN` is the negative minimal value for the type); this is a positive value that is too large to represent in the type. In such a case, this function returns `MIN` itself.

##### [§](#examples-75)Examples

```rust
assert_eq!(100isize.wrapping_neg(), -100);
assert_eq!((-100isize).wrapping_neg(), 100);
assert_eq!(isize::MIN.wrapping_neg(), isize::MIN);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Panic-free bitwise shift-left; yields `self << mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `<<` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shl`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.unbounded_shl "method isize::unbounded_shl") which has nicer behaviour.

Note that this is *not* the same as a rotate-left; the RHS of a wrapping shift-left is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_left`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.rotate_left "method isize::rotate_left") function, which may be what you want instead.

##### [§](#examples-76)Examples

```rust
assert_eq!((-1_isize).wrapping_shl(7), -128);
assert_eq!(42_isize.wrapping_shl(64), 42);
assert_eq!(42_isize.wrapping_shl(1).wrapping_shl(63), 0);
assert_eq!((-1_isize).wrapping_shl(128), -1);
assert_eq!(5_isize.wrapping_shl(1025), 10);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Panic-free bitwise shift-right; yields `self >> mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `>>` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shr`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.unbounded_shr "method isize::unbounded_shr") which has nicer behaviour.

Note that this is *not* the same as a rotate-right; the RHS of a wrapping shift-right is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_right`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.rotate_right "method isize::rotate_right") function, which may be what you want instead.

##### [§](#examples-77)Examples

```rust
assert_eq!((-128_isize).wrapping_shr(7), -1);
assert_eq!(42_isize.wrapping_shr(64), 42);
assert_eq!(42_isize.wrapping_shr(1).wrapping_shr(63), 0);
assert_eq!((-128_i16).wrapping_shr(64), -128);
assert_eq!(10_isize.wrapping_shr(1025), 5);
```

1.13.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) absolute value. Computes `self.abs()`, wrapping around at the boundary of the type.

The only case where such wrapping can occur is when one takes the absolute value of the negative minimal value for the type; this is a positive value that is too large to represent in the type. In such a case, this function returns `MIN` itself.

##### [§](#examples-78)Examples

```rust
assert_eq!(100isize.wrapping_abs(), 100);
assert_eq!((-100isize).wrapping_abs(), 100);
assert_eq!(isize::MIN.wrapping_abs(), isize::MIN);
assert_eq!((-128i8).wrapping_abs() as u8, 128);
```

1.51.0 (const: 1.51.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Computes the absolute value of `self` without any wrapping or panicking.

##### [§](#examples-79)Examples

```rust
assert_eq!(100isize.unsigned_abs(), 100usize);
assert_eq!((-100isize).unsigned_abs(), 100usize);
assert_eq!((-128i8).unsigned_abs(), 128u8);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Wrapping (modular) exponentiation. Computes `self.pow(exp)`, wrapping around at the boundary of the type.

##### [§](#examples-80)Examples

```rust
assert_eq!(3isize.wrapping_pow(4), 81);
assert_eq!(3i8.wrapping_pow(5), -13);
assert_eq!(3i8.wrapping_pow(6), -39);
assert_eq!(0_isize.wrapping_pow(0), 1);
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates `self` + `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MIN "associated constant isize::MIN")).

##### [§](#examples-81)Examples

```rust
assert_eq!(5isize.overflowing_add(2), (7, false));
assert_eq!(isize::MAX.overflowing_add(1), (isize::MIN, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Available on **64-bit** only.

Calculates `self` + `rhs` + `carry` and checks for overflow.

Performs “ternary addition” of two integer operands and a carry-in bit, and returns a tuple of the sum along with a boolean indicating whether an arithmetic overflow would occur. On overflow, the wrapped value is returned.

This allows chaining together multiple additions to create a wider addition, and can be useful for bignum addition. This method should only be used for the most significant word; for the less significant words the unsigned method [`usize::carrying_add`](https://doc.rust-lang.org/stable/std/primitive.usize.html#method.carrying_add "method usize::carrying_add") should be used.

The output boolean returned by this method is *not* a carry flag, and should *not* be added to a more significant word.

If overflow occurred, the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MIN "associated constant isize::MIN")).

If the input carry is false, this method is equivalent to [`overflowing_add`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.overflowing_add "method isize::overflowing_add").

##### [§](#examples-82)Examples

```rust
#![feature(signed_bigint_helpers)]
// Only the most significant word is signed.
//
//   10  MAX    (a = 10 × 2^64 + 2^64 - 1)
// + -5    9    (b = -5 × 2^64 + 9)
// ---------
//    6    8    (sum = 6 × 2^64 + 8)

let (a1, a0): (isize, usize) = (10, usize::MAX);
let (b1, b0): (isize, usize) = (-5, 9);
let carry0 = false;

// usize::carrying_add for the less significant words
let (sum0, carry1) = a0.carrying_add(b0, carry0);
assert_eq!(carry1, true);

// isize::carrying_add for the most significant word
let (sum1, overflow) = a1.carrying_add(b1, carry1);
assert_eq!(overflow, false);

assert_eq!((sum1, sum0), (6, 8));
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates `self` + `rhs` with an unsigned `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-83)Examples

```rust
assert_eq!(1isize.overflowing_add_unsigned(2), (3, false));
assert_eq!((isize::MIN).overflowing_add_unsigned(usize::MAX), (isize::MAX, false));
assert_eq!((isize::MAX - 2).overflowing_add_unsigned(3), (isize::MIN, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates `self` - `rhs`.

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MIN "associated constant isize::MIN")).

##### [§](#examples-84)Examples

```rust
assert_eq!(5isize.overflowing_sub(2), (3, false));
assert_eq!(isize::MIN.overflowing_sub(1), (isize::MAX, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Available on **64-bit** only.

Calculates `self` − `rhs` − `borrow` and checks for overflow.

Performs “ternary subtraction” by subtracting both an integer operand and a borrow-in bit from `self`, and returns a tuple of the difference along with a boolean indicating whether an arithmetic overflow would occur. On overflow, the wrapped value is returned.

This allows chaining together multiple subtractions to create a wider subtraction, and can be useful for bignum subtraction. This method should only be used for the most significant word; for the less significant words the unsigned method [`usize::borrowing_sub`](https://doc.rust-lang.org/stable/std/primitive.usize.html#method.borrowing_sub "method usize::borrowing_sub") should be used.

The output boolean returned by this method is *not* a borrow flag, and should *not* be subtracted from a more significant word.

If overflow occurred, the wrapped value is returned (negative if overflowed above [`MAX`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX"), non-negative if below [`MIN`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MIN "associated constant isize::MIN")).

If the input borrow is false, this method is equivalent to [`overflowing_sub`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.overflowing_sub "method isize::overflowing_sub").

##### [§](#examples-85)Examples

```rust
#![feature(signed_bigint_helpers)]
// Only the most significant word is signed.
//
//    6    8    (a = 6 × 2^64 + 8)
// - -5    9    (b = -5 × 2^64 + 9)
// ---------
//   10  MAX    (diff = 10 × 2^64 + 2^64 - 1)

let (a1, a0): (isize, usize) = (6, 8);
let (b1, b0): (isize, usize) = (-5, 9);
let borrow0 = false;

// usize::borrowing_sub for the less significant words
let (diff0, borrow1) = a0.borrowing_sub(b0, borrow0);
assert_eq!(borrow1, true);

// isize::borrowing_sub for the most significant word
let (diff1, overflow) = a1.borrowing_sub(b1, borrow1);
assert_eq!(overflow, false);

assert_eq!((diff1, diff0), (10, usize::MAX));
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates `self` - `rhs` with an unsigned `rhs`.

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-86)Examples

```rust
assert_eq!(1isize.overflowing_sub_unsigned(2), (-1, false));
assert_eq!((isize::MAX).overflowing_sub_unsigned(usize::MAX), (isize::MIN, false));
assert_eq!((isize::MIN + 2).overflowing_sub_unsigned(3), (isize::MAX, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates the multiplication of `self` and `rhs`.

Returns a tuple of the multiplication along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-87)Examples

```rust
assert_eq!(5isize.overflowing_mul(2), (10, false));
assert_eq!(1_000_000_000i32.overflowing_mul(10), (1410065408, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`widening_mul` [#152016](https://github.com/rust-lang/rust/issues/152016))

Available on **64-bit** only.

Calculates the complete product `self * rhs` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

If you also need to add a carry to the wide result, then you want [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.carrying_mul "method isize::carrying_mul") instead.

##### [§](#examples-88)Examples

Please note that this example is shared among integer types, which is why `i32` is used.

```rust
#![feature(widening_mul)]
assert_eq!(5i32.widening_mul(-2), (4294967286, -1));
assert_eq!(1_000_000_000i32.widening_mul(-10), (2884901888, -3));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Available on **64-bit** only.

Calculates the “full multiplication” `self * rhs + carry` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you don’t need the `carry`, then you can use [`Self::widening_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.widening_mul "method isize::widening_mul") instead.

##### [§](#examples-89)Examples

Please note that this example is shared among integer types, which is why `i32` is used.

```rust
#![feature(signed_bigint_helpers)]
assert_eq!(5i32.carrying_mul(-2, 0), (4294967286, -1));
assert_eq!(5i32.carrying_mul(-2, 10), (0, 0));
assert_eq!(1_000_000_000i32.carrying_mul(-10, 0), (2884901888, -3));
assert_eq!(1_000_000_000i32.carrying_mul(-10, 10), (2884901898, -3));
assert_eq!(isize::MAX.carrying_mul(isize::MAX, isize::MAX), (isize::MAX.unsigned_abs() + 1, isize::MAX / 2));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`signed_bigint_helpers` [#151989](https://github.com/rust-lang/rust/issues/151989))

Available on **64-bit** only.

Calculates the “full multiplication” `self * rhs + carry + add` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you don’t need either `carry`, then you can use [`Self::widening_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.widening_mul "method isize::widening_mul") instead, and if you only need one `carry`, then you can use [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.carrying_mul "method isize::carrying_mul") instead.

##### [§](#examples-90)Examples

Please note that this example is shared among integer types, which is why `i32` is used.

```rust
#![feature(signed_bigint_helpers)]
assert_eq!(5i32.carrying_mul_add(-2, 0, 0), (4294967286, -1));
assert_eq!(5i32.carrying_mul_add(-2, 10, 10), (10, 0));
assert_eq!(1_000_000_000i32.carrying_mul_add(-10, 0, 0), (2884901888, -3));
assert_eq!(1_000_000_000i32.carrying_mul_add(-10, 10, 10), (2884901908, -3));
assert_eq!(isize::MAX.carrying_mul_add(isize::MAX, isize::MAX, isize::MAX), (usize::MAX, isize::MAX / 2));
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates the divisor when `self` is divided by `rhs`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then self is returned.

##### [§](#panics-20)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-91)Examples

```rust
assert_eq!(5isize.overflowing_div(2), (2, false));
assert_eq!(isize::MIN.overflowing_div(-1), (isize::MIN, true));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates the quotient of Euclidean division `self.div_euclid(rhs)`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then `self` is returned.

##### [§](#panics-21)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-92)Examples

```rust
assert_eq!(5isize.overflowing_div_euclid(2), (2, false));
assert_eq!(isize::MIN.overflowing_div_euclid(-1), (isize::MIN, true));
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates the remainder when `self` is divided by `rhs`.

Returns a tuple of the remainder after dividing along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then 0 is returned.

##### [§](#panics-22)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-93)Examples

```rust
assert_eq!(5isize.overflowing_rem(2), (1, false));
assert_eq!(isize::MIN.overflowing_rem(-1), (0, true));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Overflowing Euclidean remainder. Calculates `self.rem_euclid(rhs)`.

Returns a tuple of the remainder after dividing along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would occur then 0 is returned.

##### [§](#panics-23)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-94)Examples

```rust
assert_eq!(5isize.overflowing_rem_euclid(2), (1, false));
assert_eq!(isize::MIN.overflowing_rem_euclid(-1), (0, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Negates self, overflowing if this is equal to the minimum value.

Returns a tuple of the negated version of self along with a boolean indicating whether an overflow happened. If `self` is the minimum value (e.g., `i32::MIN` for values of type `i32`), then the minimum value will be returned again and `true` will be returned for an overflow happening.

##### [§](#examples-95)Examples

```rust
assert_eq!(2isize.overflowing_neg(), (-2, false));
assert_eq!(isize::MIN.overflowing_neg(), (isize::MIN, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Shifts self left by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-96)Examples

```rust
assert_eq!(0x1isize.overflowing_shl(4), (0x10, false));
assert_eq!(0x1i32.overflowing_shl(36), (0x10, true));
assert_eq!(0x10isize.overflowing_shl(63), (0, false));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Shifts self right by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-97)Examples

```rust
assert_eq!(0x10isize.overflowing_shr(4), (0x1, false));
assert_eq!(0x10i32.overflowing_shr(36), (0x1, true));
```

1.13.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Computes the absolute value of `self`.

Returns a tuple of the absolute version of self along with a boolean indicating whether an overflow happened. If self is the minimum value (e.g., isize::MIN for values of type isize), then the minimum value will be returned again and true will be returned for an overflow happening.

##### [§](#examples-98)Examples

```rust
assert_eq!(10isize.overflowing_abs(), (10, false));
assert_eq!((-10isize).overflowing_abs(), (10, false));
assert_eq!((isize::MIN).overflowing_abs(), (isize::MIN, true));
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Raises self to the power of `exp`, using exponentiation by squaring.

Returns a tuple of the exponentiation along with a bool indicating whether an overflow happened.

##### [§](#examples-99)Examples

```rust
assert_eq!(3isize.overflowing_pow(4), (81, false));
assert_eq!(0_isize.overflowing_pow(0), (1, false));
assert_eq!(3i8.overflowing_pow(5), (-13, true));
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Raises self to the power of `exp`, using exponentiation by squaring.

##### [§](#examples-100)Examples

```rust
let x: isize = 2; // or any other integer type

assert_eq!(x.pow(5), 32);
assert_eq!(0_isize.pow(0), 1);
```

1.84.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the square root of the number, rounded down.

##### [§](#panics-24)Panics

This function will panic if `self` is negative.

##### [§](#examples-101)Examples

```rust
assert_eq!(10isize.isqrt(), 3);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates the quotient of Euclidean division of `self` by `rhs`.

This computes the integer `q` such that `self = q * rhs + r`, with `r = self.rem_euclid(rhs)` and `0 <= r < abs(rhs)`.

In other words, the result is `self / rhs` rounded to the integer `q` such that `self >= q * rhs`. If `self > 0`, this is equal to rounding towards zero (the default in Rust); if `self < 0`, this is equal to rounding away from zero (towards +/- infinity). If `rhs > 0`, this is equal to rounding towards -infinity; if `rhs < 0`, this is equal to rounding towards +infinity.

##### [§](#panics-25)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-102)Examples

```rust
let a: isize = 7; // or any other integer type
let b = 4;

assert_eq!(a.div_euclid(b), 1); // 7 >= 4 * 1
assert_eq!(a.div_euclid(-b), -1); // 7 >= -4 * -1
assert_eq!((-a).div_euclid(b), -2); // -7 >= 4 * -2
assert_eq!((-a).div_euclid(-b), 2); // -7 >= -4 * 2
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Calculates the least nonnegative remainder of `self` when divided by `rhs`.

This is done as if by the Euclidean division algorithm – given `r = self.rem_euclid(rhs)`, the result satisfies `self = rhs * self.div_euclid(rhs) + r` and `0 <= r < abs(rhs)`.

##### [§](#panics-26)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-103)Examples

```rust
let a: isize = 7; // or any other integer type
let b = 4;

assert_eq!(a.rem_euclid(b), 3);
assert_eq!((-a).rem_euclid(b), 1);
assert_eq!(a.rem_euclid(-b), 3);
assert_eq!((-a).rem_euclid(-b), 1);
```

This will panic:

[ⓘ](# "This example panics")

```rust
let _ = isize::MIN.rem_euclid(-1);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Available on **64-bit** only.

Calculates the quotient of `self` and `rhs`, rounding the result towards negative infinity.

##### [§](#panics-27)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-104)Examples

```rust
#![feature(int_roundings)]
let a: isize = 8;
let b = 3;

assert_eq!(a.div_floor(b), 2);
assert_eq!(a.div_floor(-b), -3);
assert_eq!((-a).div_floor(b), -3);
assert_eq!((-a).div_floor(-b), 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Available on **64-bit** only.

Calculates the quotient of `self` and `rhs`, rounding the result towards positive infinity.

##### [§](#panics-28)Panics

This function will panic if `rhs` is zero or if `self` is `Self::MIN` and `rhs` is -1. This behavior is not affected by the `overflow-checks` flag.

##### [§](#examples-105)Examples

```rust
#![feature(int_roundings)]
let a: isize = 8;
let b = 3;

assert_eq!(a.div_ceil(b), 3);
assert_eq!(a.div_ceil(-b), -2);
assert_eq!((-a).div_ceil(b), -2);
assert_eq!((-a).div_ceil(-b), 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Available on **64-bit** only.

If `rhs` is positive, calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`. If `rhs` is negative, calculates the largest value less than or equal to `self` that is a multiple of `rhs`.

##### [§](#panics-29)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-15)Overflow behavior

On overflow, this function will panic if overflow checks are enabled (default in debug mode) and wrap if overflow checks are disabled (default in release mode).

##### [§](#examples-106)Examples

```rust
#![feature(int_roundings)]
assert_eq!(16_isize.next_multiple_of(8), 16);
assert_eq!(23_isize.next_multiple_of(8), 24);
assert_eq!(16_isize.next_multiple_of(-8), 16);
assert_eq!(23_isize.next_multiple_of(-8), 16);
assert_eq!((-16_isize).next_multiple_of(8), -16);
assert_eq!((-23_isize).next_multiple_of(8), -16);
assert_eq!((-16_isize).next_multiple_of(-8), -16);
assert_eq!((-23_isize).next_multiple_of(-8), -24);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Available on **64-bit** only.

If `rhs` is positive, calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`. If `rhs` is negative, calculates the largest value less than or equal to `self` that is a multiple of `rhs`. Returns `None` if `rhs` is zero or the operation would result in overflow.

##### [§](#examples-107)Examples

```rust
#![feature(int_roundings)]
assert_eq!(16_isize.checked_next_multiple_of(8), Some(16));
assert_eq!(23_isize.checked_next_multiple_of(8), Some(24));
assert_eq!(16_isize.checked_next_multiple_of(-8), Some(16));
assert_eq!(23_isize.checked_next_multiple_of(-8), Some(16));
assert_eq!((-16_isize).checked_next_multiple_of(8), Some(-16));
assert_eq!((-23_isize).checked_next_multiple_of(8), Some(-16));
assert_eq!((-16_isize).checked_next_multiple_of(-8), Some(-16));
assert_eq!((-23_isize).checked_next_multiple_of(-8), Some(-24));
assert_eq!(1_isize.checked_next_multiple_of(0), None);
assert_eq!(isize::MAX.checked_next_multiple_of(2), None);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

This method might not be optimized owing to implementation details; `ilog2` can produce results more efficiently for base 2, and `ilog10` can produce results more efficiently for base 10.

##### [§](#panics-30)Panics

This function will panic if `self` is less than or equal to zero, or if `base` is less than 2.

##### [§](#examples-108)Examples

```rust
assert_eq!(5isize.ilog(5), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the base 2 logarithm of the number, rounded down.

##### [§](#panics-31)Panics

This function will panic if `self` is less than or equal to zero.

##### [§](#examples-109)Examples

```rust
assert_eq!(2isize.ilog2(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the base 10 logarithm of the number, rounded down.

##### [§](#panics-32)Panics

This function will panic if `self` is less than or equal to zero.

##### [§](#example)Example

```rust
assert_eq!(10isize.ilog10(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

Returns `None` if the number is negative or zero, or if the base is not at least 2.

This method might not be optimized owing to implementation details; `checked_ilog2` can produce results more efficiently for base 2, and `checked_ilog10` can produce results more efficiently for base 10.

##### [§](#examples-110)Examples

```rust
assert_eq!(5isize.checked_ilog(5), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the base 2 logarithm of the number, rounded down.

Returns `None` if the number is negative or zero.

##### [§](#examples-111)Examples

```rust
assert_eq!(2isize.checked_ilog2(), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the base 10 logarithm of the number, rounded down.

Returns `None` if the number is negative or zero.

##### [§](#example-1)Example

```rust
assert_eq!(10isize.checked_ilog10(), Some(1));
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Computes the absolute value of `self`.

##### [§](#overflow-behavior-16)Overflow behavior

The absolute value of `isize::MIN` cannot be represented as an `isize`, and attempting to calculate it will cause an overflow. This means that code in debug mode will trigger a panic on this case and optimized code will return `isize::MIN` without a panic. If you do not want this behavior, consider using [`unsigned_abs`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.unsigned_abs "method isize::unsigned_abs") instead.

##### [§](#examples-112)Examples

```rust
assert_eq!(10isize.abs(), 10);
assert_eq!((-10isize).abs(), 10);
```

1.60.0 (const: 1.60.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Computes the absolute difference between `self` and `other`.

This function always returns the correct answer without overflow or panics by returning an unsigned integer.

##### [§](#examples-113)Examples

```rust
assert_eq!(100isize.abs_diff(80), 20usize);
assert_eq!(100isize.abs_diff(110), 10usize);
assert_eq!((-100isize).abs_diff(80), 180usize);
assert_eq!((-100isize).abs_diff(-120), 20usize);
assert_eq!(isize::MIN.abs_diff(isize::MAX), usize::MAX);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns a number representing sign of `self`.

- `0` if the number is zero
- `1` if the number is positive
- `-1` if the number is negative

##### [§](#examples-114)Examples

```rust
assert_eq!(10isize.signum(), 1);
assert_eq!(0isize.signum(), 0);
assert_eq!((-10isize).signum(), -1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns `true` if `self` is positive and `false` if the number is zero or negative.

##### [§](#examples-115)Examples

```rust
assert!(10isize.is_positive());
assert!(!(-10isize).is_positive());
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns `true` if `self` is negative and `false` if the number is zero or positive.

##### [§](#examples-116)Examples

```rust
assert!((-10isize).is_negative());
assert!(!10isize.is_negative());
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the memory representation of this integer as a byte array in big-endian (network) byte order.

**Note**: This function returns an array of length 2, 4 or 8 bytes depending on the target pointer size.

##### [§](#examples-117)Examples

```rust
let bytes = 0x1234567890123456isize.to_be_bytes();
assert_eq!(bytes, [0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the memory representation of this integer as a byte array in little-endian byte order.

**Note**: This function returns an array of length 2, 4 or 8 bytes depending on the target pointer size.

##### [§](#examples-118)Examples

```rust
let bytes = 0x1234567890123456isize.to_le_bytes();
assert_eq!(bytes, [0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Returns the memory representation of this integer as a byte array in native byte order.

As the target platform’s native endianness is used, portable code should use [`to_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.to_be_bytes "method isize::to_be_bytes") or [`to_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.to_le_bytes "method isize::to_le_bytes"), as appropriate, instead.

**Note**: This function returns an array of length 2, 4 or 8 bytes depending on the target pointer size.

##### [§](#examples-119)Examples

```rust
let bytes = 0x1234567890123456isize.to_ne_bytes();
assert_eq!(
    bytes,
    if cfg!(target_endian = "big") {
        [0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]
    } else {
        [0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]
    }
);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Creates an integer value from its representation as a byte array in big endian.

**Note**: This function takes an array of length 2, 4 or 8 bytes depending on the target pointer size.

##### [§](#examples-120)Examples

```rust
let value = isize::from_be_bytes([0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]);
assert_eq!(value, 0x1234567890123456);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_be_isize(input: &mut &[u8]) -> isize {
    let (int_bytes, rest) = input.split_at(size_of::<isize>());
    *input = rest;
    isize::from_be_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Creates an integer value from its representation as a byte array in little endian.

**Note**: This function takes an array of length 2, 4 or 8 bytes depending on the target pointer size.

##### [§](#examples-121)Examples

```rust
let value = isize::from_le_bytes([0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]);
assert_eq!(value, 0x1234567890123456);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_le_isize(input: &mut &[u8]) -> isize {
    let (int_bytes, rest) = input.split_at(size_of::<isize>());
    *input = rest;
    isize::from_le_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

Available on **64-bit** only.

Creates an integer value from its memory representation as a byte array in native endianness.

As the target platform’s native endianness is used, portable code likely wants to use [`from_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.from_be_bytes "associated function isize::from_be_bytes") or [`from_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.from_le_bytes "associated function isize::from_le_bytes"), as appropriate instead.

**Note**: This function takes an array of length 2, 4 or 8 bytes depending on the target pointer size.

##### [§](#examples-122)Examples

```rust
let value = isize::from_ne_bytes(if cfg!(target_endian = "big") {
    [0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]
} else {
    [0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]
});
assert_eq!(value, 0x1234567890123456);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_ne_isize(input: &mut &[u8]) -> isize {
    let (int_bytes, rest) = input.split_at(size_of::<isize>());
    *input = rest;
    isize::from_ne_bytes(int_bytes.try_into().unwrap())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

👎Deprecating in a future version: replaced by the `MIN` associated constant on this type

Available on **64-bit** only.

New code should prefer to use [`isize::MIN`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MIN "associated constant isize::MIN") instead.

Returns the smallest value that can be represented by this integer type.

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

👎Deprecating in a future version: replaced by the `MAX` associated constant on this type

Available on **64-bit** only.

New code should prefer to use [`isize::MAX`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX") instead.

Returns the largest value that can be represented by this integer type.

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#519-538)

🔬This is a nightly-only experimental API. (`clamp_magnitude` [#148519](https://github.com/rust-lang/rust/issues/148519))

Available on **64-bit** only.

Clamps this number to a symmetric range centred around zero.

The method clamps the number’s magnitude (absolute value) to be at most `limit`.

This is functionally equivalent to `self.clamp(-limit, limit)`, but is more explicit about the intent.

##### [§](#examples-123)Examples

```rust
#![feature(clamp_magnitude)]
assert_eq!(120isize.clamp_magnitude(100), 100);
assert_eq!(-120isize.clamp_magnitude(100), -100);
assert_eq!(80isize.clamp_magnitude(100), 80);
assert_eq!(-80isize.clamp_magnitude(100), -80);
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#539)

Available on **64-bit** only.

Calculates the midpoint (average) between `self` and `rhs`.

`midpoint(a, b)` is `(a + b) / 2` as if it were performed in a sufficiently-large signed integral type. This implies that the result is always rounded towards zero and that no overflow will ever occur.

##### [§](#examples-124)Examples

```rust
assert_eq!(0isize.midpoint(4), 2);
assert_eq!((-1isize).midpoint(2), 0);
assert_eq!((-7isize).midpoint(0), -3);
assert_eq!(0isize.midpoint(-7), -3);
assert_eq!(0isize.midpoint(7), 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#impl-isize-1)

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
assert_eq!(isize::from_str_radix("A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(isize::from_str_radix("1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with decimal digits.

The characters are expected to be an optional `+` or `-` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#examples-126)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(isize::from_ascii(b"+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(isize::from_ascii(b"1 ").is_err());
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

assert_eq!(isize::from_ascii_radix(b"A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(isize::from_ascii_radix(b"1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)[§](#impl-isize-2)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Allows users to write an integer (in signed decimal format) into a variable `buf` of type [`NumBuffer`](https://doc.rust-lang.org/stable/core/fmt/num_buffer/struct.NumBuffer.html "struct core::fmt::num_buffer::NumBuffer") that is passed by the caller by mutable reference.

##### [§](#examples-128)Examples

```rust
#![feature(int_format_into)]
use core::fmt::NumBuffer;

let n = 0isize;
let mut buf = NumBuffer::new();
assert_eq!(n.format_into(&mut buf), "0");

let n1 = 32isize;
assert_eq!(n1.format_into(&mut buf), "32");

let n2 = isize :: MAX;
assert_eq!(n2.format_into(&mut buf), isize :: MAX.to_string());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-17)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-16)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-15)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-14)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#314)[§](#impl-AtomicPrimitive-for-isize)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#314)[§](#associatedtype.AtomicInner)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#impl-Binary-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#method.fmt-2)

Format signed integers in the two’s-complement form.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-35)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-34)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-33)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-32)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-3)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-2)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-1)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-31)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-30)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-29)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-28)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#impl-CarryingMulAdd-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#associatedtype.Unsigned)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#method.carrying_mul_add-1)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-isize)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#589-592)[§](#impl-Debug-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#176)[§](#impl-Default-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#176)[§](#method.default)

Returns the default value of `0`

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#impl-DisjointBitOr-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#method.disjoint_bitor)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::disjoint_bitor`](https://doc.rust-lang.org/stable/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)[§](#impl-Display-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#60)[§](#impl-Distribution%3Cisize%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#60)[§](#method.sample)

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Samples a random value from the distribution, using the specified random source.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-7)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-6)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-5)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-isize)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-35)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-4)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign-for-isize)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`isize`](https://doc.rust-lang.org/stable/std/primitive.isize.html "primitive isize") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-130)Examples

```rust
assert_eq!(isize::from(false), 0);

assert_eq!(isize::from(true), 1);
```

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#131)[§](#impl-From%3Ci16%3E-for-isize)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#106)[§](#impl-From%3Ci8%3E-for-isize)

1.23.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3851-3855)[§](#impl-From%3Cisize%3E-for-AtomicIsize)

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3851-3855)[§](#method.from-4)

Converts an `isize` into an `AtomicIsize`.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#130)[§](#impl-From%3Cu8%3E-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#impl-FromStr-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#method.from_str)

Parses an integer from a string slice with decimal digits.

The characters are expected to be an optional `+` or `-` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#see-also-1)See also

For parsing numbers in other bases, such as binary or hexadecimal, see [`from_str_radix`](https://doc.rust-lang.org/stable/std/primitive.isize.html#method.from_str_radix "associated function isize::from_str_radix").

##### [§](#examples-129)Examples

```rust
use std::str::FromStr;

assert_eq!(isize::from_str("+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(isize::from_str("1 ").is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1801)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-isize)

1.42.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#600)[§](#impl-LowerExp-for-isize)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#impl-LowerHex-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#method.fmt-4)

Format signed integers in the two’s-complement form.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-25)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-24)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-23)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-22)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-%26isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-%26isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num_buffer.rs.html#26-33)[§](#impl-NumBufferTrait-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num_buffer.rs.html#26-33)[§](#associatedconstant.BUF_SIZE)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Maximum number of digits in decimal base of the implemented integer.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#impl-Octal-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#method.fmt-3)

Format signed integers in the two’s-complement form.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#impl-Ord-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#impl-PartialOrd-for-isize)

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

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.product-1)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.product)

Takes an iterator and generates `Self` from the elements by multiplying the items.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#impl-RangePattern-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#associatedconstant.MIN-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#associatedconstant.MAX-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#method.sub_one)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

A compile-time helper to subtract 1 for exclusive ranges.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-11)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-10)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-9)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem-for-isize)

This operation satisfies `n % d == n - (n / d) * d`. The result has the same sign as the left operand.

#### [§](#panics-36)Panics

This operation will panic if `other == 0` or if `self / other` results in overflow.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-8)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-123)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-122)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-111)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-110)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-115)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-114)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-119)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-118)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-107)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-106)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-70)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26isize%3E-for-%26Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-131)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-79)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-67)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-71)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-75)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-63)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-127)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-55)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-43)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-47)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-51)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-39)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-59)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-23)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26isize%3E-for-Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-129)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-78)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-66)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-70)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-74)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-62)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-126)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-54)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-42)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-46)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-50)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-38)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-58)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-22)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-99)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-98)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-87)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-86)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-91)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-90)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-95)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-94)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-83)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-82)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-103)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-67)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-102)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-121)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-120)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-109)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-108)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-113)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-112)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-117)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-116)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-105)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-104)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-68)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Cisize%3E-for-%26Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-130)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-77)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-65)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-69)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-73)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-61)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-125)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-53)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-41)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-45)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-49)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-37)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-57)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-21)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Cisize%3E-for-Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-128)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-76)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-64)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-68)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-72)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-60)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-52)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-40)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-44)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-48)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-36)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-56)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-20)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-97)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-96)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-85)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-84)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-89)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-88)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-93)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-92)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-81)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-80)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-101)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-65)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-100)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-124)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-88)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i128%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i32%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i64%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i8%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u128%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u32%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u64%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26usize%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci128%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci32%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci64%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci8%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu128%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu32%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu64%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cusize%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-219)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-218)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-207)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-206)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-211)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-210)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-215)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-214)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-203)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-202)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-70)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26isize%3E-for-%26Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-227)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-175)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-163)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-167)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-171)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-159)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-223)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-151)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-139)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-143)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-147)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-135)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-155)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-23)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26isize%3E-for-Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-225)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-174)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-162)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-166)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-170)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-158)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-222)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-150)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-138)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-142)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-146)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-134)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-154)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-22)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-195)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-194)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-183)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-182)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-187)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-186)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-191)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-190)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-179)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-178)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-199)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-67)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-198)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-217)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-216)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-205)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-204)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-209)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-208)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-213)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-212)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-201)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-200)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-68)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Cisize%3E-for-%26Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-226)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-173)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-161)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-165)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-169)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-157)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-221)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-149)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-137)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-141)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-145)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-133)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-153)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-21)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Cisize%3E-for-Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-224)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-172)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-160)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-164)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-168)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-156)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-148)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-136)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-140)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-144)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-132)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-152)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-20)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-193)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-192)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-181)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-180)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-185)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-184)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-189)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-188)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-177)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-176)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-197)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-65)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-196)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-220)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-88)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i128%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i32%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i64%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i8%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u128%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u32%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u64%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26usize%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci128%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci32%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci64%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci8%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu128%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu32%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu64%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cusize%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1146)[§](#impl-SimdElement-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1147)[§](#associatedtype.Mask)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#impl-Step-for-isize)

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

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-21)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-20)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-19)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-18)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3C%26isize%3E-for-Saturating%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3C%26isize%3E-for-Wrapping%3Cisize%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign%3C%26isize%3E-for-isize)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3Cisize%3E-for-Saturating%3Cisize%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3Cisize%3E-for-Wrapping%3Cisize%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign-for-isize)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.sum-1)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.sum)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#477)[§](#impl-TryFrom%3Ci128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#477)[§](#method.try_from-18)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#477)[§](#associatedtype.Error-18)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#476)[§](#impl-TryFrom%3Ci32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#476)[§](#method.try_from-16)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#476)[§](#associatedtype.Error-16)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#476)[§](#impl-TryFrom%3Ci64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#476)[§](#method.try_from-17)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#476)[§](#associatedtype.Error-17)

The type returned in the event of a conversion error.

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#573)[§](#impl-TryFrom%3Cisize%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#573)[§](#method.try_from-19)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#573)[§](#associatedtype.Error-19)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#467)[§](#impl-TryFrom%3Cisize%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#467)[§](#method.try_from-11)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#467)[§](#associatedtype.Error-11)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#method.try_from-8)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-8)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#method.try_from-9)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-9)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#467)[§](#impl-TryFrom%3Cisize%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#467)[§](#method.try_from-10)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#467)[§](#associatedtype.Error-10)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#method.try_from-7)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-7)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#465)[§](#impl-TryFrom%3Cisize%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#465)[§](#method.try_from-6)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#465)[§](#associatedtype.Error-6)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#method.try_from-3)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#method.try_from-4)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#465)[§](#impl-TryFrom%3Cisize%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#465)[§](#method.try_from-5)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#465)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#method.try_from-2)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#406)[§](#impl-TryFrom%3Cisize%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#406)[§](#method.try_from-1)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#406)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#475)[§](#impl-TryFrom%3Cu128%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#475)[§](#method.try_from-15)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#475)[§](#associatedtype.Error-15)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#impl-TryFrom%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#method.try_from-12)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#associatedtype.Error-12)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#impl-TryFrom%3Cu32%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#method.try_from-13)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#associatedtype.Error-13)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#475)[§](#impl-TryFrom%3Cu64%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#475)[§](#method.try_from-14)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#475)[§](#associatedtype.Error-14)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#405)[§](#impl-TryFrom%3Cusize%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#405)[§](#method.try_from)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#405)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.42.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#600)[§](#impl-UpperExp-for-isize)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#impl-UpperHex-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#72)[§](#method.fmt-5)

Format signed integers in the two’s-complement form.

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#69-83)[§](#impl-ZeroablePrimitive-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#69-83)[§](#associatedtype.NonZeroInner)

🔬This is a nightly-only experimental API. (`nonzero_internals`)

A type like `Self` but with a niche that includes zero.

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-isize)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-isize)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#40)[§](#impl-FloatToInt%3Cisize%3E-for-f128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cisize%3E-for-f16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cisize%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#39)[§](#impl-FloatToInt%3Cisize%3E-for-f64)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#112)[§](#impl-MaskElement-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/cast.rs.html#30)[§](#impl-SimdCast-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#17)[§](#impl-TrustedStep-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ffi/va_list.rs.html#304)[§](#impl-VaArgSafe-for-isize)

[§](#impl-Freeze-for-isize)

[§](#impl-RefUnwindSafe-for-isize)

[§](#impl-Send-for-isize)

[§](#impl-Sync-for-isize)

[§](#impl-Unpin-for-isize)

[§](#impl-UnsafeUnpin-for-isize)

[§](#impl-UnwindSafe-for-isize)