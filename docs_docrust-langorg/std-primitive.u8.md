---
title: u8 - Rust
url: https://doc.rust-lang.org/std/primitive.u8.html
source: crawler
fetched_at: 2026-05-06T21:22:10.451786-03:00
rendered_js: false
word_count: 13709
summary: This document provides a reference for the 8-bit unsigned integer type (u8) in Rust, detailing methods for bit manipulation, bitwise rotations, and arithmetic properties.
tags:
    - rust
    - primitive-types
    - u8
    - bit-manipulation
    - binary-operations
category: reference
---

Expand description

The 8-bit unsigned integer type.

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#545)[§](#impl-u8)

1.43.0 · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

The smallest value that can be represented by this integer type.

##### [§](#examples)Examples

1.43.0 · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

The largest value that can be represented by this integer type (28 − 1).

##### [§](#examples-1)Examples

```rust
assert_eq!(u8::MAX, 255);
```

1.53.0 · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

The size of this integer type in bits.

##### [§](#examples-2)Examples

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the number of ones in the binary representation of `self`.

##### [§](#examples-3)Examples

```rust
let n = 0b01001100u8;
assert_eq!(n.count_ones(), 3);

let max = u8::MAX;
assert_eq!(max.count_ones(), 8);

let zero = 0u8;
assert_eq!(zero.count_ones(), 0);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the number of zeros in the binary representation of `self`.

##### [§](#examples-4)Examples

```rust
let zero = 0u8;
assert_eq!(zero.count_zeros(), 8);

let max = u8::MAX;
assert_eq!(max.count_zeros(), 0);
```

This is heavily dependent on the width of the type, and thus might give surprising results depending on type inference:

```rust
let lucky = 7;
foo(lucky);
assert_eq!(lucky.count_zeros(), 5);
assert_eq!(lucky.count_ones(), 3);

let lucky = 7;
bar(lucky);
assert_eq!(lucky.count_zeros(), 13);
assert_eq!(lucky.count_ones(), 3);
```

You might want to use [`Self::count_ones`](https://doc.rust-lang.org/std/primitive.u8.html#method.count_ones "method u8::count_ones") instead, or emphasize the type you’re using in the call rather than method syntax:

```rust
let small = 1;
assert_eq!(u8::count_zeros(small), 7);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the number of leading zeros in the binary representation of `self`.

