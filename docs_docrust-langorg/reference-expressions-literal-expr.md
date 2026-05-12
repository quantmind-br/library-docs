---
title: Literal expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/literal-expr.html
source: crawler
fetched_at: 2026-05-06T21:26:54.77089118-03:00
rendered_js: false
word_count: 2120
summary: This document defines literal expressions in Rust, detailing how character and string literals are represented, typed, and processed using various escape sequences.
tags:
    - rust
    - literal-expressions
    - syntax
    - string-literals
    - character-literals
    - escape-sequences
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Literal expressions](#literal-expressions)

A *literal expression* is an expression consisting of a single token, rather than a sequence of tokens, that immediately and directly denotes the value it evaluates to, rather than referring to it by name or some other evaluation rule.

A literal is a form of [constant expression](https://doc.rust-lang.org/reference/const_eval.html#constant-expressions), so is evaluated (primarily) at compile time.

Each of the lexical [literal](https://doc.rust-lang.org/reference/tokens.html#literals) forms described earlier can make up a literal expression, as can the keywords `true` and `false`.

```rust
#![allow(unused)]
fn main() {
"hello";   // string type
'5';       // character type
5;         // integer type
}
```

In the descriptions below, the *string representation* of a token is the sequence of characters from the input which matched the token’s production in a *Lexer* grammar snippet.

> Note
> 
> This string representation never includes a character `U+000D` (CR) immediately followed by `U+000A` (LF): this pair would have been previously transformed into a single `U+000A` (LF).

## [Escapes](#escapes)

The descriptions of textual literal expressions below make use of several forms of *escape*.

Each form of escape is characterised by:

- an *escape sequence*: a sequence of characters, which always begins with `U+005C` (`\`)
- an *escaped value*: either a single character or an empty sequence of characters

In the definitions of escapes below:

- An *octal digit* is any of the characters in the range \[`0`-`7`].
- A *hexadecimal digit* is any of the characters in the ranges \[`0`-`9`], \[`a`-`f`], or \[`A`-`F`].

### [Simple escapes](#simple-escapes)

Each sequence of characters occurring in the first column of the following table is an escape sequence.

In each case, the escaped value is the character given in the corresponding entry in the second column.

Escape sequenceEscaped value `\0`U+0000 (NUL) `\t`U+0009 (HT) `\n`U+000A (LF) `\r`U+000D (CR) `\"`U+0022 (QUOTATION MARK) `\'`U+0027 (APOSTROPHE) `\\`U+005C (REVERSE SOLIDUS)

### [8-bit escapes](#8-bit-escapes)

The escape sequence consists of `\x` followed by two hexadecimal digits.

The escaped value is the character whose [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) is the result of interpreting the final two characters in the escape sequence as a hexadecimal integer, as if by [`u8::from_str_radix`](https://doc.rust-lang.org/std/primitive.u8.html#method.from_str_radix) with radix 16.

### [7-bit escapes](#7-bit-escapes)

The escape sequence consists of `\x` followed by an octal digit then a hexadecimal digit.

The escaped value is the character whose [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) is the result of interpreting the final two characters in the escape sequence as a hexadecimal integer, as if by [`u8::from_str_radix`](https://doc.rust-lang.org/std/primitive.u8.html#method.from_str_radix) with radix 16.

### [Unicode escapes](#unicode-escapes)

The escape sequence consists of `\u{`, followed by a sequence of characters each of which is a hexadecimal digit or `_`, followed by `}`.

The escaped value is the character whose [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) is the result of interpreting the hexadecimal digits contained in the escape sequence as a hexadecimal integer, as if by [`u32::from_str_radix`](https://doc.rust-lang.org/std/primitive.u32.html#method.from_str_radix) with radix 16.

### [String continuation escapes](#string-continuation-escapes)

The escape sequence consists of `\` followed immediately by `U+000A` (LF), and all following whitespace characters before the next non-whitespace character. For this purpose, the whitespace characters are `U+0009` (HT), `U+000A` (LF), `U+000D` (CR), and `U+0020` (SPACE).

The escaped value is an empty sequence of characters.

> Note
> 
> The effect of this form of escape is that a string continuation skips following whitespace, including additional newlines. Thus `a`, `b` and `c` are equal:
> 
> ```rust
> #![allow(unused)]
fn main() {
let a = "foobar";
let b = "foo\
         bar";
let c = "foo\

     bar";

assert_eq!(a, b);
assert_eq!(b, c);
}
> ```
> 
> Skipping additional newlines (as in example c) is potentially confusing and unexpected. This behavior may be adjusted in the future. Until a decision is made, it is recommended to avoid relying on skipping multiple newlines with line continuations. See [this issue](https://github.com/rust-lang/reference/pull/1042) for more information.

## [Character literal expressions](#character-literal-expressions)

A character literal expression consists of a single [CHAR\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-CHAR_LITERAL) token.

The expression’s type is the primitive [`char`](https://doc.rust-lang.org/reference/types/char.html) type.

The token must not have a suffix.

[\[expr.literal.char.literal-content\]](#r-expr.literal.char.literal-content "expr.literal.char.literal-content")

The token’s *literal content* is the sequence of characters following the first `U+0027` (`'`) and preceding the last `U+0027` (`'`) in the string representation of the token.

The literal expression’s *represented character* is derived from the literal content as follows:

- If the literal content is one of the following forms of escape sequence, the represented character is the escape sequence’s escaped value:
  
  - [Simple escapes](#simple-escapes)
  - [7-bit escapes](#7-bit-escapes)
  - [Unicode escapes](#unicode-escapes)

<!--THE END-->

- Otherwise the represented character is the single character that makes up the literal content.

The expression’s value is the [`char`](https://doc.rust-lang.org/reference/types/char.html) corresponding to the represented character’s [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value).

> Note
> 
> The permitted forms of a [CHAR\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-CHAR_LITERAL) token ensure that these rules always produce a single character.

Examples of character literal expressions:

```rust
#![allow(unused)]
fn main() {
'R';                               // R
'\'';                              // '
'\x52';                            // R
'\u{00E6}';                        // LATIN SMALL LETTER AE (U+00E6)
}
```

## [String literal expressions](#string-literal-expressions)

A string literal expression consists of a single [STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-STRING_LITERAL) or [RAW\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-RAW_STRING_LITERAL) token.

The expression’s type is a shared reference (with `static` lifetime) to the primitive [`str`](https://doc.rust-lang.org/reference/types/str.html) type. That is, the type is `&'static str`.

The token must not have a suffix.

[\[expr.literal.string.literal-content\]](#r-expr.literal.string.literal-content "expr.literal.string.literal-content")

The token’s *literal content* is the sequence of characters following the first `U+0022` (`"`) and preceding the last `U+0022` (`"`) in the string representation of the token.

The literal expression’s *represented string* is a sequence of characters derived from the literal content as follows:

- If the token is a [STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-STRING_LITERAL), each escape sequence of any of the following forms occurring in the literal content is replaced by the escape sequence’s escaped value.
  
  - [Simple escapes](#simple-escapes)
  - [7-bit escapes](#7-bit-escapes)
  - [Unicode escapes](#unicode-escapes)
  - [String continuation escapes](#string-continuation-escapes)
  
  These replacements take place in left-to-right order. For example, the token `"\\x41"` is converted to the characters `\` `x` `4` `1`.

<!--THE END-->

- If the token is a [RAW\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-RAW_STRING_LITERAL), the represented string is identical to the literal content.

The expression’s value is a reference to a statically allocated [`str`](https://doc.rust-lang.org/reference/types/str.html) containing the UTF-8 encoding of the represented string.

Examples of string literal expressions:

```rust
#![allow(unused)]
fn main() {
"foo"; r"foo";                     // foo
"\"foo\""; r#""foo""#;             // "foo"

"foo #\"# bar";
r##"foo #"# bar"##;                // foo #"# bar

"\x52"; "R"; r"R";                 // R
"\\x52"; r"\x52";                  // \x52
}
```

## [Byte literal expressions](#byte-literal-expressions)

A byte literal expression consists of a single [BYTE\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-BYTE_LITERAL) token.

The expression’s type is the primitive [`u8`](https://doc.rust-lang.org/reference/types/numeric.html) type.

The token must not have a suffix.

[\[expr.literal.byte-char.literal-content\]](#r-expr.literal.byte-char.literal-content "expr.literal.byte-char.literal-content")

The token’s *literal content* is the sequence of characters following the first `U+0027` (`'`) and preceding the last `U+0027` (`'`) in the string representation of the token.

The literal expression’s *represented character* is derived from the literal content as follows:

- If the literal content is one of the following forms of escape sequence, the represented character is the escape sequence’s escaped value:
  
  - [Simple escapes](#simple-escapes)
  - [8-bit escapes](#8-bit-escapes)

<!--THE END-->

- Otherwise the represented character is the single character that makes up the literal content.

The expression’s value is the represented character’s [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value).

> Note
> 
> The permitted forms of a [BYTE\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-BYTE_LITERAL) token ensure that these rules always produce a single character, whose Unicode scalar value is in the range of [`u8`](https://doc.rust-lang.org/reference/types/numeric.html).

Examples of byte literal expressions:

```rust
#![allow(unused)]
fn main() {
b'R';                              // 82
b'\'';                             // 39
b'\x52';                           // 82
b'\xA0';                           // 160
}
```

## [Byte string literal expressions](#byte-string-literal-expressions)

A byte string literal expression consists of a single [BYTE\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-BYTE_STRING_LITERAL) or [RAW\_BYTE\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-RAW_BYTE_STRING_LITERAL) token.

The expression’s type is a shared reference (with `static` lifetime) to an array whose element type is [`u8`](https://doc.rust-lang.org/reference/types/numeric.html). That is, the type is `&'static [u8; N]`, where `N` is the number of bytes in the represented string described below.

The token must not have a suffix.

[\[expr.literal.byte-string.literal-content\]](#r-expr.literal.byte-string.literal-content "expr.literal.byte-string.literal-content")

The token’s *literal content* is the sequence of characters following the first `U+0022` (`"`) and preceding the last `U+0022` (`"`) in the string representation of the token.

The literal expression’s *represented string* is a sequence of characters derived from the literal content as follows:

- If the token is a [BYTE\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-BYTE_STRING_LITERAL), each escape sequence of any of the following forms occurring in the literal content is replaced by the escape sequence’s escaped value.
  
  - [Simple escapes](#simple-escapes)
  - [8-bit escapes](#8-bit-escapes)
  - [String continuation escapes](#string-continuation-escapes)
  
  These replacements take place in left-to-right order. For example, the token `b"\\x41"` is converted to the characters `\` `x` `4` `1`.

<!--THE END-->

- If the token is a [RAW\_BYTE\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-RAW_BYTE_STRING_LITERAL), the represented string is identical to the literal content.

The expression’s value is a reference to a statically allocated array containing the [Unicode scalar values](http://www.unicode.org/glossary/#unicode_scalar_value) of the characters in the represented string, in the same order.

Examples of byte string literal expressions:

```rust
#![allow(unused)]
fn main() {
b"foo"; br"foo";                     // foo
b"\"foo\""; br#""foo""#;             // "foo"

b"foo #\"# bar";
br##"foo #"# bar"##;                 // foo #"# bar

b"\x52"; b"R"; br"R";                // R
b"\\x52"; br"\x52";                  // \x52
}
```

## [C string literal expressions](#c-string-literal-expressions)

A C string literal expression consists of a single [C\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-C_STRING_LITERAL) or [RAW\_C\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-RAW_C_STRING_LITERAL) token.

The expression’s type is a shared reference (with `static` lifetime) to the standard library [CStr](https://doc.rust-lang.org/core/ffi/c_str/struct.CStr.html) type. That is, the type is `&'static core::ffi::CStr`.

The token must not have a suffix.

[\[expr.literal.c-string.literal-content\]](#r-expr.literal.c-string.literal-content "expr.literal.c-string.literal-content")

The token’s *literal content* is the sequence of characters following the first `"` and preceding the last `"` in the string representation of the token.

The literal expression’s *represented bytes* are a sequence of bytes derived from the literal content as follows:

- If the token is a [C\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-C_STRING_LITERAL), the literal content is treated as a sequence of items, each of which is either a single Unicode character other than `\` or an [escape](#escapes). The sequence of items is converted to a sequence of bytes as follows:
  
  - Each single Unicode character contributes its UTF-8 representation.
  - Each [simple escape](#simple-escapes) contributes the [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) of its escaped value.
  - Each [8-bit escape](#8-bit-escapes) contributes a single byte containing the [Unicode scalar value](http://www.unicode.org/glossary/#unicode_scalar_value) of its escaped value.
  - Each [unicode escape](#unicode-escapes) contributes the UTF-8 representation of its escaped value.
  - Each [string continuation escape](#string-continuation-escapes) contributes no bytes.

<!--THE END-->

- If the token is a [RAW\_C\_STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-RAW_C_STRING_LITERAL), the represented bytes are the UTF-8 encoding of the literal content.

The expression’s value is a reference to a statically allocated [CStr](https://doc.rust-lang.org/core/ffi/c_str/struct.CStr.html) whose array of bytes contains the represented bytes followed by a null byte.

Examples of C string literal expressions:

```rust
#![allow(unused)]
fn main() {
c"foo"; cr"foo";                     // foo
c"\"foo\""; cr#""foo""#;             // "foo"

c"foo #\"# bar";
cr##"foo #"# bar"##;                 // foo #"# bar

c"\x52"; c"R"; cr"R";                // R
c"\\x52"; cr"\x52";                  // \x52

c"æ";                                // LATIN SMALL LETTER AE (U+00E6)
c"\u{00E6}";                         // LATIN SMALL LETTER AE (U+00E6)
c"\xC3\xA6";                         // LATIN SMALL LETTER AE (U+00E6)

c"\xE6".to_bytes();                  // [230]
c"\u{00E6}".to_bytes();              // [195, 166]
}
```

## [Integer literal expressions](#integer-literal-expressions)

An integer literal expression consists of a single [INTEGER\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-INTEGER_LITERAL) token.

If the token has a [suffix](https://doc.rust-lang.org/reference/tokens.html#suffixes), the suffix must be the name of one of the [primitive integer types](https://doc.rust-lang.org/reference/types/numeric.html): `u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`, `i128`, `usize`, or `isize`, and the expression has that type.

If the token has no suffix, the expression’s type is determined by type inference:

- If an integer type can be *uniquely* determined from the surrounding program context, the expression has that type.

<!--THE END-->

- If the program context under-constrains the type, it defaults to the signed 32-bit integer `i32`.

<!--THE END-->

- If the program context over-constrains the type, it is considered a static type error.

Examples of integer literal expressions:

```rust
#![allow(unused)]
fn main() {
123;                               // type i32
123i32;                            // type i32
123u32;                            // type u32
123_u32;                           // type u32
let a: u64 = 123;                  // type u64

0xff;                              // type i32
0xff_u8;                           // type u8

0o70;                              // type i32
0o70_i16;                          // type i16

0b1111_1111_1001_0000;             // type i32
0b1111_1111_1001_0000i64;          // type i64

0usize;                            // type usize
}
```

The value of the expression is determined from the string representation of the token as follows:

- An integer radix is chosen by inspecting the first two characters of the string, as follows:
  
  - `0b` indicates radix 2
  - `0o` indicates radix 8
  - `0x` indicates radix 16
  - otherwise the radix is 10.

<!--THE END-->

- If the radix is not 10, the first two characters are removed from the string.

<!--THE END-->

- Any suffix is removed from the string.

<!--THE END-->

- Any underscores are removed from the string.

<!--THE END-->

- The string is converted to a `u128` value as if by [`u128::from_str_radix`](https://doc.rust-lang.org/std/primitive.u128.html#method.from_str_radix) with the chosen radix. If the value does not fit in `u128`, it is a compiler error.

<!--THE END-->

- The `u128` value is converted to the expression’s type via a [numeric cast](https://doc.rust-lang.org/reference/expressions/operator-expr.html#numeric-cast).

> Note
> 
> The final cast will truncate the value of the literal if it does not fit in the expression’s type. `rustc` includes a [lint check](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes) named `overflowing_literals`, defaulting to `deny`, which rejects expressions where this occurs.

> Note
> 
> `-1i8`, for example, is an application of the [negation operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#negation-operators) to the literal expression `1i8`, not a single integer literal expression. See [Overflow](https://doc.rust-lang.org/reference/expressions/operator-expr.html#overflow) for notes on representing the most negative value for a signed type.

## [Floating-point literal expressions](#floating-point-literal-expressions)

A floating-point literal expression has one of two forms:

- a single [FLOAT\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-FLOAT_LITERAL) token
- a single [INTEGER\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-INTEGER_LITERAL) token which has a suffix and no radix indicator

If the token has a [suffix](https://doc.rust-lang.org/reference/tokens.html#suffixes), the suffix must be the name of one of the [primitive floating-point types](https://doc.rust-lang.org/reference/types/numeric.html#floating-point-types): `f32` or `f64`, and the expression has that type.

If the token has no suffix, the expression’s type is determined by type inference:

- If a floating-point type can be *uniquely* determined from the surrounding program context, the expression has that type.

<!--THE END-->

- If the program context under-constrains the type, it defaults to `f64`.

<!--THE END-->

- If the program context over-constrains the type, it is considered a static type error.

Examples of floating-point literal expressions:

```rust
#![allow(unused)]
fn main() {
123.0f64;        // type f64
0.1f64;          // type f64
0.1f32;          // type f32
12E+99_f64;      // type f64
5f32;            // type f32
let x: f64 = 2.; // type f64
}
```

The value of the expression is determined from the string representation of the token as follows:

- Any suffix is removed from the string.

<!--THE END-->

- Any underscores are removed from the string.

<!--THE END-->

- The string is converted to the expression’s type as if by [`f32::from_str`](https://doc.rust-lang.org/core/primitive.f32.html#method.from_str) or [`f64::from_str`](https://doc.rust-lang.org/core/primitive.f64.html#method.from_str).

> Note
> 
> `-1.0`, for example, is an application of the [negation operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#negation-operators) to the literal expression `1.0`, not a single floating-point literal expression.

> Note
> 
> `inf` and `NaN` are not literal tokens. The [`f32::INFINITY`](https://doc.rust-lang.org/std/primitive.f32.html#associatedconstant.INFINITY), [`f64::INFINITY`](https://doc.rust-lang.org/std/primitive.f64.html#associatedconstant.INFINITY), [`f32::NAN`](https://doc.rust-lang.org/std/primitive.f32.html#associatedconstant.NAN), and [`f64::NAN`](https://doc.rust-lang.org/std/primitive.f64.html#associatedconstant.NAN) constants can be used instead of literal expressions. In `rustc`, a literal large enough to be evaluated as infinite will trigger the `overflowing_literals` lint check.

## [Boolean literal expressions](#boolean-literal-expressions)

A boolean literal expression consists of one of the keywords `true` or `false`.

The expression’s type is the primitive [boolean type](https://doc.rust-lang.org/reference/types/boolean.html), and its value is:

- true if the keyword is `true`
- false if the keyword is `false`