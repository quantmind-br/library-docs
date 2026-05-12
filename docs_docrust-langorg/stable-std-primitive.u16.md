---
title: u16 - Rust
url: https://doc.rust-lang.org/stable/std/primitive.u16.html
source: crawler
fetched_at: 2026-05-06T21:28:19.664499635-03:00
rendered_js: false
word_count: 12634
summary: This documentation provides a technical reference for the Rust u16 primitive type, detailing its bitwise manipulation methods, constants, and performance-related operations.
tags:
    - rust
    - primitive-types
    - u16
    - bitwise-operations
    - rust-api-reference
    - integer-types
category: reference
---

Expand description

The 16-bit unsigned integer type.

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1187)[§](#impl-u16)

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

The smallest value that can be represented by this integer type.

##### [§](#examples)Examples

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

The largest value that can be represented by this integer type (216 − 1).

##### [§](#examples-1)Examples

```rust
assert_eq!(u16::MAX, 65535);
```

1.53.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

The size of this integer type in bits.

##### [§](#examples-2)Examples

```rust
assert_eq!(u16::BITS, 16);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the number of ones in the binary representation of `self`.

##### [§](#examples-3)Examples

```rust
let n = 0b01001100u16;
assert_eq!(n.count_ones(), 3);

let max = u16::MAX;
assert_eq!(max.count_ones(), 16);

let zero = 0u16;
assert_eq!(zero.count_ones(), 0);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the number of zeros in the binary representation of `self`.

##### [§](#examples-4)Examples

```rust
let zero = 0u16;
assert_eq!(zero.count_zeros(), 16);

let max = u16::MAX;
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

You might want to use [`Self::count_ones`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.count_ones "method u16::count_ones") instead, or emphasize the type you’re using in the call rather than method syntax:

```rust
let small = 1;
assert_eq!(u16::count_zeros(small), 15);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the number of leading zeros in the binary representation of `self`.

Depending on what you’re doing with the value, you might also be interested in the [`ilog2`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.ilog2 "method u16::ilog2") function which returns a consistent number, even if the type widens.

##### [§](#examples-5)Examples

```rust
let n = u16::MAX >> 2;
assert_eq!(n.leading_zeros(), 2);

let zero = 0u16;
assert_eq!(zero.leading_zeros(), 16);

let max = u16::MAX;
assert_eq!(max.leading_zeros(), 0);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the number of trailing zeros in the binary representation of `self`.

##### [§](#examples-6)Examples

```rust
let n = 0b0101000u16;
assert_eq!(n.trailing_zeros(), 3);

let zero = 0u16;
assert_eq!(zero.trailing_zeros(), 16);

let max = u16::MAX;
assert_eq!(max.trailing_zeros(), 0);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the number of leading ones in the binary representation of `self`.

##### [§](#examples-7)Examples

```rust
let n = !(u16::MAX >> 2);
assert_eq!(n.leading_ones(), 2);

let zero = 0u16;
assert_eq!(zero.leading_ones(), 0);

let max = u16::MAX;
assert_eq!(max.leading_ones(), 16);
```

1.46.0 (const: 1.46.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the number of trailing ones in the binary representation of `self`.

##### [§](#examples-8)Examples

```rust
let n = 0b1010111u16;
assert_eq!(n.trailing_ones(), 3);

let zero = 0u16;
assert_eq!(zero.trailing_ones(), 0);

let max = u16::MAX;
assert_eq!(max.trailing_ones(), 16);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`uint_bit_width` [#142326](https://github.com/rust-lang/rust/issues/142326))

Returns the minimum number of bits required to represent `self`.

This method returns zero if `self` is zero.

##### [§](#examples-9)Examples

```rust
#![feature(uint_bit_width)]

assert_eq!(0_u16.bit_width(), 0);
assert_eq!(0b111_u16.bit_width(), 3);
assert_eq!(0b1110_u16.bit_width(), 4);
assert_eq!(u16::MAX.bit_width(), 16);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Returns `self` with only the most significant bit set, or `0` if the input is `0`.

##### [§](#examples-10)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: u16 = 0b_01100100;

assert_eq!(n.isolate_highest_one(), 0b_01000000);
assert_eq!(0_u16.isolate_highest_one(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`isolate_most_least_significant_one` [#136909](https://github.com/rust-lang/rust/issues/136909))

Returns `self` with only the least significant bit set, or `0` if the input is `0`.

##### [§](#examples-11)Examples

```rust
#![feature(isolate_most_least_significant_one)]

let n: u16 = 0b_01100100;

assert_eq!(n.isolate_lowest_one(), 0b_00000100);
assert_eq!(0_u16.isolate_lowest_one(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Returns the index of the highest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-12)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_u16.highest_one(), None);
assert_eq!(0b1_u16.highest_one(), Some(0));
assert_eq!(0b1_0000_u16.highest_one(), Some(4));
assert_eq!(0b1_1111_u16.highest_one(), Some(4));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`int_lowest_highest_one` [#145203](https://github.com/rust-lang/rust/issues/145203))

Returns the index of the lowest bit set to one in `self`, or `None` if `self` is `0`.

##### [§](#examples-13)Examples

```rust
#![feature(int_lowest_highest_one)]

assert_eq!(0b0_u16.lowest_one(), None);
assert_eq!(0b1_u16.lowest_one(), Some(0));
assert_eq!(0b1_0000_u16.lowest_one(), Some(4));
assert_eq!(0b1_1111_u16.lowest_one(), Some(0));
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the bit pattern of `self` reinterpreted as a signed integer of the same size.

This produces the same result as an `as` cast, but ensures that the bit-width remains the same.

##### [§](#examples-14)Examples

```rust
let n = u16::MAX;

assert_eq!(n.cast_signed(), -1i16);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Shifts the bits to the left by a specified amount, `n`, wrapping the truncated bits to the end of the resulting integer.

`rotate_left(n)` is equivalent to applying `rotate_left(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `<<` shifting operator!

##### [§](#examples-15)Examples

```rust
let n = 0xa003u16;
let m = 0x3a;

assert_eq!(n.rotate_left(4), m);
assert_eq!(n.rotate_left(1024), n);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Shifts the bits to the right by a specified amount, `n`, wrapping the truncated bits to the beginning of the resulting integer.

`rotate_right(n)` is equivalent to applying `rotate_right(1)` a total of `n` times. In particular, a rotation by the number of bits in `self` returns the input value unchanged.

Please note this isn’t the same operation as the `>>` shifting operator!

##### [§](#examples-16)Examples

```rust
let n = 0x3au16;
let m = 0xa003;

assert_eq!(n.rotate_right(4), m);
assert_eq!(n.rotate_right(1024), n);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`funnel_shifts` [#145686](https://github.com/rust-lang/rust/issues/145686))

Performs a left funnel shift (concatenates `self` with `rhs`, with `self` making up the most significant half, then shifts the combined value left by `n`, and most significant half is extracted to produce the result).

Please note this isn’t the same operation as the `<<` shifting operator or [`rotate_left`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.rotate_left "method u16::rotate_left"), although `a.funnel_shl(a, n)` is *equivalent* to `a.rotate_left(n)`.

##### [§](#panics)Panics

If `n` is greater than or equal to the number of bits in `self`

##### [§](#examples-17)Examples

Basic usage:

```rust
#![feature(funnel_shifts)]
let a = 0xa003u16;
let b = 0x2deu16;
let m = 0x30;

assert_eq!(a.funnel_shl(b, 4), m);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`funnel_shifts` [#145686](https://github.com/rust-lang/rust/issues/145686))

Performs a right funnel shift (concatenates `self` and `rhs`, with `self` making up the most significant half, then shifts the combined value right by `n`, and least significant half is extracted to produce the result).

Please note this isn’t the same operation as the `>>` shifting operator or [`rotate_right`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.rotate_right "method u16::rotate_right"), although `a.funnel_shr(a, n)` is *equivalent* to `a.rotate_right(n)`.

##### [§](#panics-1)Panics

If `n` is greater than or equal to the number of bits in `self`

##### [§](#examples-18)Examples

Basic usage:

```rust
#![feature(funnel_shifts)]
let a = 0xa003u16;
let b = 0x2deu16;
let m = 0x302d;

assert_eq!(a.funnel_shr(b, 4), m);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`uint_carryless_mul` [#152080](https://github.com/rust-lang/rust/issues/152080))

Performs a carry-less multiplication, returning the lower bits.

This operation is similar to long multiplication in base 2, except that exclusive or is used instead of addition. The implementation is equivalent to:

```rust
pub fn carryless_mul(lhs: u16, rhs: u16) -> u16{
    let mut retval = 0;
    for i in 0..u16::BITS {
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

let a = 0x9012u16;
let b = 0xcd34u16;

assert_eq!(a.carryless_mul(b), 0x928);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Reverses the byte order of the integer.

##### [§](#examples-20)Examples

```rust
let n = 0x1234u16;
let m = n.swap_bytes();

assert_eq!(m, 0x3412);
```

🔬This is a nightly-only experimental API. (`uint_gather_scatter_bits` [#149069](https://github.com/rust-lang/rust/issues/149069))

Returns an integer with the bit locations specified by `mask` packed contiguously into the least significant bits of the result.

```rust
#![feature(uint_gather_scatter_bits)]
let n: u16 = 0b1011_1100;

assert_eq!(n.extract_bits(0b0010_0100), 0b0000_0011);
assert_eq!(n.extract_bits(0xF0), 0b0000_1011);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`uint_gather_scatter_bits` [#149069](https://github.com/rust-lang/rust/issues/149069))

Returns an integer with the least significant bits of `self` distributed to the bit locations specified by `mask`.

```rust
#![feature(uint_gather_scatter_bits)]
let n: u16 = 0b1010_1101;

assert_eq!(n.deposit_bits(0b0101_0101), 0b0101_0001);
assert_eq!(n.deposit_bits(0xF0), 0b1101_0000);
```

1.37.0 (const: 1.37.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Reverses the order of bits in the integer. The least significant bit becomes the most significant bit, second least-significant bit becomes second most-significant bit, etc.

##### [§](#examples-21)Examples

```rust
let n = 0x1234u16;
let m = n.reverse_bits();

assert_eq!(m, 0x2c48);
assert_eq!(0, 0u16.reverse_bits());
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Converts an integer from big endian to the target’s endianness.

On big endian this is a no-op. On little endian the bytes are swapped.

##### [§](#examples-22)Examples

```rust
let n = 0x1Au16;

if cfg!(target_endian = "big") {
    assert_eq!(u16::from_be(n), n)
} else {
    assert_eq!(u16::from_be(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Converts an integer from little endian to the target’s endianness.

On little endian this is a no-op. On big endian the bytes are swapped.

##### [§](#examples-23)Examples

```rust
let n = 0x1Au16;

if cfg!(target_endian = "little") {
    assert_eq!(u16::from_le(n), n)
} else {
    assert_eq!(u16::from_le(n), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Converts `self` to big endian from the target’s endianness.

On big endian this is a no-op. On little endian the bytes are swapped.

##### [§](#examples-24)Examples

```rust
let n = 0x1Au16;

if cfg!(target_endian = "big") {
    assert_eq!(n.to_be(), n)
} else {
    assert_eq!(n.to_be(), n.swap_bytes())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Converts `self` to little endian from the target’s endianness.

On little endian this is a no-op. On big endian the bytes are swapped.

##### [§](#examples-25)Examples

```rust
let n = 0x1Au16;

if cfg!(target_endian = "little") {
    assert_eq!(n.to_le(), n)
} else {
    assert_eq!(n.to_le(), n.swap_bytes())
}
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked integer addition. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-26)Examples

```rust
assert_eq!((u16::MAX - 2).checked_add(1), Some(u16::MAX - 1));
assert_eq!((u16::MAX - 2).checked_add(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict integer addition. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics-2)Panics

###### [§](#overflow-behavior)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-27)Examples

```rust
assert_eq!((u16::MAX - 2).strict_add(1), u16::MAX - 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = (u16::MAX - 2).strict_add(3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unchecked integer addition. Computes `self + rhs`, assuming overflow cannot occur.

Calling `x.unchecked_add(y)` is semantically equivalent to calling `x.`[`checked_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_add "method u16::checked_add")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.wrapping_add "method u16::wrapping_add").

##### [§](#safety)Safety

This results in undefined behavior when `self + rhs > u16::MAX` or `self + rhs < u16::MIN`, i.e. when [`checked_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_add "method u16::checked_add") would return `None`.

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked addition with a signed integer. Computes `self + rhs`, returning `None` if overflow occurred.

##### [§](#examples-28)Examples

```rust
assert_eq!(1u16.checked_add_signed(2), Some(3));
assert_eq!(1u16.checked_add_signed(-2), None);
assert_eq!((u16::MAX - 2).checked_add_signed(3), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict addition with a signed integer. Computes `self + rhs`, panicking if overflow occurred.

##### [§](#panics-3)Panics

###### [§](#overflow-behavior-1)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-29)Examples

```rust
assert_eq!(1u16.strict_add_signed(2), 3);
```

The following panic because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 1u16.strict_add_signed(-2);
```

[ⓘ](# "This example panics")

```rust
let _ = (u16::MAX - 2).strict_add_signed(3);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked integer subtraction. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-30)Examples

```rust
assert_eq!(1u16.checked_sub(1), Some(0));
assert_eq!(0u16.checked_sub(1), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict integer subtraction. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-4)Panics

###### [§](#overflow-behavior-2)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-31)Examples

```rust
assert_eq!(1u16.strict_sub(1), 0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0u16.strict_sub(1);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unchecked integer subtraction. Computes `self - rhs`, assuming overflow cannot occur.

Calling `x.unchecked_sub(y)` is semantically equivalent to calling `x.`[`checked_sub`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_sub "method u16::checked_sub")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_sub`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.wrapping_sub "method u16::wrapping_sub").

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

This results in undefined behavior when `self - rhs > u16::MAX` or `self - rhs < u16::MIN`, i.e. when [`checked_sub`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_sub "method u16::checked_sub") would return `None`.

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked subtraction with a signed integer. Computes `self - rhs`, returning `None` if overflow occurred.

##### [§](#examples-32)Examples

```rust
assert_eq!(1u16.checked_sub_signed(2), None);
assert_eq!(1u16.checked_sub_signed(-2), Some(3));
assert_eq!((u16::MAX - 2).checked_sub_signed(-4), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict subtraction with a signed integer. Computes `self - rhs`, panicking if overflow occurred.

##### [§](#panics-5)Panics

###### [§](#overflow-behavior-3)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-33)Examples

```rust
assert_eq!(3u16.strict_sub_signed(2), 1);
```

The following panic because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 1u16.strict_sub_signed(2);
```

[ⓘ](# "This example panics")

```rust
let _ = (u16::MAX).strict_sub_signed(-1);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked integer subtraction. Computes `self - rhs` and checks if the result fits into an [`i16`](https://doc.rust-lang.org/stable/std/primitive.i16.html "primitive i16"), returning `None` if overflow occurred.

##### [§](#examples-34)Examples

```rust
assert_eq!(10u16.checked_signed_diff(2), Some(8));
assert_eq!(2u16.checked_signed_diff(10), Some(-8));
assert_eq!(u16::MAX.checked_signed_diff(i16::MAX as u16), None);
assert_eq!((i16::MAX as u16).checked_signed_diff(u16::MAX), Some(i16::MIN));
assert_eq!((i16::MAX as u16 + 1).checked_signed_diff(0), None);
assert_eq!(u16::MAX.checked_signed_diff(u16::MAX), Some(0));
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked integer multiplication. Computes `self * rhs`, returning `None` if overflow occurred.

##### [§](#examples-35)Examples

```rust
assert_eq!(5u16.checked_mul(1), Some(5));
assert_eq!(u16::MAX.checked_mul(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict integer multiplication. Computes `self * rhs`, panicking if overflow occurred.

##### [§](#panics-6)Panics

###### [§](#overflow-behavior-4)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-36)Examples

```rust
assert_eq!(5u16.strict_mul(1), 5);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = u16::MAX.strict_mul(2);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unchecked integer multiplication. Computes `self * rhs`, assuming overflow cannot occur.

Calling `x.unchecked_mul(y)` is semantically equivalent to calling `x.`[`checked_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_mul "method u16::checked_mul")`(y).`[`unwrap_unchecked`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_unchecked)`()`.

If you’re just trying to avoid the panic in debug mode, then **do not** use this. Instead, you’re looking for [`wrapping_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.wrapping_mul "method u16::wrapping_mul").

##### [§](#safety-2)Safety

This results in undefined behavior when `self * rhs > u16::MAX` or `self * rhs < u16::MIN`, i.e. when [`checked_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_mul "method u16::checked_mul") would return `None`.

1.0.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked integer division. Computes `self / rhs`, returning `None` if `rhs == 0`.

##### [§](#examples-37)Examples

```rust
assert_eq!(128u16.checked_div(2), Some(64));
assert_eq!(1u16.checked_div(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict integer division. Computes `self / rhs`.

Strict division on unsigned types is just normal division. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations.

##### [§](#panics-7)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-38)Examples

```rust
assert_eq!(100u16.strict_div(10), 10);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1u16).strict_div(0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked Euclidean division. Computes `self.div_euclid(rhs)`, returning `None` if `rhs == 0`.

##### [§](#examples-39)Examples

```rust
assert_eq!(128u16.checked_div_euclid(2), Some(64));
assert_eq!(1u16.checked_div_euclid(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict Euclidean division. Computes `self.div_euclid(rhs)`.

Strict division on unsigned types is just normal division. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.strict_div(rhs)`.

##### [§](#panics-8)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-40)Examples

```rust
assert_eq!(100u16.strict_div_euclid(10), 10);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = (1u16).strict_div_euclid(0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Checked integer division without remainder. Computes `self / rhs`, returning `None` if `rhs == 0` or if `self % rhs != 0`.

##### [§](#examples-41)Examples

```rust
#![feature(exact_div)]
assert_eq!(64u16.checked_div_exact(2), Some(32));
assert_eq!(64u16.checked_div_exact(32), Some(2));
assert_eq!(64u16.checked_div_exact(0), None);
assert_eq!(65u16.checked_div_exact(2), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Integer division without remainder. Computes `self / rhs`, returning `None` if `self % rhs != 0`.

##### [§](#panics-9)Panics

This function will panic if `rhs == 0`.

##### [§](#examples-42)Examples

```rust
#![feature(exact_div)]
assert_eq!(64u16.div_exact(2), Some(32));
assert_eq!(64u16.div_exact(32), Some(2));
assert_eq!(65u16.div_exact(2), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_div` [#139911](https://github.com/rust-lang/rust/issues/139911))

Unchecked integer division without remainder. Computes `self / rhs`.

##### [§](#safety-3)Safety

This results in undefined behavior when `rhs == 0` or `self % rhs != 0`, i.e. when [`checked_div_exact`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_div_exact "method u16::checked_div_exact") would return `None`.

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked integer remainder. Computes `self % rhs`, returning `None` if `rhs == 0`.

##### [§](#examples-43)Examples

```rust
assert_eq!(5u16.checked_rem(2), Some(1));
assert_eq!(5u16.checked_rem(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict integer remainder. Computes `self % rhs`.

Strict remainder calculation on unsigned types is just the regular remainder calculation. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations.

##### [§](#panics-10)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-44)Examples

```rust
assert_eq!(100u16.strict_rem(10), 0);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5u16.strict_rem(0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked Euclidean modulo. Computes `self.rem_euclid(rhs)`, returning `None` if `rhs == 0`.

##### [§](#examples-45)Examples

```rust
assert_eq!(5u16.checked_rem_euclid(2), Some(1));
assert_eq!(5u16.checked_rem_euclid(0), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict Euclidean modulo. Computes `self.rem_euclid(rhs)`.

Strict modulo calculation on unsigned types is just the regular remainder calculation. There’s no way overflow could ever happen. This function exists so that all operations are accounted for in the strict operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.strict_rem(rhs)`.

##### [§](#panics-11)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-46)Examples

```rust
assert_eq!(100u16.strict_rem_euclid(10), 0);
```

The following panics because of division by zero:

[ⓘ](# "This example panics")

```rust
let _ = 5u16.strict_rem_euclid(0);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`disjoint_bitor` [#135758](https://github.com/rust-lang/rust/issues/135758))

Same value as `self | other`, but UB if any bit position is set in both inputs.

This is a situational micro-optimization for places where you’d rather use addition on some platforms and bitwise or on other platforms, based on exactly which instructions combine better with whatever else you’re doing. Note that there’s no reason to bother using this for places where it’s clear from the operations involved that they can’t overlap. For example, if you’re combining `u16`s into a `u32` with `((a as u32) << 16) | (b as u32)`, that’s fine, as the backend will know those sides of the `|` are disjoint without needing help.

##### [§](#examples-47)Examples

```rust
#![feature(disjoint_bitor)]

// SAFETY: `1` and `4` have no bits in common.
unsafe {
    assert_eq!(1_u16.unchecked_disjoint_bitor(4), 5);
}
```

##### [§](#safety-4)Safety

Requires that `(self & other) == 0`, otherwise it’s immediate UB.

Equivalently, requires that `(self | other) == (self + other)`.

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

This method might not be optimized owing to implementation details; `ilog2` can produce results more efficiently for base 2, and `ilog10` can produce results more efficiently for base 10.

##### [§](#panics-12)Panics

This function will panic if `self` is zero, or if `base` is less than 2.

##### [§](#examples-48)Examples

```rust
assert_eq!(5u16.ilog(5), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the base 2 logarithm of the number, rounded down.

##### [§](#panics-13)Panics

This function will panic if `self` is zero.

##### [§](#examples-49)Examples

```rust
assert_eq!(2u16.ilog2(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the base 10 logarithm of the number, rounded down.

##### [§](#panics-14)Panics

This function will panic if `self` is zero.

##### [§](#example)Example

```rust
assert_eq!(10u16.ilog10(), 1);
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the logarithm of the number with respect to an arbitrary base, rounded down.

Returns `None` if the number is zero, or if the base is not at least 2.

This method might not be optimized owing to implementation details; `checked_ilog2` can produce results more efficiently for base 2, and `checked_ilog10` can produce results more efficiently for base 10.

##### [§](#examples-50)Examples

```rust
assert_eq!(5u16.checked_ilog(5), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the base 2 logarithm of the number, rounded down.

Returns `None` if the number is zero.

##### [§](#examples-51)Examples

```rust
assert_eq!(2u16.checked_ilog2(), Some(1));
```

1.67.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the base 10 logarithm of the number, rounded down.

Returns `None` if the number is zero.

##### [§](#examples-52)Examples

```rust
assert_eq!(10u16.checked_ilog10(), Some(1));
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked negation. Computes `-self`, returning `None` unless `self == 0`.

Note that negating any positive integer will overflow.

##### [§](#examples-53)Examples

```rust
assert_eq!(0u16.checked_neg(), Some(0));
assert_eq!(1u16.checked_neg(), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict negation. Computes `-self`, panicking unless `self == 0`.

Note that negating any positive integer will overflow.

##### [§](#panics-15)Panics

###### [§](#overflow-behavior-5)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-54)Examples

```rust
assert_eq!(0u16.strict_neg(), 0);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 1u16.strict_neg();
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked shift left. Computes `self << rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-55)Examples

```rust
assert_eq!(0x1u16.checked_shl(4), Some(0x10));
assert_eq!(0x10u16.checked_shl(129), None);
assert_eq!(0x10u16.checked_shl(15), Some(0));
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict shift left. Computes `self << rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-16)Panics

###### [§](#overflow-behavior-6)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-56)Examples

```rust
assert_eq!(0x1u16.strict_shl(4), 0x10);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x10u16.strict_shl(129);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unchecked shift left. Computes `self << rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-5)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shl`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_shl "method u16::checked_shl") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unbounded shift left. Computes `self << rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, and `0` is returned.

##### [§](#examples-57)Examples

```rust
assert_eq!(0x1_u16.unbounded_shl(4), 0x10);
assert_eq!(0x1_u16.unbounded_shl(129), 0);
assert_eq!(0b101_u16.unbounded_shl(0), 0b101);
assert_eq!(0b101_u16.unbounded_shl(1), 0b1010);
assert_eq!(0b101_u16.unbounded_shl(2), 0b10100);
assert_eq!(42_u16.unbounded_shl(16), 0);
assert_eq!(42_u16.unbounded_shl(1).unbounded_shl(15), 0);

let start : u16 = 13;
let mut running = start;
for i in 0..160 {
    // The unbounded shift left by i is the same as `<< 1` i times
    assert_eq!(running, start.unbounded_shl(i));
    // Which is not always the case for a wrapping shift
    assert_eq!(running == start.wrapping_shl(i), i < 16);

    running <<= 1;
}
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Exact shift left. Computes `self << rhs` as long as it can be reversed losslessly.

Returns `None` if any non-zero bits would be shifted out or if `rhs` &gt;= `u16::BITS`. Otherwise, returns `Some(self << rhs)`.

##### [§](#examples-58)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x1u16.shl_exact(4), Some(0x10));
assert_eq!(0x1u16.shl_exact(129), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Unchecked exact shift left. Computes `self << rhs`, assuming the operation can be losslessly reversed `rhs` cannot be larger than `u16::BITS`.

##### [§](#safety-6)Safety

This results in undefined behavior when `rhs > self.leading_zeros() || rhs >= u16::BITS` i.e. when [`u16::shl_exact`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.shl_exact "method u16::shl_exact") would return `None`.

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked shift right. Computes `self >> rhs`, returning `None` if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#examples-59)Examples

```rust
assert_eq!(0x10u16.checked_shr(4), Some(0x1));
assert_eq!(0x10u16.checked_shr(129), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict shift right. Computes `self >> rhs`, panicking if `rhs` is larger than or equal to the number of bits in `self`.

##### [§](#panics-17)Panics

###### [§](#overflow-behavior-7)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-60)Examples

```rust
assert_eq!(0x10u16.strict_shr(4), 0x1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = 0x10u16.strict_shr(129);
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unchecked shift right. Computes `self >> rhs`, assuming that `rhs` is less than the number of bits in `self`.

##### [§](#safety-7)Safety

This results in undefined behavior if `rhs` is larger than or equal to the number of bits in `self`, i.e. when [`checked_shr`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.checked_shr "method u16::checked_shr") would return `None`.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Unbounded shift right. Computes `self >> rhs`, without bounding the value of `rhs`.

If `rhs` is larger or equal to the number of bits in `self`, the entire value is shifted out, and `0` is returned.

##### [§](#examples-61)Examples

```rust
assert_eq!(0x10_u16.unbounded_shr(4), 0x1);
assert_eq!(0x10_u16.unbounded_shr(129), 0);
assert_eq!(0b1010_u16.unbounded_shr(0), 0b1010);
assert_eq!(0b1010_u16.unbounded_shr(1), 0b101);
assert_eq!(0b1010_u16.unbounded_shr(2), 0b10);
assert_eq!(42_u16.unbounded_shr(16), 0);
assert_eq!(42_u16.unbounded_shr(1).unbounded_shr(15), 0);

let start = u16::rotate_right(13, 4);
let mut running = start;
for i in 0..160 {
    // The unbounded shift right by i is the same as `>> 1` i times
    assert_eq!(running, start.unbounded_shr(i));
    // Which is not always the case for a wrapping shift
    assert_eq!(running == start.wrapping_shr(i), i < 16);

    running >>= 1;
}
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Exact shift right. Computes `self >> rhs` as long as it can be reversed losslessly.

Returns `None` if any non-zero bits would be shifted out or if `rhs` &gt;= `u16::BITS`. Otherwise, returns `Some(self >> rhs)`.

##### [§](#examples-62)Examples

```rust
#![feature(exact_bitshifts)]

assert_eq!(0x10u16.shr_exact(4), Some(0x1));
assert_eq!(0x10u16.shr_exact(5), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`exact_bitshifts` [#144336](https://github.com/rust-lang/rust/issues/144336))

Unchecked exact shift right. Computes `self >> rhs`, assuming the operation can be losslessly reversed and `rhs` cannot be larger than `u16::BITS`.

##### [§](#safety-8)Safety

This results in undefined behavior when `rhs > self.trailing_zeros() || rhs >= u16::BITS` i.e. when [`u16::shr_exact`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.shr_exact "method u16::shr_exact") would return `None`.

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Checked exponentiation. Computes `self.pow(exp)`, returning `None` if overflow occurred.

##### [§](#examples-63)Examples

```rust
assert_eq!(2u16.checked_pow(5), Some(32));
assert_eq!(0_u16.checked_pow(0), Some(1));
assert_eq!(u16::MAX.checked_pow(2), None);
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Strict exponentiation. Computes `self.pow(exp)`, panicking if overflow occurred.

##### [§](#panics-18)Panics

###### [§](#overflow-behavior-8)Overflow behavior

This function will always panic on overflow, regardless of whether overflow checks are enabled.

##### [§](#examples-64)Examples

```rust
assert_eq!(2u16.strict_pow(5), 32);
assert_eq!(0_u16.strict_pow(0), 1);
```

The following panics because of overflow:

[ⓘ](# "This example panics")

```rust
let _ = u16::MAX.strict_pow(2);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating integer addition. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-65)Examples

```rust
assert_eq!(100u16.saturating_add(1), 101);
assert_eq!(u16::MAX.saturating_add(127), u16::MAX);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating addition with a signed integer. Computes `self + rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-66)Examples

```rust
assert_eq!(1u16.saturating_add_signed(2), 3);
assert_eq!(1u16.saturating_add_signed(-2), 0);
assert_eq!((u16::MAX - 2).saturating_add_signed(4), u16::MAX);
```

1.0.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating integer subtraction. Computes `self - rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-67)Examples

```rust
assert_eq!(100u16.saturating_sub(27), 73);
assert_eq!(13u16.saturating_sub(127), 0);
```

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating integer subtraction. Computes `self` - `rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-68)Examples

```rust
assert_eq!(1u16.saturating_sub_signed(2), 0);
assert_eq!(1u16.saturating_sub_signed(-2), 3);
assert_eq!((u16::MAX - 2).saturating_sub_signed(-4), u16::MAX);
```

1.7.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating integer multiplication. Computes `self * rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-69)Examples

```rust
assert_eq!(2u16.saturating_mul(10), 20);
assert_eq!((u16::MAX).saturating_mul(10), u16::MAX);
```

1.58.0 (const: 1.58.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating integer division. Computes `self / rhs`, saturating at the numeric bounds instead of overflowing.

##### [§](#panics-19)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-70)Examples

```rust
assert_eq!(5u16.saturating_div(2), 2);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Saturating integer exponentiation. Computes `self.pow(exp)`, saturating at the numeric bounds instead of overflowing.

##### [§](#examples-71)Examples

```rust
assert_eq!(4u16.saturating_pow(3), 64);
assert_eq!(0_u16.saturating_pow(0), 1);
assert_eq!(u16::MAX.saturating_pow(2), u16::MAX);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) addition. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-72)Examples

```rust
assert_eq!(200u16.wrapping_add(55), 255);
assert_eq!(200u16.wrapping_add(u16::MAX), 199);
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) addition with a signed integer. Computes `self + rhs`, wrapping around at the boundary of the type.

##### [§](#examples-73)Examples

```rust
assert_eq!(1u16.wrapping_add_signed(2), 3);
assert_eq!(1u16.wrapping_add_signed(-2), u16::MAX);
assert_eq!((u16::MAX - 2).wrapping_add_signed(4), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) subtraction. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-74)Examples

```rust
assert_eq!(100u16.wrapping_sub(100), 0);
assert_eq!(100u16.wrapping_sub(u16::MAX), 101);
```

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) subtraction with a signed integer. Computes `self - rhs`, wrapping around at the boundary of the type.

##### [§](#examples-75)Examples

```rust
assert_eq!(1u16.wrapping_sub_signed(2), u16::MAX);
assert_eq!(1u16.wrapping_sub_signed(-2), 3);
assert_eq!((u16::MAX - 2).wrapping_sub_signed(-4), 1);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) multiplication. Computes `self * rhs`, wrapping around at the boundary of the type.

##### [§](#examples-76)Examples

Please note that this example is shared among integer types, which is why `u8` is used.

```rust
assert_eq!(10u8.wrapping_mul(12), 120);
assert_eq!(25u8.wrapping_mul(12), 44);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) division. Computes `self / rhs`.

Wrapped division on unsigned types is just normal division. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations.

##### [§](#panics-20)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-77)Examples

```rust
assert_eq!(100u16.wrapping_div(10), 10);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping Euclidean division. Computes `self.div_euclid(rhs)`.

Wrapped division on unsigned types is just normal division. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.wrapping_div(rhs)`.

##### [§](#panics-21)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-78)Examples

```rust
assert_eq!(100u16.wrapping_div_euclid(10), 10);
```

1.2.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) remainder. Computes `self % rhs`.

Wrapped remainder calculation on unsigned types is just the regular remainder calculation. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations.

##### [§](#panics-22)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-79)Examples

```rust
assert_eq!(100u16.wrapping_rem(10), 0);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping Euclidean modulo. Computes `self.rem_euclid(rhs)`.

Wrapped modulo calculation on unsigned types is just the regular remainder calculation. There’s no way wrapping could ever happen. This function exists so that all operations are accounted for in the wrapping operations. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.wrapping_rem(rhs)`.

##### [§](#panics-23)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-80)Examples

```rust
assert_eq!(100u16.wrapping_rem_euclid(10), 0);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) negation. Computes `-self`, wrapping around at the boundary of the type.

Since unsigned types do not have negative equivalents all applications of this function will wrap (except for `-0`). For values smaller than the corresponding signed type’s maximum the result is the same as casting the corresponding signed value. Any larger values are equivalent to `MAX + 1 - (val - MAX - 1)` where `MAX` is the corresponding signed type’s maximum.

##### [§](#examples-81)Examples

```rust
assert_eq!(0_u16.wrapping_neg(), 0);
assert_eq!(u16::MAX.wrapping_neg(), 1);
assert_eq!(13_u16.wrapping_neg(), (!13) + 1);
assert_eq!(42_u16.wrapping_neg(), !(42 - 1));
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Panic-free bitwise shift-left; yields `self << mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `<<` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shl`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.unbounded_shl "method u16::unbounded_shl") which has nicer behaviour.

Note that this is *not* the same as a rotate-left; the RHS of a wrapping shift-left is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_left`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.rotate_left "method u16::rotate_left") function, which may be what you want instead.

##### [§](#examples-82)Examples

```rust
assert_eq!(1_u16.wrapping_shl(7), 128);
assert_eq!(0b101_u16.wrapping_shl(0), 0b101);
assert_eq!(0b101_u16.wrapping_shl(1), 0b1010);
assert_eq!(0b101_u16.wrapping_shl(2), 0b10100);
assert_eq!(u16::MAX.wrapping_shl(2), u16::MAX - 3);
assert_eq!(42_u16.wrapping_shl(16), 42);
assert_eq!(42_u16.wrapping_shl(1).wrapping_shl(15), 0);
assert_eq!(1_u16.wrapping_shl(128), 1);
assert_eq!(5_u16.wrapping_shl(1025), 10);
```

1.2.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Panic-free bitwise shift-right; yields `self >> mask(rhs)`, where `mask` removes any high-order bits of `rhs` that would cause the shift to exceed the bitwidth of the type.

Beware that, unlike most other `wrapping_*` methods on integers, this does *not* give the same result as doing the shift in infinite precision then truncating as needed. The behaviour matches what shift instructions do on many processors, and is what the `>>` operator does when overflow checks are disabled, but numerically it’s weird. Consider, instead, using [`Self::unbounded_shr`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.unbounded_shr "method u16::unbounded_shr") which has nicer behaviour.

Note that this is *not* the same as a rotate-right; the RHS of a wrapping shift-right is restricted to the range of the type, rather than the bits shifted out of the LHS being returned to the other end. The primitive integer types all implement a [`rotate_right`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.rotate_right "method u16::rotate_right") function, which may be what you want instead.

##### [§](#examples-83)Examples

```rust
assert_eq!(128_u16.wrapping_shr(7), 1);
assert_eq!(0b1010_u16.wrapping_shr(0), 0b1010);
assert_eq!(0b1010_u16.wrapping_shr(1), 0b101);
assert_eq!(0b1010_u16.wrapping_shr(2), 0b10);
assert_eq!(u16::MAX.wrapping_shr(1), i16::MAX.cast_unsigned());
assert_eq!(42_u16.wrapping_shr(16), 42);
assert_eq!(42_u16.wrapping_shr(1).wrapping_shr(15), 0);
assert_eq!(128_u16.wrapping_shr(128), 128);
assert_eq!(10_u16.wrapping_shr(1025), 5);
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Wrapping (modular) exponentiation. Computes `self.pow(exp)`, wrapping around at the boundary of the type.

##### [§](#examples-84)Examples

```rust
assert_eq!(3u16.wrapping_pow(5), 243);
assert_eq!(3u8.wrapping_pow(6), 217);
assert_eq!(0_u16.wrapping_pow(0), 1);
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates `self` + `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-85)Examples

```rust
assert_eq!(5u16.overflowing_add(2), (7, false));
assert_eq!(u16::MAX.overflowing_add(1), (0, true));
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates `self` + `rhs` + `carry` and returns a tuple containing the sum and the output carry (in that order).

Performs “ternary addition” of two integer operands and a carry-in bit, and returns an output integer and a carry-out bit. This allows chaining together multiple additions to create a wider addition, and can be useful for bignum addition.

This can be thought of as a 16-bit “full adder”, in the electronics sense.

If the input carry is false, this method is equivalent to [`overflowing_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.overflowing_add "method u16::overflowing_add"), and the output carry is equal to the overflow flag. Note that although carry and overflow flags are similar for unsigned integers, they are different for signed integers.

##### [§](#examples-86)Examples

```rust
//    3  MAX    (a = 3 × 2^16 + 2^16 - 1)
// +  5    7    (b = 5 × 2^16 + 7)
// ---------
//    9    6    (sum = 9 × 2^16 + 6)

let (a1, a0): (u16, u16) = (3, u16::MAX);
let (b1, b0): (u16, u16) = (5, 7);
let carry0 = false;

let (sum0, carry1) = a0.carrying_add(b0, carry0);
assert_eq!(carry1, true);
let (sum1, carry2) = a1.carrying_add(b1, carry1);
assert_eq!(carry2, false);

assert_eq!((sum1, sum0), (9, 6));
```

1.66.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates `self` + `rhs` with a signed `rhs`.

Returns a tuple of the addition along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-87)Examples

```rust
assert_eq!(1u16.overflowing_add_signed(2), (3, false));
assert_eq!(1u16.overflowing_add_signed(-2), (u16::MAX, true));
assert_eq!((u16::MAX - 2).overflowing_add_signed(4), (1, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates `self` - `rhs`.

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-88)Examples

```rust
assert_eq!(5u16.overflowing_sub(2), (3, false));
assert_eq!(0u16.overflowing_sub(1), (u16::MAX, true));
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates `self` − `rhs` − `borrow` and returns a tuple containing the difference and the output borrow.

Performs “ternary subtraction” by subtracting both an integer operand and a borrow-in bit from `self`, and returns an output integer and a borrow-out bit. This allows chaining together multiple subtractions to create a wider subtraction, and can be useful for bignum subtraction.

##### [§](#examples-89)Examples

```rust
//    9    6    (a = 9 × 2^16 + 6)
// -  5    7    (b = 5 × 2^16 + 7)
// ---------
//    3  MAX    (diff = 3 × 2^16 + 2^16 - 1)

let (a1, a0): (u16, u16) = (9, 6);
let (b1, b0): (u16, u16) = (5, 7);
let borrow0 = false;

let (diff0, borrow1) = a0.borrowing_sub(b0, borrow0);
assert_eq!(borrow1, true);
let (diff1, borrow2) = a1.borrowing_sub(b1, borrow1);
assert_eq!(borrow2, false);

assert_eq!((diff1, diff0), (3, u16::MAX));
```

1.90.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates `self` - `rhs` with a signed `rhs`

Returns a tuple of the subtraction along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

##### [§](#examples-90)Examples

```rust
assert_eq!(1u16.overflowing_sub_signed(2), (u16::MAX, true));
assert_eq!(1u16.overflowing_sub_signed(-2), (3, false));
assert_eq!((u16::MAX - 2).overflowing_sub_signed(-4), (1, true));
```

1.60.0 (const: 1.60.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Computes the absolute difference between `self` and `other`.

##### [§](#examples-91)Examples

```rust
assert_eq!(100u16.abs_diff(80), 20u16);
assert_eq!(100u16.abs_diff(110), 10u16);
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the multiplication of `self` and `rhs`.

Returns a tuple of the multiplication along with a boolean indicating whether an arithmetic overflow would occur. If an overflow would have occurred then the wrapped value is returned.

If you want the *value* of the overflow, rather than just *whether* an overflow occurred, see [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.carrying_mul "method u16::carrying_mul").

##### [§](#examples-92)Examples

Please note that this example is shared among integer types, which is why `u32` is used.

```rust
assert_eq!(5u32.overflowing_mul(2), (10, false));
assert_eq!(1_000_000_000u32.overflowing_mul(10), (1410065408, true));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`widening_mul` [#152016](https://github.com/rust-lang/rust/issues/152016))

Calculates the complete double-width product `self * rhs`.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order. As such, `a.widening_mul(b).0` produces the same result as `a.wrapping_mul(b)`.

If you also need to add a value and carry to the wide result, then you want [`Self::carrying_mul_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.carrying_mul_add "method u16::carrying_mul_add") instead.

If you also need to add a carry to the wide result, then you want [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.carrying_mul "method u16::carrying_mul") instead.

If you just want to know *whether* the multiplication overflowed, then you want [`Self::overflowing_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.overflowing_mul "method u16::overflowing_mul") instead.

##### [§](#examples-93)Examples

```rust
#![feature(widening_mul)]
assert_eq!(5_u16.widening_mul(7), (35, 0));
assert_eq!(u16::MAX.widening_mul(u16::MAX), (1, u16::MAX - 1));
```

Compared to other `*_mul` methods:

```rust
#![feature(widening_mul)]
assert_eq!(u16::widening_mul(1 << 15, 6), (0, 3));
assert_eq!(u16::overflowing_mul(1 << 15, 6), (0, true));
assert_eq!(u16::wrapping_mul(1 << 15, 6), 0);
assert_eq!(u16::checked_mul(1 << 15, 6), None);
```

Please note that this example is shared among integer types, which is why `u32` is used.

```rust
#![feature(widening_mul)]
assert_eq!(5u32.widening_mul(2), (10, 0));
assert_eq!(1_000_000_000u32.widening_mul(10), (1410065408, 2));
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the “full multiplication” `self * rhs + carry` without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you also need to add a value, then use [`Self::carrying_mul_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.carrying_mul_add "method u16::carrying_mul_add").

##### [§](#examples-94)Examples

Please note that this example is shared among integer types, which is why `u32` is used.

```rust
assert_eq!(5u32.carrying_mul(2, 0), (10, 0));
assert_eq!(5u32.carrying_mul(2, 10), (20, 0));
assert_eq!(1_000_000_000u32.carrying_mul(10, 0), (1410065408, 2));
assert_eq!(1_000_000_000u32.carrying_mul(10, 10), (1410065418, 2));
assert_eq!(u16::MAX.carrying_mul(u16::MAX, u16::MAX), (0, u16::MAX));
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

If `carry` is zero, this is similar to [`overflowing_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.overflowing_mul "method u16::overflowing_mul"), except that it gives the value of the overflow instead of just whether one happened:

```rust
#![feature(const_unsigned_bigint_helpers)]
let r = u8::carrying_mul(7, 13, 0);
assert_eq!((r.0, r.1 != 0), u8::overflowing_mul(7, 13));
let r = u8::carrying_mul(13, 42, 0);
assert_eq!((r.0, r.1 != 0), u8::overflowing_mul(13, 42));
```

The value of the first field in the returned tuple matches what you’d get by combining the [`wrapping_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.wrapping_mul "method u16::wrapping_mul") and [`wrapping_add`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.wrapping_add "method u16::wrapping_add") methods:

```rust
#![feature(const_unsigned_bigint_helpers)]
assert_eq!(
    789_u16.carrying_mul(456, 123).0,
    789_u16.wrapping_mul(456).wrapping_add(123),
);
```

1.91.0 (const: [unstable](https://github.com/rust-lang/rust/issues/152015 "Tracking issue for const_unsigned_bigint_helpers")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the “full multiplication” `self * rhs + carry + add`.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

This cannot overflow, as the double-width result has exactly enough space for the largest possible result. This is equivalent to how, in decimal, 9 × 9 + 9 + 9 = 81 + 18 = 99 = 9×10⁰ + 9×10¹ = 10² - 1.

Performs “long multiplication” which takes in an extra amount to add, and may return an additional amount of overflow. This allows for chaining together multiple multiplications to create “big integers” which represent larger values.

If you don’t need the `add` part, then you can use [`Self::carrying_mul`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.carrying_mul "method u16::carrying_mul") instead.

##### [§](#examples-95)Examples

Please note that this example is shared between integer types, which explains why `u32` is used here.

```rust
assert_eq!(5u32.carrying_mul_add(2, 0, 0), (10, 0));
assert_eq!(5u32.carrying_mul_add(2, 10, 10), (30, 0));
assert_eq!(1_000_000_000u32.carrying_mul_add(10, 0, 0), (1410065408, 2));
assert_eq!(1_000_000_000u32.carrying_mul_add(10, 10, 10), (1410065428, 2));
assert_eq!(u16::MAX.carrying_mul_add(u16::MAX, u16::MAX, u16::MAX), (u16::MAX, u16::MAX));
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

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the divisor when `self` is divided by `rhs`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`.

##### [§](#panics-24)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-96)Examples

```rust
assert_eq!(5u16.overflowing_div(2), (2, false));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the quotient of Euclidean division `self.div_euclid(rhs)`.

Returns a tuple of the divisor along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`. Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self.overflowing_div(rhs)`.

##### [§](#panics-25)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-97)Examples

```rust
assert_eq!(5u16.overflowing_div_euclid(2), (2, false));
```

1.7.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the remainder when `self` is divided by `rhs`.

Returns a tuple of the remainder after dividing along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`.

##### [§](#panics-26)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-98)Examples

```rust
assert_eq!(5u16.overflowing_rem(2), (1, false));
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the remainder `self.rem_euclid(rhs)` as if by Euclidean division.

Returns a tuple of the modulo after dividing along with a boolean indicating whether an arithmetic overflow would occur. Note that for unsigned integers overflow never occurs, so the second value is always `false`. Since, for the positive integers, all common definitions of division are equal, this operation is exactly equal to `self.overflowing_rem(rhs)`.

##### [§](#panics-27)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-99)Examples

```rust
assert_eq!(5u16.overflowing_rem_euclid(2), (1, false));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Negates self in an overflowing fashion.

Returns `!self + 1` using wrapping operations to return the value that represents the negation of this unsigned value. Note that for positive unsigned values overflow always occurs, but negating 0 does not overflow.

##### [§](#examples-100)Examples

```rust
assert_eq!(0u16.overflowing_neg(), (0, false));
assert_eq!(2u16.overflowing_neg(), (-2i32 as u16, true));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Shifts self left by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-101)Examples

```rust
assert_eq!(0x1u16.overflowing_shl(4), (0x10, false));
assert_eq!(0x1u16.overflowing_shl(132), (0x10, true));
assert_eq!(0x10u16.overflowing_shl(15), (0, false));
```

1.7.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Shifts self right by `rhs` bits.

Returns a tuple of the shifted version of self along with a boolean indicating whether the shift value was larger than or equal to the number of bits. If the shift value is too large, then value is masked (N-1) where N is the number of bits, and this value is then used to perform the shift.

##### [§](#examples-102)Examples

```rust
assert_eq!(0x10u16.overflowing_shr(4), (0x1, false));
assert_eq!(0x10u16.overflowing_shr(132), (0x1, true));
```

1.34.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Raises self to the power of `exp`, using exponentiation by squaring.

Returns a tuple of the exponentiation along with a bool indicating whether an overflow happened.

##### [§](#examples-103)Examples

```rust
assert_eq!(3u16.overflowing_pow(5), (243, false));
assert_eq!(0_u16.overflowing_pow(0), (1, false));
assert_eq!(3u8.overflowing_pow(6), (217, true));
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Raises self to the power of `exp`, using exponentiation by squaring.

##### [§](#examples-104)Examples

```rust
assert_eq!(2u16.pow(5), 32);
assert_eq!(0_u16.pow(0), 1);
```

1.84.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the square root of the number, rounded down.

##### [§](#examples-105)Examples

```rust
assert_eq!(10u16.isqrt(), 3);
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Performs Euclidean division.

Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self / rhs`.

##### [§](#panics-28)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-106)Examples

```rust
assert_eq!(7u16.div_euclid(4), 1); // or any other integer type
```

1.38.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the least remainder of `self` when divided by `rhs`.

Since, for the positive integers, all common definitions of division are equal, this is exactly equal to `self % rhs`.

##### [§](#panics-29)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-107)Examples

```rust
assert_eq!(7u16.rem_euclid(4), 3); // or any other integer type
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`int_roundings` [#88581](https://github.com/rust-lang/rust/issues/88581))

Calculates the quotient of `self` and `rhs`, rounding the result towards negative infinity.

This is the same as performing `self / rhs` for all unsigned integers.

##### [§](#panics-30)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-108)Examples

```rust
#![feature(int_roundings)]
assert_eq!(7_u16.div_floor(4), 1);
```

1.73.0 (const: 1.73.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the quotient of `self` and `rhs`, rounding the result towards positive infinity.

##### [§](#panics-31)Panics

This function will panic if `rhs` is zero.

##### [§](#examples-109)Examples

```rust
assert_eq!(7_u16.div_ceil(4), 2);
```

1.73.0 (const: 1.73.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`.

##### [§](#panics-32)Panics

This function will panic if `rhs` is zero.

###### [§](#overflow-behavior-9)Overflow behavior

On overflow, this function will panic if overflow checks are enabled (default in debug mode) and wrap if overflow checks are disabled (default in release mode).

##### [§](#examples-110)Examples

```rust
assert_eq!(16_u16.next_multiple_of(8), 16);
assert_eq!(23_u16.next_multiple_of(8), 24);
```

1.73.0 (const: 1.73.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Calculates the smallest value greater than or equal to `self` that is a multiple of `rhs`. Returns `None` if `rhs` is zero or the operation would result in overflow.

##### [§](#examples-111)Examples

```rust
assert_eq!(16_u16.checked_next_multiple_of(8), Some(16));
assert_eq!(23_u16.checked_next_multiple_of(8), Some(24));
assert_eq!(1_u16.checked_next_multiple_of(0), None);
assert_eq!(u16::MAX.checked_next_multiple_of(2), None);
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns `true` if `self` is an integer multiple of `rhs`, and false otherwise.

This function is equivalent to `self % rhs == 0`, except that it will not panic for `rhs == 0`. Instead, `0.is_multiple_of(0) == true`, and for any non-zero `n`, `n.is_multiple_of(0) == false`.

##### [§](#examples-112)Examples

```rust
assert!(6_u16.is_multiple_of(2));
assert!(!5_u16.is_multiple_of(2));

assert!(0_u16.is_multiple_of(0));
assert!(!6_u16.is_multiple_of(0));
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns `true` if and only if `self == 2^k` for some unsigned integer `k`.

##### [§](#examples-113)Examples

```rust
assert!(16u16.is_power_of_two());
assert!(!10u16.is_power_of_two());
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the smallest power of two greater than or equal to `self`.

When return value overflows (i.e., `self > (1 << (N-1))` for type `uN`), it panics in debug mode and the return value is wrapped to 0 in release mode (the only situation in which this method can return 0).

##### [§](#examples-114)Examples

```rust
assert_eq!(2u16.next_power_of_two(), 2);
assert_eq!(3u16.next_power_of_two(), 4);
assert_eq!(0u16.next_power_of_two(), 1);
```

1.0.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the smallest power of two greater than or equal to `self`. If the next power of two is greater than the type’s maximum value, `None` is returned, otherwise the power of two is wrapped in `Some`.

##### [§](#examples-115)Examples

```rust
assert_eq!(2u16.checked_next_power_of_two(), Some(2));
assert_eq!(3u16.checked_next_power_of_two(), Some(4));
assert_eq!(u16::MAX.checked_next_power_of_two(), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

🔬This is a nightly-only experimental API. (`wrapping_next_power_of_two` [#32463](https://github.com/rust-lang/rust/issues/32463))

Returns the smallest power of two greater than or equal to `n`. If the next power of two is greater than the type’s maximum value, the return value is wrapped to `0`.

##### [§](#examples-116)Examples

```rust
#![feature(wrapping_next_power_of_two)]

assert_eq!(2u16.wrapping_next_power_of_two(), 2);
assert_eq!(3u16.wrapping_next_power_of_two(), 4);
assert_eq!(u16::MAX.wrapping_next_power_of_two(), 0);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the memory representation of this integer as a byte array in big-endian (network) byte order.

##### [§](#examples-117)Examples

```rust
let bytes = 0x1234u16.to_be_bytes();
assert_eq!(bytes, [0x12, 0x34]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the memory representation of this integer as a byte array in little-endian byte order.

##### [§](#examples-118)Examples

```rust
let bytes = 0x1234u16.to_le_bytes();
assert_eq!(bytes, [0x34, 0x12]);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Returns the memory representation of this integer as a byte array in native byte order.

As the target platform’s native endianness is used, portable code should use [`to_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.to_be_bytes "method u16::to_be_bytes") or [`to_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.to_le_bytes "method u16::to_le_bytes"), as appropriate, instead.

##### [§](#examples-119)Examples

```rust
let bytes = 0x1234u16.to_ne_bytes();
assert_eq!(
    bytes,
    if cfg!(target_endian = "big") {
        [0x12, 0x34]
    } else {
        [0x34, 0x12]
    }
);
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Creates a native endian integer value from its representation as a byte array in big endian.

##### [§](#examples-120)Examples

```rust
let value = u16::from_be_bytes([0x12, 0x34]);
assert_eq!(value, 0x1234);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_be_u16(input: &mut &[u8]) -> u16 {
    let (int_bytes, rest) = input.split_at(size_of::<u16>());
    *input = rest;
    u16::from_be_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Creates a native endian integer value from its representation as a byte array in little endian.

##### [§](#examples-121)Examples

```rust
let value = u16::from_le_bytes([0x34, 0x12]);
assert_eq!(value, 0x1234);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_le_u16(input: &mut &[u8]) -> u16 {
    let (int_bytes, rest) = input.split_at(size_of::<u16>());
    *input = rest;
    u16::from_le_bytes(int_bytes.try_into().unwrap())
}
```

1.32.0 (const: 1.44.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

Creates a native endian integer value from its memory representation as a byte array in native endianness.

As the target platform’s native endianness is used, portable code likely wants to use [`from_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.from_be_bytes "associated function u16::from_be_bytes") or [`from_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.from_le_bytes "associated function u16::from_le_bytes"), as appropriate instead.

##### [§](#examples-122)Examples

```rust
let value = u16::from_ne_bytes(if cfg!(target_endian = "big") {
    [0x12, 0x34]
} else {
    [0x34, 0x12]
});
assert_eq!(value, 0x1234);
```

When starting from a slice rather than an array, fallible conversion APIs can be used:

```rust
fn read_ne_u16(input: &mut &[u8]) -> u16 {
    let (int_bytes, rest) = input.split_at(size_of::<u16>());
    *input = rest;
    u16::from_ne_bytes(int_bytes.try_into().unwrap())
}
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

👎Deprecating in a future version: replaced by the `MIN` associated constant on this type

New code should prefer to use [`u16::MIN`](https://doc.rust-lang.org/stable/std/primitive.u16.html#associatedconstant.MIN "associated constant u16::MIN") instead.

Returns the smallest value that can be represented by this integer type.

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1188-1212)

👎Deprecating in a future version: replaced by the `MAX` associated constant on this type

New code should prefer to use [`u16::MAX`](https://doc.rust-lang.org/stable/std/primitive.u16.html#associatedconstant.MAX "associated constant u16::MAX") instead.

Returns the largest value that can be represented by this integer type.

1.85.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1213)

Calculates the midpoint (average) between `self` and `rhs`.

`midpoint(a, b)` is `(a + b) / 2` as if it were performed in a sufficiently-large unsigned integral type. This implies that the result is always rounded towards zero and that no overflow will ever occur.

##### [§](#examples-123)Examples

```rust
assert_eq!(0u16.midpoint(4), 2);
assert_eq!(1u16.midpoint(4), 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1214)

🔬This is a nightly-only experimental API. (`uint_carryless_mul` [#152080](https://github.com/rust-lang/rust/issues/152080))

Performs a widening carry-less multiplication.

##### [§](#examples-124)Examples

```rust
#![feature(uint_carryless_mul)]

assert_eq!(u16::MAX.widening_carryless_mul(u16::MAX), u32::MAX / 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1215)

🔬This is a nightly-only experimental API. (`uint_carryless_mul` [#152080](https://github.com/rust-lang/rust/issues/152080))

Calculates the “full carryless multiplication” without the possibility to overflow.

This returns the low-order (wrapping) bits and the high-order (overflow) bits of the result as two separate values, in that order.

##### [§](#examples-125)Examples

Please note that this example is shared among integer types, which is why `u8` is used.

```rust
#![feature(uint_carryless_mul)]

assert_eq!(0b1000_0000u8.carrying_carryless_mul(0b1000_0000, 0b0000), (0, 0b0100_0000));
assert_eq!(0b1000_0000u8.carrying_carryless_mul(0b1000_0000, 0b1111), (0b1111, 0b0100_0000));
assert_eq!(u16::MAX.carrying_carryless_mul(u16::MAX, u16::MAX), (!(u16::MAX / 3), u16::MAX / 3));
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1237)

🔬This is a nightly-only experimental API. (`utf16_extra` [#94919](https://github.com/rust-lang/rust/issues/94919))

Checks if the value is a Unicode surrogate code point, which are disallowed values for [`char`](https://doc.rust-lang.org/stable/std/primitive.char.html "primitive char").

##### [§](#examples-126)Examples

```rust
#![feature(utf16_extra)]

let low_non_surrogate = 0xA000u16;
let low_surrogate = 0xD800u16;
let high_surrogate = 0xDC00u16;
let high_non_surrogate = 0xE000u16;

assert!(!low_non_surrogate.is_utf16_surrogate());
assert!(low_surrogate.is_utf16_surrogate());
assert!(high_surrogate.is_utf16_surrogate());
assert!(!high_non_surrogate.is_utf16_surrogate());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)[§](#impl-u16-1)

1.0.0 (const: 1.82.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)

Parses an integer from a string slice with digits in a given base.

The string is expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

Digits are a subset of these characters, depending on `radix`:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#panics-33)Panics

This function panics if `radix` is not in the range from 2 to 36.

##### [§](#see-also)See also

If the string to be parsed is in base 10 (decimal), [`from_str`](#method.from_str) or [`str::parse`](https://doc.rust-lang.org/stable/std/primitive.str.html#method.parse) can also be used.

##### [§](#examples-127)Examples

```rust
assert_eq!(u16::from_str_radix("A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(u16::from_str_radix("1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with decimal digits.

The characters are expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#examples-128)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(u16::from_ascii(b"+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(u16::from_ascii(b"1 ").is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)

🔬This is a nightly-only experimental API. (`int_from_ascii` [#134821](https://github.com/rust-lang/rust/issues/134821))

Parses an integer from an ASCII-byte slice with digits in a given base.

The characters are expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

Digits are a subset of these characters, depending on `radix`:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#panics-34)Panics

This function panics if `radix` is not in the range from 2 to 36.

##### [§](#examples-129)Examples

```rust
#![feature(int_from_ascii)]

assert_eq!(u16::from_ascii_radix(b"A", 16), Ok(10));
```

Trailing space returns error:

```rust
assert!(u16::from_ascii_radix(b"1 ", 10).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)[§](#impl-u16-2)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Allows users to write an integer (in signed decimal format) into a variable `buf` of type [`NumBuffer`](https://doc.rust-lang.org/stable/core/fmt/num_buffer/struct.NumBuffer.html "struct core::fmt::num_buffer::NumBuffer") that is passed by the caller by mutable reference.

##### [§](#examples-130)Examples

```rust
#![feature(int_format_into)]
use core::fmt::NumBuffer;

let n = 0u16;
let mut buf = NumBuffer::new();
assert_eq!(n.format_into(&mut buf), "0");

let n1 = 32u16;
assert_eq!(n1.format_into(&mut buf), "32");

let n2 = u16 :: MAX;
assert_eq!(n2.format_into(&mut buf), u16 :: MAX.to_string());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-17)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-16)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-15)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-14)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign%3C%26u16%3E-for-u16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-AddAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-AddAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#301)[§](#impl-AtomicPrimitive-for-u16)

Available on **`target_has_atomic_load_store=16`** only.

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#301)[§](#associatedtype.AtomicInner)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-Binary-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-2)

Format unsigned integers in the radix.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-35)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-34)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-33)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-32)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign%3C%26u16%3E-for-u16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitAndAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitAndAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-3)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-2)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-1)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign%3C%26u16%3E-for-u16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitOrAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitOrAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-31)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-30)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-29)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-28)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign%3C%26u16%3E-for-u16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-BitXorAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-BitXorAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#impl-CarryingMulAdd-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#associatedtype.Unsigned)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#34-45)[§](#method.carrying_mul_add-1)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#253-255)[§](#impl-CarrylessMul-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#253-255)[§](#method.carryless_mul-1)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::carryless_mul`](https://doc.rust-lang.org/stable/std/intrinsics/fn.carryless_mul.html "fn std::intrinsics::carryless_mul"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-u16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#589-592)[§](#impl-Debug-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#171)[§](#impl-Default-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#171)[§](#method.default)

Returns the default value of `0`

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#impl-DisjointBitOr-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#method.disjoint_bitor)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::disjoint_bitor`](https://doc.rust-lang.org/stable/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#599)[§](#impl-Display-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#51)[§](#impl-Distribution%3Cu16%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#51)[§](#method.sample)

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Samples a random value from the distribution, using the specified random source.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-8)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-7)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-3)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#impl-Div%3CNonZero%3Cu16%3E%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#method.div)

Same as `self / other.get()`, but because `other` is a `NonZero<_>`, there’s never a runtime check for division-by-zero.

This operation rounds towards zero, truncating any fractional part of the exact result, and cannot panic.

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#associatedtype.Output-4)

The resulting type after applying the `/` operator.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-6)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u16)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-35)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-5)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#504-507)[§](#method.div-1)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign%3C%26u16%3E-for-u16)

1.79.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#impl-DivAssign%3CNonZero%3Cu16%3E%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#method.div_assign)

Same as `self /= other.get()`, but because `other` is a `NonZero<_>`, there’s never a runtime check for division-by-zero.

This operation rounds towards zero, truncating any fractional part of the exact result, and cannot panic.

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-DivAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-DivAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ascii/ascii_char.rs.html#1171)[§](#method.from-12)

Converts to this type from the input type.

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`u16`](https://doc.rust-lang.org/stable/std/primitive.u16.html "primitive u16") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-132)Examples

```rust
assert_eq!(u16::from(false), 0);

assert_eq!(u16::from(true), 1);
```

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3653-3670)[§](#impl-From%3Cu16%3E-for-AtomicU16)

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3653-3670)[§](#method.from-13)

Converts an `u16` into an `AtomicU16`.

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#170)[§](#impl-From%3Cu16%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#168)[§](#impl-From%3Cu16%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#169)[§](#impl-From%3Cu16%3E-for-f64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#121)[§](#impl-From%3Cu16%3E-for-i128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#119)[§](#impl-From%3Cu16%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#120)[§](#impl-From%3Cu16%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#96)[§](#impl-From%3Cu16%3E-for-u128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#94)[§](#impl-From%3Cu16%3E-for-u32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#95)[§](#impl-From%3Cu16%3E-for-u64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#129)[§](#impl-From%3Cu16%3E-for-usize)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#89)[§](#impl-From%3Cu8%3E-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)[§](#impl-FromStr-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)[§](#method.from_str)

Parses an integer from a string slice with decimal digits.

The characters are expected to be an optional `+` sign followed by only digits. Leading and trailing non-digit characters (including whitespace) represent an error. Underscores (which are accepted in Rust literals) also represent an error.

##### [§](#see-also-1)See also

For parsing numbers in other bases, such as binary or hexadecimal, see [`from_str_radix`](https://doc.rust-lang.org/stable/std/primitive.u16.html#method.from_str_radix "associated function u16::from_str_radix").

##### [§](#examples-131)Examples

```rust
use std::str::FromStr;

assert_eq!(u16::from_str("+10"), Ok(10));
```

Trailing space returns error:

```rust
assert!(u16::from_str("1 ").is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/mod.rs.html#1802)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#218-220)[§](#impl-FunnelShift-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#218-220)[§](#method.unchecked_funnel_shl)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::unchecked_funnel_shl`](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_funnel_shl.html "fn std::intrinsics::unchecked_funnel_shl"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#218-220)[§](#method.unchecked_funnel_shr)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::unchecked_funnel_shr`](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_funnel_shr.html "fn std::intrinsics::unchecked_funnel_shr"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u16)

1.42.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#600)[§](#impl-LowerExp-for-u16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-LowerHex-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-4)

Format unsigned integers in the radix.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-25)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-24)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-23)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-22)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign%3C%26u16%3E-for-u16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-MulAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-MulAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-%26u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num_buffer.rs.html#26-33)[§](#impl-NumBufferTrait-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num_buffer.rs.html#26-33)[§](#associatedconstant.BUF_SIZE)

🔬This is a nightly-only experimental API. (`int_format_into` [#138215](https://github.com/rust-lang/rust/issues/138215))

Maximum number of digits in decimal base of the implemented integer.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-Octal-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-3)

Format unsigned integers in the radix.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#impl-Ord-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2080)[§](#impl-PartialOrd-for-u16)

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

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.product-1)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Product-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.product)

Takes an iterator and generates `Self` from the elements by multiplying the items.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#impl-RangePattern-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#associatedconstant.MIN-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#associatedconstant.MAX-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/stable/src/core/pat.rs.html#61-64)[§](#method.sub_one)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

A compile-time helper to subtract 1 for exclusive ranges.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-13)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-12)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-3)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#impl-Rem%3CNonZero%3Cu16%3E%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#method.rem)

This operation satisfies `n % d == n - (n / d) * d`, and cannot panic.

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#associatedtype.Output-9)

The resulting type after applying the `%` operator.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-11)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#impl-Rem-for-u16)

This operation satisfies `n % d == n - (n / d) * d`. The result has the same sign as the left operand.

#### [§](#panics-36)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#associatedtype.Output-10)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#613-616)[§](#method.rem-1)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign%3C%26u16%3E-for-u16)

1.79.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#impl-RemAssign%3CNonZero%3Cu16%3E%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#2424-2434)[§](#method.rem_assign)

This operation satisfies `n % d == n - (n / d) * d`, and cannot panic.

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-RemAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-RemAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-83)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-82)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-71)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-70)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-75)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-74)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-79)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-78)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-67)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26i8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-66)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-87)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26isize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-86)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-59)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-23)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-58)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-22)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26u16%3E-for-%26Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-131)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-123)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-111)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-115)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-119)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-107)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-127)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-99)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-47)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-91)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-95)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-39)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-103)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-67)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3C%26u16%3E-for-Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-129)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-122)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-110)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-114)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-118)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-106)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-70)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-126)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-98)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-46)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-90)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-94)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-38)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-102)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-51)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-50)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-55)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-54)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-43)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26u8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-42)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-63)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3C%26usize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-62)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-81)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-80)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-69)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-68)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-73)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-72)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-77)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-76)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-65)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Ci8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-64)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-85)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-84)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-57)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-21)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-56)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-20)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Cu16%3E-for-%26Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-130)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-121)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-109)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-113)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-117)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-105)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-125)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-97)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-45)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-89)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-93)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-37)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-101)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-65)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shl%3Cu16%3E-for-Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-128)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shl-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-120)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-108)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-112)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-116)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-104)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-68)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-124)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-88)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-96)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-88)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-92)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-36)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-100)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-49)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-48)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-53)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-52)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-41)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cu8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-40)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-61)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl%3Cusize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-60)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#impl-Shl-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#associatedtype.Output-44)