Depending on what you’re doing with the value, you might also be interested in the [`ilog2`](https://doc.rust-lang.org/std/primitive.u8.html#method.ilog2 "method u8::ilog2") function which returns a consistent number, even if the type widens.

##### [§](#examples-5)Examples

```rust
let n = u8::MAX >> 2;
assert_eq!(n.leading_zeros(), 2);

let zero = 0u8;
assert_eq!(zero.leading_zeros(), 8);

let max = u8::MAX;
assert_eq!(max.leading_zeros(), 0);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the number of trailing zeros in the binary representation of `self`.

##### [§](#examples-6)Examples

```rust
let n = 0b0101000u8;
assert_eq!(n.trailing_zeros(), 3);

let zero = 0u8;
assert_eq!(zero.trailing_zeros(), 8);

let max = u8::MAX;
assert_eq!(max.trailing_zeros(), 0);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the number of leading ones in the binary representation of `self`.

##### [§](#examples-7)Examples

```rust
let n = !(u8::MAX >> 2);
assert_eq!(n.leading_ones(), 2);

let zero = 0u8;
assert_eq!(zero.leading_ones(), 0);

let max = u8::MAX;
assert_eq!(max.leading_ones(), 8);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the number of trailing ones in the binary representation of `self`.

##### [§](#examples-8)Examples

```rust
let n = 0b1010111u8;
assert_eq!(n.trailing_ones(), 3);

let zero = 0u8;
assert_eq!(zero.trailing_ones(), 0);

let max = u8::MAX;
assert_eq!(max.trailing_ones(), 8);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`uint_bit_width` [#142326](https://github.com/rust-lang/rust/issues/142326))

Returns the minimum number of bits required to represent `self`.

This method returns zero if `self` is zero.

##### [§](#examples-9)Examples

```rust
#![feature(uint_bit_width)]

assert_eq!(0_u8.bit_width(), 0);
assert_eq!(0b111_u8.bit_width(), 3);
assert_eq!(0b1110_u8.bit_width(), 4);
assert_eq!(u8::MAX.bit_width(), 8);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Returns `self` with only the most significant bit set, or `0` if the input is `0`.

##### [§](#examples-10)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: u8 = 0b_01100100;

assert_eq!(n.isolate_highest_one(), 0b_01000000);
assert_eq!(0_u8.isolate_highest_one(), 0);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Returns `self` with only the least significant bit set, or `0` if the input is `0`.

##### [§](#examples-11)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: u8 = 0b_01100100;

assert_eq!(n.isolate_lowest_one(), 0b_00000100);
assert_eq!(0_u8.isolate_lowest_one(), 0);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Returns the index of the highest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-12)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_u8.highest_one(), None);
assert_eq!(0b1_u8.highest_one(), Some(0));
assert_eq!(0b1_0000_u8.highest_one(), Some(4));
assert_eq!(0b1_1111_u8.highest_one(), Some(4));
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Returns the index of the lowest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-13)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_u8.lowest_one(), None);
assert_eq!(0b1_u8.lowest_one(), Some(0));
assert_eq!(0b1_0000_u8.lowest_one(), Some(4));
assert_eq!(0b1_1111_u8.lowest_one(), Some(0));
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the bit pattern of `self` reinterpreted as a signed integer of the same size.

This produces the same result as an `as` cast, but ensures that the bit-width remains the same.

##### [§](#examples-14)Examples

```rust
let n = u8::MAX;

assert_eq!(n.cast_signed(), -1i8);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Shifts the bits to the left by a specified amount, `n`, wrapping the truncated bits to the end of the resulting integer.

`rotate_left(n)` is equivalent to applying `rotate_left(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `<<` shifting operator!

##### [§](#examples-15)Examples

```rust
let n = 0x82u8;
let m = 0xa;

assert_eq!(n.rotate_left(2), m);
assert_eq!(n.rotate_left(1024), n);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Shifts the bits to the right by a specified amount, `n`, wrapping the truncated bits to the beginning of the resulting integer.

`rotate_right(n)` is equivalent to applying `rotate_right(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `>>` shifting operator!

##### [§](#examples-16)Examples

```rust
let n = 0xau8;
let m = 0x82;

assert_eq!(n.rotate_right(2), m);
assert_eq!(n.rotate_right(1024), n);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`funnel_shifts` [#145686](https://github.com/rust-lang/rust/issues/145686))

Performs a left funnel shift (concatenates `self` with `rhs`, with `self` making up the most significant half, then shifts the combined value left by `n`, and most significant half is extracted to produce the result).

Please note this isn’t the same operation as the `<<` shifting operator or [`rotate_left`](https://doc.rust-lang.org/std/primitive.u8.html#method.rotate_left "method u8::rotate_left"), although `a.funnel_shl(a, n)` is *equivalent* to `a.rotate_left(n)`.

##### [§](#panics)Panics

If `n` is greater than or equal to the number of bits in `self`

##### [§](#examples-17)Examples

Basic usage:

```rust
#![feature(funnel_shifts)]
let a = 0x82u8;
let b = 0x36u8;
let m = 0x8;

assert_eq!(a.funnel_shl(b, 2), m);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`funnel_shifts` [#145686](https://github.com/rust-lang/rust/issues/145686))

Performs a right funnel shift (concatenates `self` and `rhs`, with `self` making up the most significant half, then shifts the combined value right by `n`, and least significant half is extracted to produce the result).

Please note this isn’t the same operation as the `>>` shifting operator or [`rotate_right`](https://doc.rust-lang.org/std/primitive.u8.html#method.rotate_right "method u8::rotate_right"), although `a.funnel_shr(a, n)` is *equivalent* to `a.rotate_right(n)`.

##### [§](#panics-1)Panics

If `n` is greater than or equal to the number of bits in `self`

##### [§](#examples-18)Examples

Basic usage:

```rust
#![feature(funnel_shifts)]
let a = 0x82u8;
let b = 0x36u8;
let m = 0x8d;

assert_eq!(a.funnel_shr(b, 2), m);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`uint_carryless_mul` [#152080](https://github.com/rust-lang/rust/issues/152080))

Performs a carry-less multiplication, returning the lower bits.

This operation is similar to long multiplication in base 2, except that exclusive or is used instead of addition. The implementation is equivalent to:

```rust
pub fn carryless_mul(lhs: u8, rhs: u8) -> u8{
    let mut retval = 0;
    for i in 0..u8::BITS {
        if (rhs >> i) & 1 != 0 {
            // long multiplication would use +=
            retval ^= lhs << i;
        }
    }
    retval
}
```

The actual implementation is more efficient, and on some platforms lowers directly to a dedicated instruction.

##### [§](#uses)Uses

Carryless multiplication can be used to turn a bitmask of quote characters into a bit mask of characters surrounded by quotes:

```rust
r#"abc xxx "foobar" zzz "a"!"#; // input string
 0b0000000010000001000001010; // quote_mask
 0b0000000001111110000000100; // quote_mask.carryless_mul(!0) & !quote_mask
```

Another use is in cryptography, where carryless multiplication allows for efficient implementations of polynomial multiplication in `GF(2)[X]`, the polynomial ring over `GF(2)`.

##### [§](#examples-19)Examples

```rust
#![feature(uint_carryless_mul)]

let a = 0x12u8;
let b = 0x34u8;

assert_eq!(a.carryless_mul(b), 0x28);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Reverses the byte order of the integer.

##### [§](#examples-20)Examples

```rust
let n = 0x12u8;
let m = n.swap_bytes();

assert_eq!(m, 0x12);
```

🔬This is a nightly-only experimental API. (`uint_gather_scatter_bits` [#149069](https://github.com/rust-lang/rust/issues/149069))

Returns an integer with the bit locations specified by `mask` packed contiguously into the least significant bits of the result.

```rust
#![feature(uint_gather_scatter_bits)]
let n: u8 = 0b1011_1100;

assert_eq!(n.extract_bits(0b0010_0100), 0b0000_0011);
assert_eq!(n.extract_bits(0xF0), 0b0000_1011);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`uint_gather_scatter_bits` [#149069](https://github.com/rust-lang/rust/issues/149069))

Returns an integer with the least significant bits of `self` distributed to the bit locations specified by `mask`.

```rust
#![feature(uint_gather_scatter_bits)]
let n: u8 = 0b1010_1101;

assert_eq!(n.deposit_bits(0b0101_0101), 0b0101_0001);
assert_eq!(n.deposit_bits(0xF0), 0b1101_0000);
```

1.37.0 (const: 1.37.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Reverses the order of bits in the integer. The least significant bit becomes the most significant bit, second least-significant bit becomes second most-significant bit, etc.

##### [§](#examples-21)Examples

```rust
let n = 0x12u8;
let m = n.reverse_bits();

assert_eq!(m, 0x48);
assert_eq!(0, 0u8.reverse_bits());
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Converts an integer from big endian to the target’s endianness.

On big endian this is a no-op. On little endian the bytes are swapped.

##### [§](#examples-22)Examples

```rust
let n = 0x1Au8;

if cfg!(target_endian = "big") {
    assert_eq!(u8::from_be(n), n)
} else {
    assert_eq!(u8::from_be(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Converts an integer from little endian to the target’s endianness.

On little endian this is a no-op. On big endian the bytes are swapped.

##### [§](#examples-23)Examples

```rust
let n = 0x1Au8;

if cfg!(target_endian = "little") {
    assert_eq!(u8::from_le(n), n)
} else {
    assert_eq!(u8::from_le(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Converts `self` to big endian from the target’s endianness.

On big endian this is a no-op. On little endian the bytes are swapped.

##### [§](#examples-24)Examples

```rust
let n = 0x1Au8;

if cfg!(target_endian = "big") {
    assert_eq!(n.to_be(), n)
} else {
    assert_eq!(n.to_be(), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Converts `self` to little endian from the target’s endianness.

On little endian this is a no-op. On big endian the bytes are swapped.

##### [§](#examples-25)Examples

```rust
let n = 0x1Au8;

if cfg!(target_endian = "little") {
    assert_eq!(n.to_le(), n)
} else {
    assert_eq!(n.to_le(), n.swap_bytes())
}
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked integer addition. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-26)Examples

```rust
assert_eq!((u8::MAX - 2).checked_add(1), Some(u8::MAX - 1));
assert_eq!((u8::MAX - 2).checked_add(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict integer addition. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics-2)Panics

###### [§](#overflow-behavior)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-27)Examples

```rust
assert_eq!((u8::MAX - 2).strict_add(1), u8::MAX - 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (u8::MAX - 2).strict_add(3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unchecked integer addition. Computes `self + rhs`, assuming overflow cannot occur.

Calling `x.unchecked_add(y)` is semantically equivalent to calling `x.`[`checked_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_add "method u8::checked_add")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.wrapping_add "method u8::wrapping_add").

##### [§](#safety)Safety

This results in undefined behavior when `self + rhs > u8::MAX` or `self + rhs < u8::MIN`, i.e. when [`checked_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_add "method u8::checked_add") would return `None`.

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked addition with a signed integer. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-28)Examples

```rust
assert_eq!(1u8.checked_add_signed(2), Some(3));
assert_eq!(1u8.checked_add_signed(-2), None);
assert_eq!((u8::MAX - 2).checked_add_signed(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict addition with a signed integer. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics-3)Panics

###### [§](#overflow-behavior-1)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-29)Examples

```rust
assert_eq!(1u8.strict_add_signed(2), 3);
```

The following panic because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 1u8.strict_add_signed(-2);
```

[ⓘ](# "This example panics")

```rust
let _ = (u8::MAX - 2).strict_add_signed(3);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked integer subtraction. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-30)Examples

```rust
assert_eq!(1u8.checked_sub(1), Some(0));
assert_eq!(0u8.checked_sub(1), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict integer subtraction. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-4)Panics

###### [§](#overflow-behavior-2)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-31)Examples

```rust
assert_eq!(1u8.strict_sub(1), 0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0u8.strict_sub(1);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unchecked integer subtraction. Computes `self - rhs`, assuming overflow cannot occur.

Calling `x.unchecked_sub(y)` is semantically equivalent to calling `x.`[`checked_sub`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_sub "method u8::checked_sub")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_sub`](https://doc.rust-lang.org/std/primitive.u8.html#method.wrapping_sub "method u8::wrapping_sub").

If you find yourself writing code like this:

```rust
if foo >= bar {
    // SAFETY: just checked it will not overflow
    let diff = unsafe { foo.unchecked_sub(bar) };
    // ... use diff ...
}
```

Consider changing it to

```rust
if let Some(diff) = foo.checked_sub(bar) {
    // ... use diff ...
}
```

As that does exactly the same thing – including telling the optimizer that the subtraction cannot overflow – but avoids needing `unsafe`.

##### [§](#safety-1)Safety

This results in undefined behavior when `self - rhs > u8::MAX` or `self - rhs < u8::MIN`, i.e. when [`checked_sub`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_sub "method u8::checked_sub") would return `None`.

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked subtraction with a signed integer. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-32)Examples

```rust
assert_eq!(1u8.checked_sub_signed(2), None);
assert_eq!(1u8.checked_sub_signed(-2), Some(3));
assert_eq!((u8::MAX - 2).checked_sub_signed(-4), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict subtraction with a signed integer. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-5)Panics

###### [§](#overflow-behavior-3)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-33)Examples

```rust
assert_eq!(3u8.strict_sub_signed(2), 1);
```

The following panic because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 1u8.strict_sub_signed(2);
```

[ⓘ](# "This example panics")

```rust
let _ = (u8::MAX).strict_sub_signed(-1);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked integer subtraction. Computes `self - rhs` and checks if the result fits into an [`i8`](https://doc.rust-lang.org/std/primitive.i8.html "primitive i8"), returning `None` if overflow occurred.

##### [§](#examples-34)Examples

```rust
assert_eq!(10u8.checked_signed_diff(2), Some(8));
assert_eq!(2u8.checked_signed_diff(10), Some(-8));
assert_eq!(u8::MAX.checked_signed_diff(i8::MAX as u8), None);
assert_eq!((i8::MAX as u8).checked_signed_diff(u8::MAX), Some(i8::MIN));
assert_eq!((i8::MAX as u8 + 1).checked_signed_diff(0), None);
assert_eq!(u8::MAX.checked_signed_diff(u8::MAX), Some(0));
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked integer multiplication. Computes `self * rhs`, returning `None` if overflow occurred.

##### [§](#examples-35)Examples

```rust
assert_eq!(5u8.checked_mul(1), Some(5));
assert_eq!(u8::MAX.checked_mul(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict integer multiplication. Computes `self * rhs`, panicking if overflow occurred.

##### [§](#panics-6)Panics

###### [§](#overflow-behavior-4)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-36)Examples

```rust
assert_eq!(5u8.strict_mul(1), 5);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = u8::MAX.strict_mul(2);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unchecked integer multiplication. Computes `self * rhs`, assuming overflow cannot occur.

Calling `x.unchecked_mul(y)` is semantically equivalent to calling `x.`[`checked_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_mul "method u8::checked_mul")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.wrapping_mul "method u8::wrapping_mul").

##### [§](#safety-2)Safety

This results in undefined behavior when `self * rhs > u8::MAX` or `self * rhs < u8::MIN`, i.e. when [`checked_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_mul "method u8::checked_mul") would return `None`.

1.0.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked integer division. Computes `self / rhs`, returning `None` if `rhs == 0`.

##### [§](#examples-37)Examples

```rust
assert_eq!(128u8.checked_div(2), Some(64));
assert_eq!(1u8.checked_div(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict integer division. Computes `self / rhs`.

Strict division on unsigned types is just normal division. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations.

##### [§](#panics-7)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-38)Examples

```rust
assert_eq!(100u8.strict_div(10), 10);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1u8).strict_div(0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked Euclidean division. Computes `self.div_euclid(rhs)`, returning `None` if `rhs == 0`.

##### [§](#examples-39)Examples

```rust
assert_eq!(128u8.checked_div_euclid(2), Some(64));
assert_eq!(1u8.checked_div_euclid(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict Euclidean division. Computes `self.div_euclid(rhs)`.

Strict division on unsigned types is just normal division. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.strict_div(rhs)`.

##### [§](#panics-8)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-40)Examples

```rust
assert_eq!(100u8.strict_div_euclid(10), 10);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1u8).strict_div_euclid(0);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Checked integer division without remainder. Computes `self / rhs`, returning `None` if `rhs == 0` or if `self % rhs != 0`.

##### [§](#examples-41)Examples

```rust
#![feature(exact_div)]
assert_eq!(64u8.checked_div_exact(2), Some(32));
assert_eq!(64u8.checked_div_exact(32), Some(2));
assert_eq!(64u8.checked_div_exact(0), None);
assert_eq!(65u8.checked_div_exact(2), None);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Integer division without remainder. Computes `self / rhs`, returning `None` if `self % rhs != 0`.

##### [§](#panics-9)Panics

This function will panic if `rhs == 0`.

##### [§](#examples-42)Examples

```rust
#![feature(exact_div)]
assert_eq!(64u8.div_exact(2), Some(32));
assert_eq!(64u8.div_exact(32), Some(2));
assert_eq!(65u8.div_exact(2), None);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Unchecked integer division without remainder. Computes `self / rhs`.

##### [§](#safety-3)Safety

This results in undefined behavior when `rhs == 0` or `self % rhs != 0`, i.e. when [`checked_div_exact`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_div_exact "method u8::checked_div_exact") would return `None`.

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked integer remainder. Computes `self % rhs`, returning `None` if `rhs == 0`.

##### [§](#examples-43)Examples

```rust
assert_eq!(5u8.checked_rem(2), Some(1));
assert_eq!(5u8.checked_rem(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict integer remainder. Computes `self % rhs`.

Strict remainder calculation on unsigned types is just the regular remainder calculation. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations.

##### [§](#panics-10)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-44)Examples

```rust
assert_eq!(100u8.strict_rem(10), 0);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5u8.strict_rem(0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked Euclidean modulo. Computes `self.rem_euclid(rhs)`, returning `None` if `rhs == 0`.

##### [§](#examples-45)Examples

```rust
assert_eq!(5u8.checked_rem_euclid(2), Some(1));
assert_eq!(5u8.checked_rem_euclid(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict Euclidean modulo. Computes `self.rem_euclid(rhs)`.

Strict modulo calculation on unsigned types is just the regular remainder calculation. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.strict_rem(rhs)`.

##### [§](#panics-11)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-46)Examples

```rust
assert_eq!(100u8.strict_rem_euclid(10), 0);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5u8.strict_rem_euclid(0);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`disjoint_bitor` [#135758](https://github.com/rust-lang/rust/issues/135758))

Same value as `self | other`, but UB if any bit position is set in both inputs.

This is a situational micro-optimization for places where you’d rather use addition on some platforms and bitwise or on other platforms, based on exactly which instructions combine better with whatever else you’re doing. Note that there’s no reason to bother using this for places where it’s clear from the operations involved that they can’t overlap. For example, if you’re combining `u16`s into a `u32` with `((a as u32) << 16) | (b as u32)`, that’s fine, as the backend will know those sides of the `|` are disjoint without needing help.

##### [§](#examples-47)Examples

```rust
#![feature(disjoint_bitor)]

// SAFETY: `1` and `4` have no bits in common.
unsafe {
    assert_eq!(1_u8.unchecked_disjoint_bitor(4), 5);
}
```

##### [§](#safety-4)Safety

Requires that `(self & other) == 0`, otherwise it’s immediate UB.

Equivalently, requires that `(self | other) == (self + other)`.

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

This method might not be optimized owing to implementation details; `ilog2` can produce results more efficiently for base 2, and `ilog10` can produce results more efficiently for base 10.

##### [§](#panics-12)Panics

This function will panic if `self` is zero, or if `base` is less than 2.

##### [§](#examples-48)Examples

```rust
assert_eq!(5u8.ilog(5), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the base 2 logarithm of the number, rounded down.

##### [§](#panics-13)Panics

This function will panic if `self` is zero.

##### [§](#examples-49)Examples

```rust
assert_eq!(2u8.ilog2(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the base 10 logarithm of the number, rounded down.

##### [§](#panics-14)Panics

This function will panic if `self` is zero.

##### [§](#example)Example

```rust
assert_eq!(10u8.ilog10(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

Returns `None` if the number is zero, or if the base is not at least 2.

This method might not be optimized owing to implementation details; `checked_ilog2` can produce results more efficiently for base 2, and `checked_ilog10` can produce results more efficiently for base 10.

##### [§](#examples-50)Examples

```rust
assert_eq!(5u8.checked_ilog(5), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the base 2 logarithm of the number, rounded down.

Returns `None` if the number is zero.

##### [§](#examples-51)Examples

```rust
assert_eq!(2u8.checked_ilog2(), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the base 10 logarithm of the number, rounded down.

Returns `None` if the number is zero.

##### [§](#examples-52)Examples

```rust
assert_eq!(10u8.checked_ilog10(), Some(1));
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked negation. Computes `-self`, returning `None` unless `self == 0`.

Note that negating any positive integer will overflow.

##### [§](#examples-53)Examples

```rust
assert_eq!(0u8.checked_neg(), Some(0));
assert_eq!(1u8.checked_neg(), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict negation. Computes `-self`, panicking unless `self == 0`.

Note that negating any positive integer will overflow.

##### [§](#panics-15)Panics

###### [§](#overflow-behavior-5)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-54)Examples

```rust
assert_eq!(0u8.strict_neg(), 0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 1u8.strict_neg();
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked shift left. Computes `self << rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-55)Examples

```rust
assert_eq!(0x1u8.checked_shl(4), Some(0x10));
assert_eq!(0x10u8.checked_shl(129), None);
assert_eq!(0x10u8.checked_shl(7), Some(0));
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict shift left. Computes `self << rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-16)Panics

###### [§](#overflow-behavior-6)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-56)Examples

```rust
assert_eq!(0x1u8.strict_shl(4), 0x10);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x10u8.strict_shl(129);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unchecked shift left. Computes `self << rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-5)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shl`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_shl "method u8::checked_shl") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unbounded shift left. Computes `self << rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, and `0` is returned.

##### [§](#examples-57)Examples

```rust
assert_eq!(0x1_u8.unbounded_shl(4), 0x10);
assert_eq!(0x1_u8.unbounded_shl(129), 0);
assert_eq!(0b101_u8.unbounded_shl(0), 0b101);
assert_eq!(0b101_u8.unbounded_shl(1), 0b1010);
assert_eq!(0b101_u8.unbounded_shl(2), 0b10100);
assert_eq!(42_u8.unbounded_shl(8), 0);
assert_eq!(42_u8.unbounded_shl(1).unbounded_shl(7), 0);

let start : u8 = 13;
let mut running = start;
for i in 0..160 {
    // The unbounded shift left by i is the same as `<< 1` i times
    assert_eq!(running, start.unbounded_shl(i));
    // Which is not always the case for a wrapping shift
    assert_eq!(running == start.wrapping_shl(i), i < 8);

    running <<= 1;
}
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Exact shift left. Computes `self << rhs` as long as it can be reversed losslessly.

Returns `None` if any non-zero bits would be shifted out or if `rhs` &gt;= `u8::BITS`. Otherwise, returns `Some(self << rhs)`.

##### [§](#examples-58)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x1u8.shl_exact(4), Some(0x10));
assert_eq!(0x1u8.shl_exact(129), None);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Unchecked exact shift left. Computes `self << rhs`, assuming the operation can be losslessly reversed `rhs` cannot be larger than `u8::BITS`.

##### [§](#safety-6)Safety

This results in undefined behavior when `rhs > self.leading_zeros() || rhs >= u8::BITS` i.e. when [`u8::shl_exact`](https://doc.rust-lang.org/std/primitive.u8.html#method.shl_exact "method u8::shl_exact") would return `None`.

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked shift right. Computes `self >> rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-59)Examples

```rust
assert_eq!(0x10u8.checked_shr(4), Some(0x1));
assert_eq!(0x10u8.checked_shr(129), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict shift right. Computes `self >> rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-17)Panics

###### [§](#overflow-behavior-7)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-60)Examples

```rust
assert_eq!(0x10u8.strict_shr(4), 0x1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x10u8.strict_shr(129);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unchecked shift right. Computes `self >> rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-7)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shr`](https://doc.rust-lang.org/std/primitive.u8.html#method.checked_shr "method u8::checked_shr") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Unbounded shift right. Computes `self >> rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, and `0` is returned.

##### [§](#examples-61)Examples

```rust
assert_eq!(0x10_u8.unbounded_shr(4), 0x1);
assert_eq!(0x10_u8.unbounded_shr(129), 0);
assert_eq!(0b1010_u8.unbounded_shr(0), 0b1010);
assert_eq!(0b1010_u8.unbounded_shr(1), 0b101);
assert_eq!(0b1010_u8.unbounded_shr(2), 0b10);
assert_eq!(42_u8.unbounded_shr(8), 0);
assert_eq!(42_u8.unbounded_shr(1).unbounded_shr(7), 0);

let start = u8::rotate_right(13, 4);
let mut running = start;
for i in 0..160 {
    // The unbounded shift right by i is the same as `>> 1` i times
    assert_eq!(running, start.unbounded_shr(i));
    // Which is not always the case for a wrapping shift
    assert_eq!(running == start.wrapping_shr(i), i < 8);

    running >>= 1;
}
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Exact shift right. Computes `self >> rhs` as long as it can be reversed losslessly.

Returns `None` if any non-zero bits would be shifted out or if `rhs` &gt;= `u8::BITS`. Otherwise, returns `Some(self >> rhs)`.

##### [§](#examples-62)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x10u8.shr_exact(4), Some(0x1));
assert_eq!(0x10u8.shr_exact(5), None);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Unchecked exact shift right. Computes `self >> rhs`, assuming the operation can be losslessly reversed and `rhs` cannot be larger than `u8::BITS`.

##### [§](#safety-8)Safety

This results in undefined behavior when `rhs > self.trailing_zeros() || rhs >= u8::BITS` i.e. when [`u8::shr_exact`](https://doc.rust-lang.org/std/primitive.u8.html#method.shr_exact "method u8::shr_exact") would return `None`.

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Checked exponentiation. Computes `self.pow(exp)`, returning `None` if overflow occurred.

##### [§](#examples-63)Examples

```rust
assert_eq!(2u8.checked_pow(5), Some(32));
assert_eq!(0_u8.checked_pow(0), Some(1));
assert_eq!(u8::MAX.checked_pow(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Strict exponentiation. Computes `self.pow(exp)`, panicking if overflow occurred.

##### [§](#panics-18)Panics

###### [§](#overflow-behavior-8)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-64)Examples

```rust
assert_eq!(2u8.strict_pow(5), 32);
assert_eq!(0_u8.strict_pow(0), 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = u8::MAX.strict_pow(2);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating integer addition. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-65)Examples

```rust
assert_eq!(100u8.saturating_add(1), 101);
assert_eq!(u8::MAX.saturating_add(127), u8::MAX);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating addition with a signed integer. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-66)Examples

```rust
assert_eq!(1u8.saturating_add_signed(2), 3);
assert_eq!(1u8.saturating_add_signed(-2), 0);
assert_eq!((u8::MAX - 2).saturating_add_signed(4), u8::MAX);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating integer subtraction. Computes `self - rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-67)Examples

```rust
assert_eq!(100u8.saturating_sub(27), 73);
assert_eq!(13u8.saturating_sub(127), 0);
```

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating integer subtraction. Computes `self` - `rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-68)Examples

```rust
assert_eq!(1u8.saturating_sub_signed(2), 0);
assert_eq!(1u8.saturating_sub_signed(-2), 3);
assert_eq!((u8::MAX - 2).saturating_sub_signed(-4), u8::MAX);
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating integer multiplication. Computes `self * rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-69)Examples

```rust
assert_eq!(2u8.saturating_mul(10), 20);
assert_eq!((u8::MAX).saturating_mul(10), u8::MAX);
```

1.58.0 (const: 1.58.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating integer division. Computes `self / rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#panics-19)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-70)Examples

```rust
assert_eq!(5u8.saturating_div(2), 2);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Saturating integer exponentiation. Computes `self.pow(exp)`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-71)Examples

```rust
assert_eq!(4u8.saturating_pow(3), 64);
assert_eq!(0_u8.saturating_pow(0), 1);
assert_eq!(u8::MAX.saturating_pow(2), u8::MAX);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) addition. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-72)Examples

```rust
assert_eq!(200u8.wrapping_add(55), 255);
assert_eq!(200u8.wrapping_add(u8::MAX), 199);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) addition with a signed integer. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-73)Examples

```rust
assert_eq!(1u8.wrapping_add_signed(2), 3);
assert_eq!(1u8.wrapping_add_signed(-2), u8::MAX);
assert_eq!((u8::MAX - 2).wrapping_add_signed(4), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) subtraction. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-74)Examples

```rust
assert_eq!(100u8.wrapping_sub(100), 0);
assert_eq!(100u8.wrapping_sub(u8::MAX), 101);
```

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) subtraction with a signed integer. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-75)Examples

```rust
assert_eq!(1u8.wrapping_sub_signed(2), u8::MAX);
assert_eq!(1u8.wrapping_sub_signed(-2), 3);
assert_eq!((u8::MAX - 2).wrapping_sub_signed(-4), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) multiplication. Computes `self * rhs`, wrapping around at the boundary of the type.

##### [§](#examples-76)Examples

Please note that this example is shared among integer types, which is why `u8` is used.

```rust
assert_eq!(10u8.wrapping_mul(12), 120);
assert_eq!(25u8.wrapping_mul(12), 44);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) division. Computes `self / rhs`.

Wrapped division on unsigned types is just normal division. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations.

##### [§](#panics-20)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-77)Examples

```rust
assert_eq!(100u8.wrapping_div(10), 10);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping Euclidean division. Computes `self.div_euclid(rhs)`.

Wrapped division on unsigned types is just normal division. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.wrapping_div(rhs)`.

##### [§](#panics-21)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-78)Examples

```rust
assert_eq!(100u8.wrapping_div_euclid(10), 10);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) remainder. Computes `self % rhs`.

Wrapped remainder calculation on unsigned types is just the regular remainder calculation. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations.

##### [§](#panics-22)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-79)Examples

```rust
assert_eq!(100u8.wrapping_rem(10), 0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping Euclidean modulo. Computes `self.rem_euclid(rhs)`.

Wrapped modulo calculation on unsigned types is just the regular remainder calculation. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.wrapping_rem(rhs)`.

##### [§](#panics-23)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-80)Examples

```rust
assert_eq!(100u8.wrapping_rem_euclid(10), 0);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) negation. Computes `-self`, wrapping around at the boundary of the type.

Since unsigned types do not have negative equivalents all applications of this function will wrap (except for `-0`). For values smaller than the corresponding signed type’s maximum the result is the same as casting the corresponding signed value. Any larger values are equivalent to `MAX + 1 - (val - MAX - 1)` where `MAX` is the corresponding signed type’s maximum.

##### [§](#examples-81)Examples

```rust
assert_eq!(0_u8.wrapping_neg(), 0);
assert_eq!(u8::MAX.wrapping_neg(), 1);
assert_eq!(13_u8.wrapping_neg(), (!13) + 1);
assert_eq!(42_u8.wrapping_neg(), !(42 - 1));
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Panic-free bitwise shift-left; yields `self << mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `<<` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shl`](https://doc.rust-lang.org/std/primitive.u8.html#method.unbounded_shl "method u8::unbounded_shl") which has nicer behaviour.

Note that this is *not* the same as a rotate-left; the RHS of a wrapping shift-left is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_left`](https://doc.rust-lang.org/std/primitive.u8.html#method.rotate_left "method u8::rotate_left") function, which may be what you want instead.

##### [§](#examples-82)Examples

```rust
assert_eq!(1_u8.wrapping_shl(7), 128);
assert_eq!(0b101_u8.wrapping_shl(0), 0b101);
assert_eq!(0b101_u8.wrapping_shl(1), 0b1010);
assert_eq!(0b101_u8.wrapping_shl(2), 0b10100);
assert_eq!(u8::MAX.wrapping_shl(2), u8::MAX - 3);
assert_eq!(42_u8.wrapping_shl(8), 42);
assert_eq!(42_u8.wrapping_shl(1).wrapping_shl(7), 0);
assert_eq!(1_u8.wrapping_shl(128), 1);
assert_eq!(5_u8.wrapping_shl(1025), 10);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Panic-free bitwise shift-right; yields `self >> mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `>>` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shr`](https://doc.rust-lang.org/std/primitive.u8.html#method.unbounded_shr "method u8::unbounded_shr") which has nicer behaviour.

Note that this is *not* the same as a rotate-right; the RHS of a wrapping shift-right is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_right`](https://doc.rust-lang.org/std/primitive.u8.html#method.rotate_right "method u8::rotate_right") function, which may be what you want instead.

##### [§](#examples-83)Examples

```rust
assert_eq!(128_u8.wrapping_shr(7), 1);
assert_eq!(0b1010_u8.wrapping_shr(0), 0b1010);
assert_eq!(0b1010_u8.wrapping_shr(1), 0b101);
assert_eq!(0b1010_u8.wrapping_shr(2), 0b10);
assert_eq!(u8::MAX.wrapping_shr(1), i8::MAX.cast_unsigned());
assert_eq!(42_u8.wrapping_shr(8), 42);
assert_eq!(42_u8.wrapping_shr(1).wrapping_shr(7), 0);
assert_eq!(128_u8.wrapping_shr(128), 128);
assert_eq!(10_u8.wrapping_shr(1025), 5);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Wrapping (modular) exponentiation. Computes `self.pow(exp)`, wrapping around at the boundary of the type.

##### [§](#examples-84)Examples

```rust
assert_eq!(3u8.wrapping_pow(5), 243);
assert_eq!(3u8.wrapping_pow(6), 217);
assert_eq!(0_u8.wrapping_pow(0), 1);
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates `self` + `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-85)Examples

```rust
assert_eq!(5u8.overflowing_add(2), (7, false));
assert_eq!(u8::MAX.overflowing_add(1), (0, true));
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates `self` + `rhs` + `carry` and returns a tuple containing the sum and the output carry (in that order).

Performs “ternary addition” of two integer operands and a carry-in bit, and returns an output integer and a carry-out bit. This allows chaining together multiple additions to create a wider addition, and can be useful for bignum addition.

This can be thought of as a 8-bit “full adder”, in the electronics sense.

If the input carry is false, this method is equivalent to [`overflowing_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.overflowing_add "method u8::overflowing_add"), and the output carry is equal to the overflow flag. Note that although carry and overflow flags are similar for unsigned integers, they are different for signed integers.

##### [§](#examples-86)Examples

```rust
//    3  MAX    (a = 3 × 2^8 + 2^8 - 1)
// +  5    7    (b = 5 × 2^8 + 7)
// ---------
//    9    6    (sum = 9 × 2^8 + 6)

let (a1, a0): (u8, u8) = (3, u8::MAX);
let (b1, b0): (u8, u8) = (5, 7);
let carry0 = false;

let (sum0, carry1) = a0.carrying_add(b0, carry0);
assert_eq!(carry1, true);
let (sum1, carry2) = a1.carrying_add(b1, carry1);
assert_eq!(carry2, false);

assert_eq!((sum1, sum0), (9, 6));
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates `self` + `rhs` with a signed `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-87)Examples

```rust
assert_eq!(1u8.overflowing_add_signed(2), (3, false));
assert_eq!(1u8.overflowing_add_signed(-2), (u8::MAX, true));
assert_eq!((u8::MAX - 2).overflowing_add_signed(4), (1, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates `self` - `rhs`.

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-88)Examples

```rust
assert_eq!(5u8.overflowing_sub(2), (3, false));
assert_eq!(0u8.overflowing_sub(1), (u8::MAX, true));
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates `self` − `rhs` − `borrow` and returns a tuple containing the difference and the output borrow.

Performs “ternary subtraction” by subtracting both an integer operand and a borrow-in bit from `self`, and returns an output integer and a borrow-out bit. This allows chaining together multiple subtractions to create a wider subtraction, and can be useful for bignum subtraction.

##### [§](#examples-89)Examples

```rust
//    9    6    (a = 9 × 2^8 + 6)
// -  5    7    (b = 5 × 2^8 + 7)
// ---------
//    3  MAX    (diff = 3 × 2^8 + 2^8 - 1)

let (a1, a0): (u8, u8) = (9, 6);
let (b1, b0): (u8, u8) = (5, 7);
let borrow0 = false;

let (diff0, borrow1) = a0.borrowing_sub(b0, borrow0);
assert_eq!(borrow1, true);
let (diff1, borrow2) = a1.borrowing_sub(b1, borrow1);
assert_eq!(borrow2, false);

assert_eq!((diff1, diff0), (3, u8::MAX));
```

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates `self` - `rhs` with a signed `rhs`

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-90)Examples

```rust
assert_eq!(1u8.overflowing_sub_signed(2), (u8::MAX, true));
assert_eq!(1u8.overflowing_sub_signed(-2), (3, false));
assert_eq!((u8::MAX - 2).overflowing_sub_signed(-4), (1, true));
```

1.60.0 (const: 1.60.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Computes the absolute difference between `self` and `other`.

##### [§](#examples-91)Examples

```rust
assert_eq!(100u8.abs_diff(80), 20u8);
assert_eq!(100u8.abs_diff(110), 10u8);
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the multiplication of `self` and `rhs`.

Returns a tuple of the multiplication along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

If you want the *value* of the overflow, rather than just *whether* an overflow occurred, see [`Self::carrying_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.carrying_mul "method u8::carrying_mul").

##### [§](#examples-92)Examples

Please note that this example is shared among integer types, which is why `u32` is used.

```rust
assert_eq!(5u32.overflowing_mul(2), (10, false));
assert_eq!(1_000_000_000u32.overflowing_mul(10), (1410065408, true));
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`widening_mul` [#152016](https://github.com/rust-lang/rust/issues/152016))

Calculates the complete double-width product `self * rhs`.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order. As such, `a.widening_mul(b).0` produces the same result as `a.wrapping_mul(b)`.

If you also need to add a value and carry to the wide result, then you want [`Self::carrying_mul_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.carrying_mul_add "method u8::carrying_mul_add") instead.

If you also need to add a carry to the wide result, then you want [`Self::carrying_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.carrying_mul "method u8::carrying_mul") instead.

If you just want to know *whether* the multiplication overflowed, then you want [`Self::overflowing_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.overflowing_mul "method u8::overflowing_mul") instead.

##### [§](#examples-93)Examples

```rust
#![feature(widening_mul)]
assert_eq!(5_u8.widening_mul(7), (35, 0));
assert_eq!(u8::MAX.widening_mul(u8::MAX), (1, u8::MAX - 1));
```

Compared to other `*_mul` methods:

```rust
#![feature(widening_mul)]
assert_eq!(u8::widening_mul(1 << 7, 6), (0, 3));
assert_eq!(u8::overflowing_mul(1 << 7, 6), (0, true));
assert_eq!(u8::wrapping_mul(1 << 7, 6), 0);
assert_eq!(u8::checked_mul(1 << 7, 6), None);
```

Please note that this example is shared among integer types, which is why `u32` is used.

```rust
#![feature(widening_mul)]
assert_eq!(5u32.widening_mul(2), (10, 0));
assert_eq!(1_000_000_000u32.widening_mul(10), (1410065408, 2));
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the “full multiplication” `self * rhs + carry` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you also need to add a value, then use [`Self::carrying_mul_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.carrying_mul_add "method u8::carrying_mul_add").

##### [§](#examples-94)Examples

Please note that this example is shared among integer types, which is why `u32` is used.

```rust
assert_eq!(5u32.carrying_mul(2, 0), (10, 0));
assert_eq!(5u32.carrying_mul(2, 10), (20, 0));
assert_eq!(1_000_000_000u32.carrying_mul(10, 0), (1410065408, 2));
assert_eq!(1_000_000_000u32.carrying_mul(10, 10), (1410065418, 2));
assert_eq!(u8::MAX.carrying_mul(u8::MAX, u8::MAX), (0, u8::MAX));
```

This is the core operation needed for scalar multiplication when implementing it for wider-than-native types.

```rust
fn scalar_mul_eq(little_endian_digits: &mut Vec<u16>, multiplicand: u16) {
    let mut carry = 0;
    for d in little_endian_digits.iter_mut() {
        (*d, carry) = d.carrying_mul(multiplicand, carry);
    }
    if carry != 0 {
        little_endian_digits.push(carry);
    }
}

let mut v = vec![10, 20];
scalar_mul_eq(&mut v, 3);
assert_eq!(v, [30, 60]);

assert_eq!(0x87654321_u64 * 0xFEED, 0x86D3D159E38D);
let mut v = vec![0x4321, 0x8765];
scalar_mul_eq(&mut v, 0xFEED);
assert_eq!(v, [0xE38D, 0xD159, 0x86D3]);
```

If `carry` is zero, this is similar to [`overflowing_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.overflowing_mul "method u8::overflowing_mul"), except that it gives the value of the overflow instead of just whether one happened:

```rust
#![feature(const_unsigned_bigint_helpers)]
let r = u8::carrying_mul(7, 13, 0);
assert_eq!((r.0, r.1 != 0), u8::overflowing_mul(7, 13));
let r = u8::carrying_mul(13, 42, 0);
assert_eq!((r.0, r.1 != 0), u8::overflowing_mul(13, 42));
```

The value of the first field in the returned tuple matches what you’d get by combining the [`wrapping_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.wrapping_mul "method u8::wrapping_mul") and [`wrapping_add`](https://doc.rust-lang.org/std/primitive.u8.html#method.wrapping_add "method u8::wrapping_add") methods:

```rust
#![feature(const_unsigned_bigint_helpers)]
assert_eq!(
    789_u16.carrying_mul(456, 123).0,
    789_u16.wrapping_mul(456).wrapping_add(123),
);
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the “full multiplication” `self * rhs + carry + add`.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

This cannot overflow, as the double-width result has exactly enough space for the largest possible result. This is equivalent to how, in decimal, 9 × 9 + 9 + 9 = 81 + 18 = 99 = 9×10⁰ + 9×10¹ = 10² - 1.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you don’t need the `add` part, then you can use [`Self::carrying_mul`](https://doc.rust-lang.org/std/primitive.u8.html#method.carrying_mul "method u8::carrying_mul") instead.

##### [§](#examples-95)Examples

Please note that this example is shared between integer types, which explains why `u32` is used here.

```rust
assert_eq!(5u32.carrying_mul_add(2, 0, 0), (10, 0));
assert_eq!(5u32.carrying_mul_add(2, 10, 10), (30, 0));
assert_eq!(1_000_000_000u32.carrying_mul_add(10, 0, 0), (1410065408, 2));
assert_eq!(1_000_000_000u32.carrying_mul_add(10, 10, 10), (1410065428, 2));
assert_eq!(u8::MAX.carrying_mul_add(u8::MAX, u8::MAX, u8::MAX), (u8::MAX, u8::MAX));
```

This is the core per-digit operation for “grade school” O(n²) multiplication.

Please note that this example is shared between integer types, using `u8` for simplicity of the demonstration.

```rust
fn quadratic_mul<const N: usize>(a: [u8; N], b: [u8; N]) -> [u8; N] {
    let mut out = [0; N];
    for j in 0..N {
        let mut carry = 0;
        for i in 0..(N - j) {
            (out[j + i], carry) = u8::carrying_mul_add(a[i], b[j], out[j + i], carry);
        }
    }
    out
}

// -1 * -1 == 1
assert_eq!(quadratic_mul([0xFF; 3], [0xFF; 3]), [1, 0, 0]);

assert_eq!(u32::wrapping_mul(0x9e3779b9, 0x7f4a7c15), 0xcffc982d);
assert_eq!(
    quadratic_mul(u32::to_le_bytes(0x9e3779b9), u32::to_le_bytes(0x7f4a7c15)),
    u32::to_le_bytes(0xcffc982d)
);
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the divisor when `self` is divided by `rhs`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`.

##### [§](#panics-24)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-96)Examples

```rust
assert_eq!(5u8.overflowing_div(2), (2, false));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the quotient of Euclidean division `self.div_euclid(rhs)`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.overflowing_div(rhs)`.

##### [§](#panics-25)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-97)Examples

```rust
assert_eq!(5u8.overflowing_div_euclid(2), (2, false));
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the remainder when `self` is divided by `rhs`.

Returns a tuple of the remainder after dividing along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`.

##### [§](#panics-26)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-98)Examples

```rust
assert_eq!(5u8.overflowing_rem(2), (1, false));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the remainder `self.rem_euclid(rhs)` as if by Euclidean division.

Returns a tuple of the modulo after dividing along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`. Since, for the positive integers, all common definitions of division are equal, this operation is exactly equal to `self.overflowing_rem(rhs)`.

##### [§](#panics-27)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-99)Examples

```rust
assert_eq!(5u8.overflowing_rem_euclid(2), (1, false));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Negates self in an overflowing fashion.

Returns `!self + 1` using wrapping operations to return the value that represents the negation of this unsigned value. Note that for positive unsigned values overflow always occurs, but negating 0 does not overflow.

##### [§](#examples-100)Examples

```rust
assert_eq!(0u8.overflowing_neg(), (0, false));
assert_eq!(2u8.overflowing_neg(), (-2i32 as u8, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Shifts self left by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-101)Examples

```rust
assert_eq!(0x1u8.overflowing_shl(4), (0x10, false));
assert_eq!(0x1u8.overflowing_shl(132), (0x10, true));
assert_eq!(0x10u8.overflowing_shl(7), (0, false));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Shifts self right by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-102)Examples

```rust
assert_eq!(0x10u8.overflowing_shr(4), (0x1, false));
assert_eq!(0x10u8.overflowing_shr(132), (0x1, true));
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Raises self to the power of `exp`, using exponentiation by squaring.

Returns a tuple of the exponentiation along with a bool indicating whether an overflow happened.

##### [§](#examples-103)Examples

```rust
assert_eq!(3u8.overflowing_pow(5), (243, false));
assert_eq!(0_u8.overflowing_pow(0), (1, false));
assert_eq!(3u8.overflowing_pow(6), (217, true));
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Raises self to the power of `exp`, using exponentiation by squaring.

##### [§](#examples-104)Examples

```rust
assert_eq!(2u8.pow(5), 32);
assert_eq!(0_u8.pow(0), 1);
```

1.84.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the square root of the number, rounded down.

##### [§](#examples-105)Examples

```rust
assert_eq!(10u8.isqrt(), 3);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Performs Euclidean division.

Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self / rhs`.

##### [§](#panics-28)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-106)Examples

```rust
assert_eq!(7u8.div_euclid(4), 1); // or any other integer type
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the least remainder of `self` when divided by `rhs`.

Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self % rhs`.

##### [§](#panics-29)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-107)Examples

```rust
assert_eq!(7u8.rem_euclid(4), 3); // or any other integer type
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Calculates the quotient of `self` and `rhs`, rounding the result towards negative infinity.

This is the same as performing `self / rhs` for all unsigned integers.

##### [§](#panics-30)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-108)Examples

```rust
#![feature(int_roundings)]
assert_eq!(7_u8.div_floor(4), 1);
```

1.73.0 (const: 1.73.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the quotient of `self` and `rhs`, rounding the result towards positive infinity.

##### [§](#panics-31)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-109)Examples

```rust
assert_eq!(7_u8.div_ceil(4), 2);
```

1.73.0 (const: 1.73.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`.

##### [§](#panics-32)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-9)Overflow behavior

On overflow, this function will panic if overflow checks are enabled (default in debug mode) and wrap if overflow checks are disabled (default in release mode).

##### [§](#examples-110)Examples

```rust
assert_eq!(16_u8.next_multiple_of(8), 16);
assert_eq!(23_u8.next_multiple_of(8), 24);
```

1.73.0 (const: 1.73.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`. Returns `None` if `rhs` is zero or the operation would result in overflow.

##### [§](#examples-111)Examples

```rust
assert_eq!(16_u8.checked_next_multiple_of(8), Some(16));
assert_eq!(23_u8.checked_next_multiple_of(8), Some(24));
assert_eq!(1_u8.checked_next_multiple_of(0), None);
assert_eq!(u8::MAX.checked_next_multiple_of(2), None);
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns `true` if `self` is an integer multiple of `rhs`, and false otherwise.

This function is equivalent to `self % rhs == 0`, except that it will not panic for `rhs == 0`. Instead, `0.is_multiple_of(0) == true`, and for any non-zero `n`, `n.is_multiple_of(0) == false`.

##### [§](#examples-112)Examples

```rust
assert!(6_u8.is_multiple_of(2));
assert!(!5_u8.is_multiple_of(2));

assert!(0_u8.is_multiple_of(0));
assert!(!6_u8.is_multiple_of(0));
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns `true` if and only if `self == 2^k` for some unsigned integer `k`.

##### [§](#examples-113)Examples

```rust
assert!(16u8.is_power_of_two());
assert!(!10u8.is_power_of_two());
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the smallest power of two greater than or equal to `self`.

When return value overflows (i.e., `self > (1 << (N-1))` for type `uN`), it panics in debug mode and the return value is wrapped to 0 in release mode (the only situation in which this method can return 0).

##### [§](#examples-114)Examples

```rust
assert_eq!(2u8.next_power_of_two(), 2);
assert_eq!(3u8.next_power_of_two(), 4);
assert_eq!(0u8.next_power_of_two(), 1);
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the smallest power of two greater than or equal to `self`. If the next power of two is greater than the type’s maximum value, `None` is returned, otherwise the power of two is wrapped in `Some`.

##### [§](#examples-115)Examples

```rust
assert_eq!(2u8.checked_next_power_of_two(), Some(2));
assert_eq!(3u8.checked_next_power_of_two(), Some(4));
assert_eq!(u8::MAX.checked_next_power_of_two(), None);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

🔬This is a nightly-only experimental API. (`wrapping_next_power_of_two` [#32463](https://github.com/rust-lang/rust/issues/32463))

Returns the smallest power of two greater than or equal to `n`. If the next power of two is greater than the type’s maximum value, the return value is wrapped to `0`.

##### [§](#examples-116)Examples

```rust
#![feature(wrapping_next_power_of_two)]

assert_eq!(2u8.wrapping_next_power_of_two(), 2);
assert_eq!(3u8.wrapping_next_power_of_two(), 4);
assert_eq!(u8::MAX.wrapping_next_power_of_two(), 0);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the memory representation of this integer as a byte array in big-endian (network) byte order.

**Note**: This function is meaningless on `u8`. Byte order does not exist as a concept for byte-sized integers. This function is only provided in symmetry with larger integer types.

##### [§](#examples-117)Examples

```rust
let bytes = 0x12u8.to_be_bytes();
assert_eq!(bytes, [0x12]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the memory representation of this integer as a byte array in little-endian byte order.

**Note**: This function is meaningless on `u8`. Byte order does not exist as a concept for byte-sized integers. This function is only provided in symmetry with larger integer types.

##### [§](#examples-118)Examples

```rust
let bytes = 0x12u8.to_le_bytes();
assert_eq!(bytes, [0x12]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Returns the memory representation of this integer as a byte array in native byte order.

As the target platform’s native endianness is used, portable code should use [`to_be_bytes`](https://doc.rust-lang.org/std/primitive.u8.html#method.to_be_bytes "method u8::to_be_bytes") or [`to_le_bytes`](https://doc.rust-lang.org/std/primitive.u8.html#method.to_le_bytes "method u8::to_le_bytes"), as appropriate, instead.

**Note**: This function is meaningless on `u8`. Byte order does not exist as a concept for byte-sized integers. This function is only provided in symmetry with larger integer types.

##### [§](#examples-119)Examples

```rust
let bytes = 0x12u8.to_ne_bytes();
assert_eq!(
    bytes,
    if cfg!(target_endian = "big") {
        [0x12]
    } else {
        [0x12]
    }
);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Creates a native endian integer value from its representation as a byte array in big endian.

**Note**: This function is meaningless on `u8`. Byte order does not exist as a concept for byte-sized integers. This function is only provided in symmetry with larger integer types.

##### [§](#examples-120)Examples

```rust
let value = u8::from_be_bytes([0x12]);
assert_eq!(value, 0x12);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_be_u8(input: &mut &[u8]) -> u8 {
    let (int_bytes, rest) = input.split_at(size_of::<u8>());
    *input = rest;
    u8::from_be_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Creates a native endian integer value from its representation as a byte array in little endian.

**Note**: This function is meaningless on `u8`. Byte order does not exist as a concept for byte-sized integers. This function is only provided in symmetry with larger integer types.

##### [§](#examples-121)Examples

```rust
let value = u8::from_le_bytes([0x12]);
assert_eq!(value, 0x12);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_le_u8(input: &mut &[u8]) -> u8 {
    let (int_bytes, rest) = input.split_at(size_of::<u8>());
    *input = rest;
    u8::from_le_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

Creates a native endian integer value from its memory representation as a byte array in native endianness.

As the target platform’s native endianness is used, portable code likely wants to use [`from_be_bytes`](https://doc.rust-lang.org/std/primitive.u8.html#method.from_be_bytes "associated function u8::from_be_bytes") or [`from_le_bytes`](https://doc.rust-lang.org/std/primitive.u8.html#method.from_le_bytes "associated function u8::from_le_bytes"), as appropriate instead.

**Note**: This function is meaningless on `u8`. Byte order does not exist as a concept for byte-sized integers. This function is only provided in symmetry with larger integer types.

##### [§](#examples-122)Examples

```rust
let value = u8::from_ne_bytes(if cfg!(target_endian = "big") {
    [0x12]
} else {
    [0x12]
});
assert_eq!(value, 0x12);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_ne_u8(input: &mut &[u8]) -> u8 {
    let (int_bytes, rest) = input.split_at(size_of::<u8>());
    *input = rest;
    u8::from_ne_bytes(int_bytes.try_into().unwrap())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

👎Deprecating in a future version: replaced by the `MIN` associated constant on this type

New code should prefer to use [`u8::MIN`](https://doc.rust-lang.org/std/primitive.u8.html#associatedconstant.MIN "associated constant u8::MIN") instead.

Returns the smallest value that can be represented by this integer type.

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570)

👎Deprecating in a future version: replaced by the `MAX` associated constant on this type

New code should prefer to use [`u8::MAX`](https://doc.rust-lang.org/std/primitive.u8.html#associatedconstant.MAX "associated constant u8::MAX") instead.

Returns the largest value that can be represented by this integer type.

1.85.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#571)

Calculates the midpoint (average) between `self` and `rhs`.

`midpoint(a, b)` is `(a + b) / 2` as if it were performed in a sufficiently-large unsigned integral type. This implies that the result is always rounded towards zero and that no overflow will ever occur.

##### [§](#examples-123)Examples

```rust
assert_eq!(0u8.midpoint(4), 2);
assert_eq!(1u8.midpoint(4), 2);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#572)

🔬This is a nightly-only experimental API. (`uint_carryless_mul` [#152080](https://github.com/rust-lang/rust/issues/152080))

Performs a widening carry-less multiplication.

##### [§](#examples-124)Examples

```rust
#![feature(uint_carryless_mul)]

assert_eq!(u8::MAX.widening_carryless_mul(u8::MAX), u16::MAX / 3);
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#573)

🔬This is a nightly-only experimental API. (`uint_carryless_mul` [#152080](https://github.com/rust-lang/rust/issues/152080))

Calculates the “full carryless multiplication” without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

##### [§](#examples-125)Examples

Please note that this example is shared among integer types, which is why `u8` is used.

```rust
#![feature(uint_carryless_mul)]

assert_eq!(0b1000_0000u8.carrying_carryless_mul(0b1000_0000, 0b0000), (0, 0b0100_0000));
assert_eq!(0b1000_0000u8.carrying_carryless_mul(0b1000_0000, 0b1111), (0b1111, 0b0100_0000));
assert_eq!(u8::MAX.carrying_carryless_mul(u8::MAX, u8::MAX), (!(u8::MAX / 3), u8::MAX / 3));
```

1.23.0 (const: 1.43.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#590)

Checks if the value is within the ASCII range.

##### [§](#examples-126)Examples

```rust
let ascii = 97u8;
let non_ascii = 150u8;

assert!(ascii.is_ascii());
assert!(!non_ascii.is_ascii());
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#599)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

If the value of this byte is within the ASCII range, returns it as an [ASCII character](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"). Otherwise, returns `None`.

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#612)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this byte to an [ASCII character](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"), without checking whether or not it’s valid.

##### [§](#safety-9)Safety

This byte must be valid ASCII, or else this is UB.

1.23.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#643)

Makes a copy of the value in its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`make_ascii_uppercase`](https://doc.rust-lang.org/std/primitive.u8.html#method.make_ascii_uppercase "method u8::make_ascii_uppercase").

##### [§](#examples-127)Examples

```rust
let lowercase_a = 97u8;

assert_eq!(65, lowercase_a.to_ascii_uppercase());
```

1.23.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#668)

Makes a copy of the value in its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use [`make_ascii_lowercase`](https://doc.rust-lang.org/std/primitive.u8.html#method.make_ascii_lowercase "method u8::make_ascii_lowercase").

##### [§](#examples-128)Examples

```rust
let uppercase_a = 65u8;

assert_eq!(97, uppercase_a.to_ascii_lowercase());
```

1.23.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#694)

Checks that two values are an ASCII case-insensitive match.

This is equivalent to `to_ascii_lowercase(a) == to_ascii_lowercase(b)`.

##### [§](#examples-129)Examples

```rust
let lowercase_a = 97u8;
let uppercase_a = 65u8;

assert!(lowercase_a.eq_ignore_ascii_case(&uppercase_a));
```

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#720)

Converts this value to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use [`to_ascii_uppercase`](https://doc.rust-lang.org/std/primitive.u8.html#method.to_ascii_uppercase "method u8::to_ascii_uppercase").

##### [§](#examples-130)Examples

```rust
let mut byte = b'a';

byte.make_ascii_uppercase();

assert_eq!(b'A', byte);
```

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#746)

Converts this value to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use [`to_ascii_lowercase`](https://doc.rust-lang.org/std/primitive.u8.html#method.to_ascii_lowercase "method u8::to_ascii_lowercase").

##### [§](#examples-131)Examples

```rust
let mut byte = b'A';

byte.make_ascii_lowercase();

assert_eq!(b'a', byte);
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#782)

Checks if the value is an ASCII alphabetic character:

- U+0041 ‘A’ ..= U+005A ‘Z’, or
- U+0061 ‘a’ ..= U+007A ‘z’.

##### [§](#examples-132)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(uppercase_a.is_ascii_alphabetic());
assert!(uppercase_g.is_ascii_alphabetic());
assert!(a.is_ascii_alphabetic());
assert!(g.is_ascii_alphabetic());
assert!(!zero.is_ascii_alphabetic());
assert!(!percent.is_ascii_alphabetic());
assert!(!space.is_ascii_alphabetic());
assert!(!lf.is_ascii_alphabetic());
assert!(!esc.is_ascii_alphabetic());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#816)

Checks if the value is an ASCII uppercase character: U+0041 ‘A’ ..= U+005A ‘Z’.

##### [§](#examples-133)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(uppercase_a.is_ascii_uppercase());
assert!(uppercase_g.is_ascii_uppercase());
assert!(!a.is_ascii_uppercase());
assert!(!g.is_ascii_uppercase());
assert!(!zero.is_ascii_uppercase());
assert!(!percent.is_ascii_uppercase());
assert!(!space.is_ascii_uppercase());
assert!(!lf.is_ascii_uppercase());
assert!(!esc.is_ascii_uppercase());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#850)

Checks if the value is an ASCII lowercase character: U+0061 ‘a’ ..= U+007A ‘z’.

##### [§](#examples-134)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(!uppercase_a.is_ascii_lowercase());
assert!(!uppercase_g.is_ascii_lowercase());
assert!(a.is_ascii_lowercase());
assert!(g.is_ascii_lowercase());
assert!(!zero.is_ascii_lowercase());
assert!(!percent.is_ascii_lowercase());
assert!(!space.is_ascii_lowercase());
assert!(!lf.is_ascii_lowercase());
assert!(!esc.is_ascii_lowercase());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#887)

Checks if the value is an ASCII alphanumeric character:

- U+0041 ‘A’ ..= U+005A ‘Z’, or
- U+0061 ‘a’ ..= U+007A ‘z’, or
- U+0030 ‘0’ ..= U+0039 ‘9’.

##### [§](#examples-135)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(uppercase_a.is_ascii_alphanumeric());
assert!(uppercase_g.is_ascii_alphanumeric());
assert!(a.is_ascii_alphanumeric());
assert!(g.is_ascii_alphanumeric());
assert!(zero.is_ascii_alphanumeric());
assert!(!percent.is_ascii_alphanumeric());
assert!(!space.is_ascii_alphanumeric());
assert!(!lf.is_ascii_alphanumeric());
assert!(!esc.is_ascii_alphanumeric());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#921)

Checks if the value is an ASCII decimal digit: U+0030 ‘0’ ..= U+0039 ‘9’.

##### [§](#examples-136)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(!uppercase_a.is_ascii_digit());
assert!(!uppercase_g.is_ascii_digit());
assert!(!a.is_ascii_digit());
assert!(!g.is_ascii_digit());
assert!(zero.is_ascii_digit());
assert!(!percent.is_ascii_digit());
assert!(!space.is_ascii_digit());
assert!(!lf.is_ascii_digit());
assert!(!esc.is_ascii_digit());
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#952)

🔬This is a nightly-only experimental API. (`is_ascii_octdigit` [#101288](https://github.com/rust-lang/rust/issues/101288))

Checks if the value is an ASCII octal digit: U+0030 ‘0’ ..= U+0037 ‘7’.

##### [§](#examples-137)Examples

```rust
#![feature(is_ascii_octdigit)]

let uppercase_a = b'A';
let a = b'a';
let zero = b'0';
let seven = b'7';
let nine = b'9';
let percent = b'%';
let lf = b'\n';

assert!(!uppercase_a.is_ascii_octdigit());
assert!(!a.is_ascii_octdigit());
assert!(zero.is_ascii_octdigit());
assert!(seven.is_ascii_octdigit());
assert!(!nine.is_ascii_octdigit());
assert!(!percent.is_ascii_octdigit());
assert!(!lf.is_ascii_octdigit());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#989)

Checks if the value is an ASCII hexadecimal digit:

- U+0030 ‘0’ ..= U+0039 ‘9’, or
- U+0041 ‘A’ ..= U+0046 ‘F’, or
- U+0061 ‘a’ ..= U+0066 ‘f’.

##### [§](#examples-138)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(uppercase_a.is_ascii_hexdigit());
assert!(!uppercase_g.is_ascii_hexdigit());
assert!(a.is_ascii_hexdigit());
assert!(!g.is_ascii_hexdigit());
assert!(zero.is_ascii_hexdigit());
assert!(!percent.is_ascii_hexdigit());
assert!(!space.is_ascii_hexdigit());
assert!(!lf.is_ascii_hexdigit());
assert!(!esc.is_ascii_hexdigit());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1027)

Checks if the value is an ASCII punctuation character:

- U+0021 ..= U+002F `! " # $ % & ' ( ) * + , - . /`, or
- U+003A ..= U+0040 `: ; < = > ? @`, or
- U+005B ..= U+0060 ``[ \ ] ^ _ ` ``, or
- U+007B ..= U+007E `{ | } ~`

##### [§](#examples-139)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(!uppercase_a.is_ascii_punctuation());
assert!(!uppercase_g.is_ascii_punctuation());
assert!(!a.is_ascii_punctuation());
assert!(!g.is_ascii_punctuation());
assert!(!zero.is_ascii_punctuation());
assert!(percent.is_ascii_punctuation());
assert!(!space.is_ascii_punctuation());
assert!(!lf.is_ascii_punctuation());
assert!(!esc.is_ascii_punctuation());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1064)

Checks if the value is an ASCII graphic character: U+0021 ‘!’ ..= U+007E ‘~’.

##### [§](#examples-140)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(uppercase_a.is_ascii_graphic());
assert!(uppercase_g.is_ascii_graphic());
assert!(a.is_ascii_graphic());
assert!(g.is_ascii_graphic());
assert!(zero.is_ascii_graphic());
assert!(percent.is_ascii_graphic());
assert!(!space.is_ascii_graphic());
assert!(!lf.is_ascii_graphic());
assert!(!esc.is_ascii_graphic());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1115)

Checks if the value is an ASCII whitespace character: U+0020 SPACE, U+0009 HORIZONTAL TAB, U+000A LINE FEED, U+000C FORM FEED, or U+000D CARRIAGE RETURN.

Rust uses the WhatWG Infra Standard’s [definition of ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace). There are several other definitions in wide use. For instance, [the POSIX locale](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap07.html#tag_07_03_01) includes U+000B VERTICAL TAB as well as all the above characters, but—from the very same specification—[the default rule for “field splitting” in the Bourne shell](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_05) considers *only* SPACE, HORIZONTAL TAB, and LINE FEED as whitespace.

If you are writing a program that will process an existing file format, check what that format’s definition of whitespace is before using this function.

##### [§](#examples-141)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(!uppercase_a.is_ascii_whitespace());
assert!(!uppercase_g.is_ascii_whitespace());
assert!(!a.is_ascii_whitespace());
assert!(!g.is_ascii_whitespace());
assert!(!zero.is_ascii_whitespace());
assert!(!percent.is_ascii_whitespace());
assert!(space.is_ascii_whitespace());
assert!(lf.is_ascii_whitespace());
assert!(!esc.is_ascii_whitespace());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1151)

Checks if the value is an ASCII control character: U+0000 NUL ..= U+001F UNIT SEPARATOR, or U+007F DELETE. Note that most ASCII whitespace characters are control characters, but SPACE is not.

##### [§](#examples-142)Examples

```rust
let uppercase_a = b'A';
let uppercase_g = b'G';
let a = b'a';
let g = b'g';
let zero = b'0';
let percent = b'%';
let space = b' ';
let lf = b'\n';
let esc = b'\x1b';

assert!(!uppercase_a.is_ascii_control());
assert!(!uppercase_g.is_ascii_control());
assert!(!a.is_ascii_control());
assert!(!g.is_ascii_control());
assert!(!zero.is_ascii_control());
assert!(!percent.is_ascii_control());
assert!(!space.is_ascii_control());
assert!(lf.is_ascii_control());
assert!(esc.is_ascii_control());
```

1.60.0 · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1176)

Returns an iterator that produces an escaped version of a `u8`, treating it as an ASCII character.

The behavior is identical to [`ascii::escape_default`](https://doc.rust-lang.org/std/ascii/fn.escape_default.html "fn std::ascii::escape_default").

##### [§](#examples-143)Examples

```rust
assert_eq!("0", b'0'.escape_ascii().to_string());
assert_eq!("\\t", b'\t'.escape_ascii().to_string());
assert_eq!("\\r", b'\r'.escape_ascii().to_string());
assert_eq!("\\n", b'\n'.escape_ascii().to_string());
assert_eq!("\\'", b'\''.escape_ascii().to_string());
assert_eq!("\\\"", b'"'.escape_ascii().to_string());
assert_eq!("\\\\", b'\\'.escape_ascii().to_string());
assert_eq!("\\x9d", b'\x9d'.escape_ascii().to_string());
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)[§](#impl-u8-1)

1.0.0 (const: 1.82.0) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)

Parses an integer from a string slice with digits in a given base.

The string is expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

Digits are a subset of these characters, depending on `radix`:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#panics-33)Panics

This function panics if `radix` is not in the range from 2 to 36.

##### [§](#see-also)See also

If the string to be parsed is in base 10 (decimal), [`from_str`](#method.from_str) or [`str::parse`](https://doc.rust-lang.org/std/primitive.str.html#method.parse) can also be used.

##### [§](#examples-144)Examples

```rust
assert_eq!(u8::from_str_radix("A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(u8::from_str_radix("1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with decimal digits.

The characters are expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#examples-145)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(u8::from_ascii(b"+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(u8::from_ascii(b"1 ").is_err());
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with digits in a given base.

The characters are expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

Digits are a subset of these characters, depending on `radix`:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#panics-34)Panics

This function panics if `radix` is not in the range from 2 to 36.

##### [§](#examples-146)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(u8::from_ascii_radix(b"A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(u8::from_ascii_radix(b"1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#599)[§](#impl-u8-2)

[Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#599)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Allows users to write an integer (in signed decimal format) into a variable `buf` of type [`NumBuffer`](https://doc.rust-lang.org/core/fmt/num_buffer/struct.NumBuffer.html "struct core::fmt::num_buffer::NumBuffer") that is passed by the caller by mutable reference.

##### [§](#examples-147)Examples

```rust
#![feature(int_format_into)]
use core::fmt::NumBuffer;

let n = 0u8;
let mut buf = NumBuffer::new();
assert_eq!(n.format_into(&mut buf), "0");

let n1 = 32u8;
assert_eq!(n1.format_into(&mut buf), "32");

let n2 = u8 :: MAX;
assert_eq!(n2.format_into(&mut buf), u8 :: MAX.to_string());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ascii.rs.html#182-186)[§](#impl-AsciiExt-for-u8)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#183)[§](#associatedtype.Owned)

👎Deprecated since 1.26.0: use inherent methods instead

Container type for copied ASCII characters.

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#185)[§](#method.is_ascii-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks if the value is within the ASCII range. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.is_ascii)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#185)[§](#method.to_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII upper case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#185)[§](#method.to_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII lower case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_lowercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#185)[§](#method.eq_ignore_ascii_case-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks that two values are an ASCII case-insensitive match. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.eq_ignore_ascii_case)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#185)[§](#method.make_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII upper case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#185)[§](#method.make_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII lower case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_lowercase)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-17)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-16)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-15)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-14)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign%3C%26u8%3E-for-u8)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign-for-u8)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#299)[§](#impl-AtomicPrimitive-for-u8)

Available on **`target_has_atomic_load_store=8`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#299)[§](#associatedtype.AtomicInner)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#impl-Binary-for-u8)

[Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#method.fmt-2)

Format unsigned integers in the radix.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-35)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#method.bitand-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-34)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#method.bitand-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-33)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#method.bitand-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-32)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#187)[§](#method.bitand)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign%3C%26u8%3E-for-u8)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-3)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#method.bitor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-2)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#method.bitor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-1)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#method.bitor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#impl-BitOr-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#291)[§](#method.bitor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign%3C%26u8%3E-for-u8)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-31)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#method.bitxor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-30)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#method.bitxor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-29)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#method.bitxor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#impl-BitXor-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-28)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#395)[§](#method.bitxor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign%3C%26u8%3E-for-u8)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign-for-u8)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#34-45)[§](#impl-CarryingMulAdd-for-u8)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#34-45)[§](#associatedtype.Unsigned)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#34-45)[§](#method.carrying_mul_add-1)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#253-255)[§](#impl-CarrylessMul-for-u8)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#253-255)[§](#method.carryless_mul-1)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::carryless_mul`](https://doc.rust-lang.org/std/intrinsics/fn.carryless_mul.html "fn std::intrinsics::carryless_mul"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-u8)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#589-592)[§](#impl-Debug-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/default.rs.html#170)[§](#impl-Default-for-u8)

[Source](https://doc.rust-lang.org/src/core/default.rs.html#170)[§](#method.default)

Returns the default value of `0`

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#144-148)[§](#impl-DisjointBitOr-for-u8)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#144-148)[§](#method.disjoint_bitor)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::disjoint_bitor`](https://doc.rust-lang.org/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#599)[§](#impl-Display-for-u8)

[Source](https://doc.rust-lang.org/src/core/random.rs.html#49)[§](#impl-Distribution%3Cu8%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/src/core/random.rs.html#49)[§](#method.sample)

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Samples a random value from the distribution, using the specified random source.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-8)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#method.div-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-7)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#method.div-3)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#impl-Div%3CNonZero%3Cu8%3E%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#method.div)

Same as `self / other.get()`, but because `other` is a `NonZero<_>`, there’s never a runtime check for division-by-zero.

This operation rounds towards zero, truncating any fractional part of the exact result, and cannot panic.

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#associatedtype.Output-4)

The resulting type after applying the `/` operator.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-6)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#method.div-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u8)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-35)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-5)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#method.div-1)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign%3C%26u8%3E-for-u8)

1.79.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#impl-DivAssign%3CNonZero%3Cu8%3E%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#method.div_assign)

Same as `self /= other.get()`, but because `other` is a `NonZero<_>`, there’s never a runtime check for division-by-zero.

This operation rounds towards zero, truncating any fractional part of the exact result, and cannot panic.

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign-for-u8)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#method.from-15)

Converts to this type from the input type.

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#method.from)

Converts from [`bool`](https://doc.rust-lang.org/std/primitive.bool.html "primitive bool") to [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-149)Examples

```rust
assert_eq!(u8::from(false), 0);

assert_eq!(u8::from(true), 1);
```

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3615-3632)[§](#impl-From%3Cu8%3E-for-AtomicU8)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3615-3632)[§](#method.from-17)

Converts an `u8` into an `AtomicU8`.

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2197-2202)[§](#impl-From%3Cu8%3E-for-ExitCode)

[Source](https://doc.rust-lang.org/src/std/process.rs.html#2199-2201)[§](#method.from-18)

Constructs an `ExitCode` from an arbitrary u8 value.

1.13.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#217)[§](#impl-From%3Cu8%3E-for-char)

Maps a byte in `0x00..=0xFF` to a `char` whose code point has the same value from U+0000 to U+00FF (inclusive).

Unicode is designed such that this effectively decodes bytes with the character encoding that IANA calls ISO-8859-1. This encoding is compatible with ASCII.

Note that this is different from ISO/IEC 8859-1 a.k.a. ISO 8859-1 (with one less hyphen), which leaves some “blanks”, byte values that are not assigned to any character. ISO-8859-1 (the IANA one) assigns them to the C0 and C1 control codes.

Note that this is *also* different from Windows-1252 a.k.a. code page 1252, which is a superset ISO/IEC 8859-1 that assigns some (not all!) blanks to punctuation and various Latin characters.

To confuse things further, [on the Web](https://encoding.spec.whatwg.org/) `ascii`, `iso-8859-1`, and `windows-1252` are all aliases for a superset of Windows-1252 that fills the remaining blanks with corresponding C0 and C1 control codes.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#229)[§](#method.from-16)

Converts a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8") into a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char").

##### [§](#examples-150)Examples

```rust
let u = 32 as u8;
let c = char::from(u);

assert!(4 == size_of_val(&c))
```

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#167)[§](#impl-From%3Cu8%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#164)[§](#impl-From%3Cu8%3E-for-f16)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#165)[§](#impl-From%3Cu8%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#166)[§](#impl-From%3Cu8%3E-for-f64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#118)[§](#impl-From%3Cu8%3E-for-i128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#115)[§](#impl-From%3Cu8%3E-for-i16)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#116)[§](#impl-From%3Cu8%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#117)[§](#impl-From%3Cu8%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#130)[§](#impl-From%3Cu8%3E-for-isize)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#92)[§](#impl-From%3Cu8%3E-for-u128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#89)[§](#impl-From%3Cu8%3E-for-u16)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#90)[§](#impl-From%3Cu8%3E-for-u32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#91)[§](#impl-From%3Cu8%3E-for-u64)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#93)[§](#impl-From%3Cu8%3E-for-usize)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#272)[§](#impl-FromIterator%3Cu8%3E-for-ByteString)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)[§](#impl-FromStr-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)[§](#method.from_str)

Parses an integer from a string slice with decimal digits.

The characters are expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#see-also-1)See also

For parsing numbers in other bases, such as binary or hexadecimal, see [`from_str_radix`](https://doc.rust-lang.org/std/primitive.u8.html#method.from_str_radix "associated function u8::from_str_radix").

##### [§](#examples-148)Examples

```rust
use std::str::FromStr;

assert_eq!(u8::from_str("+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(u8::from_str("1 ").is_err());
```

[Source](https://doc.rust-lang.org/src/core/num/mod.rs.html#1802)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#218-220)[§](#impl-FunnelShift-for-u8)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#218-220)[§](#method.unchecked_funnel_shl)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::unchecked_funnel_shl`](https://doc.rust-lang.org/std/intrinsics/fn.unchecked_funnel_shl.html "fn std::intrinsics::unchecked_funnel_shl"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#218-220)[§](#method.unchecked_funnel_shr)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::unchecked_funnel_shr`](https://doc.rust-lang.org/std/intrinsics/fn.unchecked_funnel_shr.html "fn std::intrinsics::unchecked_funnel_shr"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u8)

1.42.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#600)[§](#impl-LowerExp-for-u8)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#impl-LowerHex-for-u8)

[Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#method.fmt-4)

Format unsigned integers in the radix.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-25)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-24)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-23)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-22)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign%3C%26u8%3E-for-u8)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-%26u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-u8)

[Source](https://doc.rust-lang.org/src/core/fmt/num_buffer.rs.html#26-33)[§](#impl-NumBufferTrait-for-u8)

[Source](https://doc.rust-lang.org/src/core/fmt/num_buffer.rs.html#26-33)[§](#associatedconstant.BUF_SIZE)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Maximum number of digits in decimal base of the implemented integer.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#impl-Octal-for-u8)

[Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#method.fmt-3)

Format unsigned integers in the radix.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#impl-Ord-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-u8)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#impl-PartialOrd-for-u8)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#method.product-1)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product-for-u8)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#method.product)

Takes an iterator and generates `Self` from the elements by multiplying the items.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#61-64)[§](#impl-RangePattern-for-u8)

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#61-64)[§](#associatedconstant.MIN-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#61-64)[§](#associatedconstant.MAX-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#61-64)[§](#method.sub_one)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

A compile-time helper to subtract 1 for exclusive ranges.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-13)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#method.rem-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-12)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#method.rem-3)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#impl-Rem%3CNonZero%3Cu8%3E%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#method.rem)

This operation satisfies `n % d == n - (n / d) * d`, and cannot panic.

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#associatedtype.Output-9)

The resulting type after applying the `%` operator.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-11)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#method.rem-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem-for-u8)

This operation satisfies `n % d == n - (n / d) * d`. The result has the same sign as the left operand.

#### [§](#panics-36)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-10)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616)[§](#method.rem-1)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign%3C%26u8%3E-for-u8)

1.79.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#impl-RemAssign%3CNonZero%3Cu8%3E%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#method.rem_assign)

This operation satisfies `n % d == n - (n / d) * d`, and cannot panic.

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-79)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-78)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-67)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-66)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-71)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-70)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-75)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-74)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-63)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-62)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-83)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-82)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-55)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-54)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-43)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-42)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-47)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-46)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-51)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-50)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-14)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26u8%3E-for-%26Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-131)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-123)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-111)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-115)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-119)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-107)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-127)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-99)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-87)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-91)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-95)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-39)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-103)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-67)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26u8%3E-for-Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-129)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-122)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-110)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-114)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-118)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-106)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-70)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-126)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-98)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-86)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-90)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-94)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-38)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-102)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-59)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-23)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-58)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-22)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-77)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-76)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-65)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-64)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-69)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-68)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-73)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-72)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-61)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-60)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-81)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-80)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-53)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-52)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-41)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-40)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-45)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-44)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-49)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-48)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-12)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Cu8%3E-for-%26Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-130)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-121)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-109)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-113)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-117)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-105)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-125)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-97)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-85)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-89)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-93)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-37)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-101)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-65)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Cu8%3E-for-Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-128)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-120)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-108)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-112)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-116)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-104)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-68)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-124)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-88)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-96)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-84)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-88)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-92)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-100)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-57)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-21)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-56)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl-20)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#impl-Shl-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-36)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#517)[§](#method.shl)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i128%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i32%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i64%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i8%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u128%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u32%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u64%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26usize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci128%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci32%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci64%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci8%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu128%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu32%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu64%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cusize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-175)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-174)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-163)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-162)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-167)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-166)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-171)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-170)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-159)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-158)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-179)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-178)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-151)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-150)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-139)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-138)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-143)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-142)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-147)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-146)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-14)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26u8%3E-for-%26Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-227)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-219)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-207)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-211)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-215)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-203)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-223)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-195)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-183)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-187)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-191)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-135)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-199)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-67)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26u8%3E-for-Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-225)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-218)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-206)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-210)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-214)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-202)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-70)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-222)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-194)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-182)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-186)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-190)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-134)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-198)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-155)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-23)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-154)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-22)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-173)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-172)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-161)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-160)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-165)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-164)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-169)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-168)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-157)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-156)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-177)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-176)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-149)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-148)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-137)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-136)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-141)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-140)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-145)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-144)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-12)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Cu8%3E-for-%26Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-226)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-217)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-205)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-209)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-213)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-201)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-221)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-193)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-181)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-185)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-189)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-133)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-197)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-65)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Cu8%3E-for-Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-224)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-216)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-204)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-208)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-212)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-200)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-68)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-220)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-88)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-192)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-180)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-184)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-188)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-196)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-153)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-21)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-152)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr-20)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#impl-Shr-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-132)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#639)[§](#method.shr)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i128%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i32%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i64%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i8%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u128%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u32%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u64%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26usize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci128%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci32%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci64%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci8%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu128%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu32%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu64%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cusize%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign-for-u8)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1083)[§](#impl-SimdElement-for-u8)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1084)[§](#associatedtype.Mask)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#impl-Step-for-u8)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.forward)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.forward)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.backward)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.backward)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.forward_unchecked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.forward_unchecked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.backward_unchecked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.backward_unchecked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.steps_between)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the bounds on the number of *successor* steps required to get from `start` to `end` like [`Iterator::size_hint()`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.size_hint "method std::iter::Iterator::size_hint"). [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#tymethod.steps_between)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.forward_checked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#tymethod.forward_checked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#434-437)[§](#method.backward_checked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#tymethod.backward_checked)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-21)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-20)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-19)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-18)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3C%26u8%3E-for-Saturating%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3C%26u8%3E-for-Wrapping%3Cu8%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign%3C%26u8%3E-for-u8)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3Cu8%3E-for-Saturating%3Cu8%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3Cu8%3E-for-Wrapping%3Cu8%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign-for-u8)

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#method.sum-1)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum-for-u8)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#204)[§](#method.sum)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.59.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#105)[§](#impl-TryFrom%3Cchar%3E-for-u8)