The resulting type after applying the `<<` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#517)[§](#method.shl-8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i128%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i16%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i32%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i64%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26i8%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26isize%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u128%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u16%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u32%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u64%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26u8%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3C%26usize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci128%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci16%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci32%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci64%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Ci8%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cisize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu128%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu16%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu32%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu64%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cu8%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign%3Cusize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#991)[§](#impl-ShlAssign-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-179)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-178)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-167)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-35)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-166)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-34)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-171)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-39)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-170)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-38)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-175)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-174)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-163)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-31)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26i8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-162)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-30)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-183)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26isize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-182)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-155)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-23)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-154)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-22)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26u16%3E-for-%26Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-227)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-95)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-219)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-87)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-207)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-75)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-211)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-79)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-215)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-83)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-203)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-223)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-91)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-195)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-143)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-187)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-191)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-135)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-199)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-67)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3C%26u16%3E-for-Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-225)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-93)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-218)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-86)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-206)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-74)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-210)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-78)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-214)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-82)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-202)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-70)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-222)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-90)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-194)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-142)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-186)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-190)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-134)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-198)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-147)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-146)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-151)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-19)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-150)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-18)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-139)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26u8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-138)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-159)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-27)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3C%26usize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-158)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-26)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-177)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-176)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-165)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-33)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-164)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-169)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-37)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-168)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-36)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-173)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-172)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-161)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Ci8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-160)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-28)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-181)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-180)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-153)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-21)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-152)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-20)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Cu16%3E-for-%26Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-226)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-94)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-217)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-85)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-205)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-73)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-209)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-77)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-213)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-81)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-201)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-221)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-89)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-193)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-141)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-185)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-189)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-133)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-%26usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-197)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-65)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#impl-Shr%3Cu16%3E-for-Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#associatedtype.Output-224)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/ops/shift_scalar.rs.html#54)[§](#method.shr-92)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-216)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-84)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-204)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-72)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-208)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-76)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-212)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-80)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-200)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-68)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-220)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-88)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-192)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-184)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-188)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-132)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu16%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-196)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-145)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-144)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-149)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-17)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-148)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-137)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cu8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-136)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-157)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-25)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr%3Cusize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-156)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-24)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#impl-Shr-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#associatedtype.Output-140)

The resulting type after applying the `>>` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#639)[§](#method.shr-8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i128%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i16%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i32%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i64%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26i8%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26isize%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u128%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-i128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-i16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-i32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-i64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-i8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-isize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-u128)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-u32)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-u64)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-u8)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u16%3E-for-usize)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u32%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u64%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26u8%3E-for-u16)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3C%26usize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci128%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci16%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci32%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci64%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Ci8%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cisize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu128%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-i128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-i16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-i32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-i64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-i8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-isize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-u128)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-u32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-u64)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-u8)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu16%3E-for-usize)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu32%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu64%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cu8%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign%3Cusize%3E-for-u16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#1077)[§](#impl-ShrAssign-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1090)[§](#impl-SimdElement-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1091)[§](#associatedtype.Mask)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#434-437)[§](#impl-Step-for-u16)

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

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-21)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-20)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-19)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-18)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3C%26u16%3E-for-Saturating%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3C%26u16%3E-for-Wrapping%3Cu16%3E)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign%3C%26u16%3E-for-u16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/saturating.rs.html#551)[§](#impl-SubAssign%3Cu16%3E-for-Saturating%3Cu16%3E)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/num/wrapping.rs.html#566)[§](#impl-SubAssign%3Cu16%3E-for-Wrapping%3Cu16%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign-for-u16)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.sum-1)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#impl-Sum-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#204)[§](#method.sum)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/char/convert.rs.html#135)[§](#impl-TryFrom%3Cchar%3E-for-u16)