Maps a `char` with a code point from U+0000 to U+00FF (inclusive) to a byte in `0x00..=0xFF` with the same value, failing if the code point is greater than U+00FF.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#120)[§](#method.try_from-14)

Tries to convert a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8").

##### [§](#examples-152)Examples

```rust
let a = 'ÿ'; // U+00FF
let b = 'Ā'; // U+0100

assert_eq!(u8::try_from(a), Ok(0xFF_u8));
assert!(u8::try_from(b).is_err());
```

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#106)[§](#associatedtype.Error-14)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#impl-TryFrom%3Ci128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#method.try_from-10)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#associatedtype.Error-10)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#395)[§](#impl-TryFrom%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#395)[§](#method.try_from-7)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#395)[§](#associatedtype.Error-7)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#impl-TryFrom%3Ci32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#method.try_from-8)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#associatedtype.Error-8)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#impl-TryFrom%3Ci64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#method.try_from-9)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#associatedtype.Error-9)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#method.try_from-6)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-6)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#method.try_from-12)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-12)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#impl-TryFrom%3Cu128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#method.try_from-4)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#375)[§](#impl-TryFrom%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#375)[§](#method.try_from-1)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#375)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#impl-TryFrom%3Cu32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#method.try_from-2)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#impl-TryFrom%3Cu64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#method.try_from-3)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#562)[§](#impl-TryFrom%3Cu8%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#562)[§](#method.try_from-13)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#562)[§](#associatedtype.Error-13)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu8%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#method.try_from)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-151)Examples