Maps a `char` with a code point from U+0000 to U+FFFF (inclusive) to a `u16` in `0x0000..=0xFFFF` with the same value, failing if the code point is greater than U+FFFF.

This corresponds to the UCS-2 encoding, as specified in ISO/IEC 10646:2003.

[Source](https://doc.rust-lang.org/stable/src/core/char/convert.rs.html#150)[§](#method.try_from-16)

Tries to convert a [`char`](https://doc.rust-lang.org/stable/std/primitive.char.html "primitive char") into a [`u16`](https://doc.rust-lang.org/stable/std/primitive.u16.html "primitive u16").

##### [§](#examples-134)Examples

```rust
let trans_rights = '⚧'; // U+26A7
let ninjas = '🥷'; // U+1F977

assert_eq!(u16::try_from(trans_rights), Ok(0x26A7_u16));
assert!(u16::try_from(ninjas).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/char/convert.rs.html#136)[§](#associatedtype.Error-16)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#401)[§](#impl-TryFrom%3Ci128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#401)[§](#method.try_from-11)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#401)[§](#associatedtype.Error-11)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#method.try_from-8)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-8)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#397)[§](#impl-TryFrom%3Ci32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#397)[§](#method.try_from-9)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#397)[§](#associatedtype.Error-9)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#399)[§](#impl-TryFrom%3Ci64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#399)[§](#method.try_from-10)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#399)[§](#associatedtype.Error-10)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#394)[§](#method.try_from-7)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-7)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#method.try_from-13)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-13)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#378)[§](#impl-TryFrom%3Cu128%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#378)[§](#method.try_from-4)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#378)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#563)[§](#impl-TryFrom%3Cu16%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#563)[§](#method.try_from-15)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#563)[§](#associatedtype.Error-15)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu16%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#method.try_from)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-133)Examples

```rust
assert_eq!(0_u16.try_into(), Ok(false));

assert_eq!(1_u16.try_into(), Ok(true));

assert!(<u16 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#impl-TryFrom%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#method.try_from-6)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#associatedtype.Error-6)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#impl-TryFrom%3Cu16%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#method.try_from-5)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#388)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#impl-TryFrom%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#method.try_from-14)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#474)[§](#associatedtype.Error-14)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#375)[§](#impl-TryFrom%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#375)[§](#method.try_from-1)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#375)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#376)[§](#impl-TryFrom%3Cu32%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#376)[§](#method.try_from-2)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#376)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#377)[§](#impl-TryFrom%3Cu64%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#377)[§](#method.try_from-3)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#377)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#459)[§](#impl-TryFrom%3Cusize%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#459)[§](#method.try_from-12)

Tries to create the target number type from a source number type. This returns an error if the source value is outside of the range of the target type.

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#459)[§](#associatedtype.Error-12)

The type returned in the event of a conversion error.

1.42.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#600)[§](#impl-UpperExp-for-u16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#impl-UpperHex-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/num.rs.html#74)[§](#method.fmt-5)

Format unsigned integers in the radix.

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#69-83)[§](#impl-ZeroablePrimitive-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/num/nonzero.rs.html#69-83)[§](#associatedtype.NonZeroInner)

🔬This is a nightly-only experimental API. (`nonzero_internals`)

A type like `Self` but with a niche that includes zero.

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-u16)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-u16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#40)[§](#impl-FloatToInt%3Cu16%3E-for-f128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu16%3E-for-f16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu16%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#39)[§](#impl-FloatToInt%3Cu16%3E-for-f64)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/cast.rs.html#36)[§](#impl-SimdCast-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/iter/range.rs.html#17)[§](#impl-TrustedStep-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-u16)

[§](#impl-Freeze-for-u16)

[§](#impl-RefUnwindSafe-for-u16)

[§](#impl-Send-for-u16)

[§](#impl-Sync-for-u16)

[§](#impl-Unpin-for-u16)

[§](#impl-UnsafeUnpin-for-u16)

[§](#impl-UnwindSafe-for-u16)