```rust
assert_eq!(0_u8.try_into(), Ok(false));

assert_eq!(1_u8.try_into(), Ok(true));

assert!(<u8 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#387)[§](#impl-TryFrom%3Cu8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#387)[§](#method.try_from-5)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#387)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#impl-TryFrom%3Cusize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#method.try_from-11)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#associatedtype.Error-11)

The type returned in the event of a conversion error.

1.42.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#600)[§](#impl-UpperExp-for-u8)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#impl-UpperHex-for-u8)

[Source](https://doc.rust-lang.org/src/core/fmt/num.rs.html#73)[§](#method.fmt-5)

Format unsigned integers in the radix.

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#69-83)[§](#impl-ZeroablePrimitive-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#69-83)[§](#associatedtype.NonZeroInner)

🔬This is a nightly-only experimental API. (`nonzero_internals`)

A type like `Self` but with a niche that includes zero.

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-u8)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-u8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#40)[§](#impl-FloatToInt%3Cu8%3E-for-f128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu8%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu8%3E-for-f32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#39)[§](#impl-FloatToInt%3Cu8%3E-for-f64)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/cast.rs.html#33)[§](#impl-SimdCast-for-u8)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-u8)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#17)[§](#impl-TrustedStep-for-u8)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-u8)

[§](#impl-Freeze-for-u8)

[§](#impl-RefUnwindSafe-for-u8)

[§](#impl-Send-for-u8)

[§](#impl-Sync-for-u8)

[§](#impl-Unpin-for-u8)

[§](#impl-UnsafeUnpin-for-u8)

[§](#impl-UnwindSafe-for-u8)