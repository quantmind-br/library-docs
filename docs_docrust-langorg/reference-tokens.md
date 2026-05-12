---
title: Tokens - The Rust Reference
url: https://doc.rust-lang.org/reference/tokens.html#grammar-STRING_LITERAL
source: crawler
fetched_at: 2026-05-06T21:38:50.001464785-03:00
rendered_js: false
word_count: 3274
summary: This document defines the syntax and rules for lexical tokens in the Rust programming language, specifically focusing on literals, character and string formats, and escape sequences.
tags:
    - rust
    - lexical-analysis
    - literals
    - string-literals
    - tokens
    - programming-grammar
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Tokens](#tokens)

Tokens are primitive productions in the grammar defined by regular (non-recursive) languages. Rust source input can be broken down into the following kinds of tokens:

- [Keywords](https://doc.rust-lang.org/reference/keywords.html)
- [Identifiers](https://doc.rust-lang.org/reference/identifiers.html)
- [Literals](#literals)
- [Lifetimes](#lifetimes-and-loop-labels)
- [Punctuation](#punctuation)
- [Delimiters](#delimiters)

Within this documentation’s grammar, “simple” tokens are given in [string table production](https://doc.rust-lang.org/reference/notation.html#string-table-productions) form, and appear in `monospace` font.

## [Literals](#literals)

Literals are tokens used in [literal expressions](https://doc.rust-lang.org/reference/expressions/literal-expr.html).

### [Examples](#examples)

#### [Characters and strings](#characters-and-strings)

Example`#` sets[1](#footnote-nsets)CharactersEscapes [Character](#character-literals)`'H'`0All Unicode[Quote](#quote-escapes) & [ASCII](#ascii-escapes) & [Unicode](#unicode-escapes) [String](#string-literals)`"hello"`0All Unicode[Quote](#quote-escapes) & [ASCII](#ascii-escapes) & [Unicode](#unicode-escapes) [Raw string](#raw-string-literals)`r#"hello"#`&lt;256All Unicode`N/A` [Byte](#byte-literals)`b'H'`0All ASCII[Quote](#quote-escapes) & [Byte](#byte-escapes) [Byte string](#byte-string-literals)`b"hello"`0All ASCII[Quote](#quote-escapes) & [Byte](#byte-escapes) [Raw byte string](#raw-byte-string-literals)`br#"hello"#`&lt;256All ASCII`N/A` [C string](#c-string-literals)`c"hello"`0All Unicode[Quote](#quote-escapes) & [Byte](#byte-escapes) & [Unicode](#unicode-escapes) [Raw C string](#raw-c-string-literals)`cr#"hello"#`&lt;256All Unicode`N/A`

#### [ASCII escapes](#ascii-escapes)

Name `\x41`7-bit character code (exactly 2 hex digits, up to 0x7F) `\n`Newline `\r`Carriage return `\t`Tab `\\`Backslash `\0`Null

#### [Byte escapes](#byte-escapes)

Name `\x7F`8-bit character code (exactly 2 hex digits) `\n`Newline `\r`Carriage return `\t`Tab `\\`Backslash `\0`Null

#### [Unicode escapes](#unicode-escapes)

Name `\u{7FFF}`24-bit Unicode character code (up to 6 hex digits)

#### [Quote escapes](#quote-escapes)

Name `\'`Single quote `\"`Double quote

#### [Numbers](#numbers)

[Number literals](#number-literals)[2](#footnote-nl)ExampleExponentiation Decimal integer`98_222``N/A` Hex integer`0xff``N/A` Octal integer`0o77``N/A` Binary integer`0b1111_0000``N/A` Floating-point`123.0E+77``Optional`

#### [Suffixes](#suffixes)

A suffix is a sequence of characters following the primary part of a literal (without intervening whitespace), of the same form as a non-raw identifier or keyword.

Any kind of literal (string, integer, etc) with any suffix is valid as a token.

A literal token with any suffix can be passed to a macro without producing an error. The macro itself will decide how to interpret such a token and whether to produce an error or not. In particular, the `literal` fragment specifier for by-example macros matches literal tokens with arbitrary suffixes.

```rust
#![allow(unused)]
fn main() {
macro_rules! blackhole { ($tt:tt) => () }
macro_rules! blackhole_lit { ($l:literal) => () }

blackhole!("string"suffix); // OK
blackhole_lit!(1suffix); // OK
}
```

However, suffixes on literal tokens which are interpreted as literal expressions or patterns are restricted. Any suffixes are rejected on non-numeric literal tokens, and numeric literal tokens are accepted only with suffixes from the list below.

IntegerFloating-point `u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`, `i128`, `usize`, `isize``f32`, `f64`

### [Character and string literals](#character-and-string-literals)

#### [Character literals](#character-literals)

A *character literal* is a single Unicode character enclosed within two `U+0027` (single-quote) characters, with the exception of `U+0027` itself, which must be *escaped* by a preceding `U+005C` character (`\`).

#### [String literals](#string-literals)

A *string literal* is a sequence of any Unicode characters enclosed within two `U+0022` (double-quote) characters, with the exception of `U+0022` itself, which must be *escaped* by a preceding `U+005C` character (`\`).

Line-breaks, represented by the character `U+000A` (LF), are allowed in string literals. The character `U+000D` (CR) may not appear in a string literal. When an unescaped `U+005C` character (`\`) occurs immediately before a line break, the line break does not appear in the string represented by the token. See [String continuation escapes](https://doc.rust-lang.org/reference/expressions/literal-expr.html#string-continuation-escapes) for details.

#### [Character escapes](#character-escapes)

Some additional *escapes* are available in either character or non-raw string literals. An escape starts with a `U+005C` (`\`) and continues with one of the following forms:

- A *7-bit code point escape* starts with `U+0078` (`x`) and is followed by exactly two *hex digits* with value up to `0x7F`. It denotes the ASCII character with value equal to the provided hex value. Higher values are not permitted because it is ambiguous whether they mean Unicode code points or byte values.

<!--THE END-->

- A *24-bit code point escape* starts with `U+0075` (`u`) and is followed by up to six *hex digits* surrounded by braces `U+007B` (`{`) and `U+007D` (`}`). It denotes the Unicode code point equal to the provided hex value. The value must be a valid Unicode scalar value.

<!--THE END-->

- A *whitespace escape* is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the Unicode values `U+000A` (LF), `U+000D` (CR) or `U+0009` (HT) respectively.

<!--THE END-->

- The *null escape* is the character `U+0030` (`0`) and denotes the Unicode value `U+0000` (NUL).

<!--THE END-->

- The *backslash escape* is the character `U+005C` (`\`) which must be escaped in order to denote itself.

#### [Raw string literals](#raw-string-literals)

Raw string literals do not process any escapes. They start with the character `U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`) and a `U+0022` (double-quote) character.

[\[lex.token.literal.str-raw.body\]](#r-lex.token.literal.str-raw.body "lex.token.literal.str-raw.body")

The *raw string body* can contain any sequence of Unicode characters other than `U+000D` (CR). It is terminated only by another `U+0022` (double-quote) character, followed by the same number of `U+0023` (`#`) characters that preceded the opening `U+0022` (double-quote) character.

[\[lex.token.literal.str-raw.content\]](#r-lex.token.literal.str-raw.content "lex.token.literal.str-raw.content")

All Unicode characters contained in the raw string body represent themselves, the characters `U+0022` (double-quote) (except when followed by at least as many `U+0023` (`#`) characters as were used to start the raw string literal) or `U+005C` (`\`) do not have any special meaning.

Examples for string literals:

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

### [Byte and byte string literals](#byte-and-byte-string-literals)

#### [Byte literals](#byte-literals)

A *byte literal* is a single ASCII character (in the `U+0000` to `U+007F` range) or a single *escape* preceded by the characters `U+0062` (`b`) and `U+0027` (single-quote), and followed by the character `U+0027`. If the character `U+0027` is present within the literal, it must be *escaped* by a preceding `U+005C` (`\`) character. It is equivalent to a `u8` unsigned 8-bit integer *number literal*.

#### [Byte string literals](#byte-string-literals)

A non-raw *byte string literal* is a sequence of ASCII characters and *escapes*, preceded by the characters `U+0062` (`b`) and `U+0022` (double-quote), and followed by the character `U+0022`. If the character `U+0022` is present within the literal, it must be *escaped* by a preceding `U+005C` (`\`) character. Alternatively, a byte string literal can be a *raw byte string literal*, defined below.

Line-breaks, represented by the character `U+000A` (LF), are allowed in byte string literals. The character `U+000D` (CR) may not appear in a byte string literal. When an unescaped `U+005C` character (`\`) occurs immediately before a line break, the line break does not appear in the string represented by the token. See [String continuation escapes](https://doc.rust-lang.org/reference/expressions/literal-expr.html#string-continuation-escapes) for details.

Some additional *escapes* are available in either byte or non-raw byte string literals. An escape starts with a `U+005C` (`\`) and continues with one of the following forms:

- A *byte escape* escape starts with `U+0078` (`x`) and is followed by exactly two *hex digits*. It denotes the byte equal to the provided hex value.

<!--THE END-->

- A *whitespace escape* is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the bytes values `0x0A` (ASCII LF), `0x0D` (ASCII CR) or `0x09` (ASCII HT) respectively.

<!--THE END-->

- The *null escape* is the character `U+0030` (`0`) and denotes the byte value `0x00` (ASCII NUL).

<!--THE END-->

- The *backslash escape* is the character `U+005C` (`\`) which must be escaped in order to denote its ASCII encoding `0x5C`.

#### [Raw byte string literals](#raw-byte-string-literals)

Raw byte string literals do not process any escapes. They start with the character `U+0062` (`b`), followed by `U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`), and a `U+0022` (double-quote) character.

[\[lex.token.str-byte-raw.body\]](#r-lex.token.str-byte-raw.body "lex.token.str-byte-raw.body")

The *raw string body* can contain any sequence of ASCII characters other than `U+000D` (CR). It is terminated only by another `U+0022` (double-quote) character, followed by the same number of `U+0023` (`#`) characters that preceded the opening `U+0022` (double-quote) character. A raw byte string literal can not contain any non-ASCII byte.

[\[lex.token.literal.str-byte-raw.content\]](#r-lex.token.literal.str-byte-raw.content "lex.token.literal.str-byte-raw.content")

All characters contained in the raw string body represent their ASCII encoding, the characters `U+0022` (double-quote) (except when followed by at least as many `U+0023` (`#`) characters as were used to start the raw string literal) or `U+005C` (`\`) do not have any special meaning.

Examples for byte string literals:

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

### [C string and raw C string literals](#c-string-and-raw-c-string-literals)

#### [C string literals](#c-string-literals)

A *C string literal* is a sequence of Unicode characters and *escapes*, preceded by the characters `U+0063` (`c`) and `U+0022` (double-quote), and followed by the character `U+0022`. If the character `U+0022` is present within the literal, it must be *escaped* by a preceding `U+005C` (`\`) character. Alternatively, a C string literal can be a *raw C string literal*, defined below.

C strings are implicitly terminated by byte `0x00`, so the C string literal `c""` is equivalent to manually constructing a `&CStr` from the byte string literal `b"\x00"`. Other than the implicit terminator, byte `0x00` is not permitted within a C string.

Line-breaks, represented by the character `U+000A` (LF), are allowed in C string literals. The character `U+000D` (CR) may not appear in a C string literal. When an unescaped `U+005C` character (`\`) occurs immediately before a line break, the line break does not appear in the string represented by the token. See [String continuation escapes](https://doc.rust-lang.org/reference/expressions/literal-expr.html#string-continuation-escapes) for details.

Some additional *escapes* are available in non-raw C string literals. An escape starts with a `U+005C` (`\`) and continues with one of the following forms:

- A *byte escape* escape starts with `U+0078` (`x`) and is followed by exactly two *hex digits*. It denotes the byte equal to the provided hex value.

<!--THE END-->

- A *24-bit code point escape* starts with `U+0075` (`u`) and is followed by up to six *hex digits* surrounded by braces `U+007B` (`{`) and `U+007D` (`}`). It denotes the Unicode code point equal to the provided hex value, encoded as UTF-8.

<!--THE END-->

- A *whitespace escape* is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the bytes values `0x0A` (ASCII LF), `0x0D` (ASCII CR) or `0x09` (ASCII HT) respectively.

<!--THE END-->

- The *backslash escape* is the character `U+005C` (`\`) which must be escaped in order to denote its ASCII encoding `0x5C`.

A C string represents bytes with no defined encoding, but a C string literal may contain Unicode characters above `U+007F`. Such characters will be replaced with the bytes of that character’s UTF-8 representation.

The following C string literals are equivalent:

```rust
#![allow(unused)]
fn main() {
c"æ";        // LATIN SMALL LETTER AE (U+00E6)
c"\u{00E6}";
c"\xC3\xA6";
}
```

> 2021 Edition differences
> 
> C string literals are accepted in the 2021 edition or later. In earlier editions the token `c""` is lexed as `c ""`.

#### [Raw C string literals](#raw-c-string-literals)

Raw C string literals do not process any escapes. They start with the character `U+0063` (`c`), followed by `U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`), and a `U+0022` (double-quote) character.

[\[lex.token.str-c-raw.body\]](#r-lex.token.str-c-raw.body "lex.token.str-c-raw.body")

The *raw C string body* can contain any sequence of Unicode characters other than `U+0000` (NUL) and `U+000D` (CR). It is terminated only by another `U+0022` (double-quote) character, followed by the same number of `U+0023` (`#`) characters that preceded the opening `U+0022` (double-quote) character.

[\[lex.token.str-c-raw.content\]](#r-lex.token.str-c-raw.content "lex.token.str-c-raw.content")

All characters contained in the raw C string body represent themselves in UTF-8 encoding. The characters `U+0022` (double-quote) (except when followed by at least as many `U+0023` (`#`) characters as were used to start the raw C string literal) or `U+005C` (`\`) do not have any special meaning.

> 2021 Edition differences
> 
> Raw C string literals are accepted in the 2021 edition or later. In earlier editions the token `cr""` is lexed as `cr ""`, and `cr#""#` is lexed as `cr #""#` (which is non-grammatical).

#### [Examples for C string and raw C string literals](#examples-for-c-string-and-raw-c-string-literals)

```rust
#![allow(unused)]
fn main() {
c"foo"; cr"foo";                     // foo
c"\"foo\""; cr#""foo""#;             // "foo"

c"foo #\"# bar";
cr##"foo #"# bar"##;                 // foo #"# bar

c"\x52"; c"R"; cr"R";                // R
c"\\x52"; cr"\x52";                  // \x52
}
```

### [Number literals](#number-literals)

A *number literal* is either an *integer literal* or a *floating-point literal*. The grammar for recognizing the two kinds of literals is mixed.

#### [Integer literals](#integer-literals)

An *integer literal* has one of four forms:

- A *decimal literal* starts with a *decimal digit* and continues with any mixture of *decimal digits* and *underscores*.

<!--THE END-->

- A *hex literal* starts with the character sequence `U+0030` `U+0078` (`0x`) and continues as any mixture (with at least one digit) of hex digits and underscores.

<!--THE END-->

- An *octal literal* starts with the character sequence `U+0030` `U+006F` (`0o`) and continues as any mixture (with at least one digit) of octal digits and underscores.

<!--THE END-->

- A *binary literal* starts with the character sequence `U+0030` `U+0062` (`0b`) and continues as any mixture (with at least one digit) of binary digits and underscores.

Like any literal, an integer literal may be followed (immediately, without any spaces) by a suffix as described above. The suffix may not begin with `e` or `E`, as that would be interpreted as the exponent of a floating-point literal. See [Integer literal expressions](https://doc.rust-lang.org/reference/expressions/literal-expr.html#integer-literal-expressions) for the effect of these suffixes.

Examples of integer literals which are accepted as literal expressions:

```rust
#![allow(unused)]
fn main() {
#![allow(overflowing_literals)]
123;
123i32;
123u32;
123_u32;

0xff;
0xff_u8;
0x01_f32; // integer 7986, not floating-point 1.0
0x01_e3;  // integer 483, not floating-point 1000.0

0o70;
0o70_i16;

0b1111_1111_1001_0000;
0b1111_1111_1001_0000i64;
0b________1;

0usize;

// These are too big for their type, but are accepted as literal expressions.
128_i8;
256_u8;

// This is an integer literal, accepted as a floating-point literal expression.
5f32;
}
```

Note that `-1i8`, for example, is analyzed as two tokens: `-` followed by `1i8`.

Examples of integer literals which are not accepted as literal expressions:

```rust
#![allow(unused)]
fn main() {
#[cfg(false)] {
0invalidSuffix;
123AFB43;
0b010a;
0xAB_CD_EF_GH;
0b1111_f32;
}
}
```

#### [Tuple index](#tuple-index)

A tuple index is used to refer to the fields of [tuples](https://doc.rust-lang.org/reference/types/tuple.html), [tuple structs](https://doc.rust-lang.org/reference/items/structs.html), and [tuple enum variants](https://doc.rust-lang.org/reference/items/enumerations.html).

Tuple indices are compared with the literal token directly. Tuple indices start with `0` and each successive index increments the value by `1` as a decimal value. Thus, only decimal values will match, and the value must not have any extra `0` prefix characters.

Tuple indices may not include any suffixes (such as `usize`).

```rust
#![allow(unused)]
fn main() {
let example = ("dog", "cat", "horse");
let dog = example.0;
let cat = example.1;
// The following examples are invalid.
let cat = example.01;  // ERROR no field named `01`
let horse = example.0b10;  // ERROR no field named `0b10`
let unicorn = example.0usize; // ERROR suffixes on a tuple index are invalid
let underscore = example.0_0; // ERROR no field `0_0` on type `(&str, &str, &str)`
}
```

#### [Floating-point literals](#floating-point-literals)

A *floating-point literal* has one of two forms:

- A *decimal literal* followed by a period character `U+002E` (`.`). This is optionally followed by another decimal literal, with an optional *exponent*.
- A single *decimal literal* followed by an *exponent*.

Like integer literals, a floating-point literal may be followed by a suffix, so long as the pre-suffix part does not end with `U+002E` (`.`). The suffix may not begin with `e` or `E` if the literal does not include an exponent. See [Floating-point literal expressions](https://doc.rust-lang.org/reference/expressions/literal-expr.html#floating-point-literal-expressions) for the effect of these suffixes.

Examples of floating-point literals which are accepted as literal expressions:

```rust
#![allow(unused)]
fn main() {
123.0f64;
0.1f64;
0.1f32;
12E+99_f64;
let x: f64 = 2.;
}
```

This last example is different because it is not possible to use the suffix syntax with a floating point literal ending in a period. `2.f64` would attempt to call a method named `f64` on `2`.

Note that `-1.0`, for example, is analyzed as two tokens: `-` followed by `1.0`.

Examples of floating-point literals which are not accepted as literal expressions:

```rust
#![allow(unused)]
fn main() {
#[cfg(false)] {
2.0f80;
2e5f80;
2e5e6;
2.0e5e6;
1.3e10u64;
}
}
```

#### [Reserved forms similar to number literals](#reserved-forms-similar-to-number-literals)

The following lexical forms similar to number literals are *reserved forms*. Due to the possible ambiguity these raise, they are rejected by the tokenizer instead of being interpreted as separate tokens.

- An unsuffixed binary or octal literal followed, without intervening whitespace, by a decimal digit out of the range for its radix.

<!--THE END-->

- An unsuffixed binary, octal, or hexadecimal literal followed, without intervening whitespace, by a period character (with the same restrictions on what follows the period as for floating-point literals).

<!--THE END-->

- An unsuffixed binary or octal literal followed, without intervening whitespace, by the character `e` or `E`.

<!--THE END-->

- Input which begins with one of the radix prefixes but is not a valid binary, octal, or hexadecimal literal (because it contains no digits).

<!--THE END-->

- Input which has the form of a floating-point literal with no digits in the exponent.

Examples of reserved forms:

```rust
#![allow(unused)]
fn main() {
0b0102;  // this is not `0b010` followed by `2`
0o1279;  // this is not `0o127` followed by `9`
0x80.0;  // this is not `0x80` followed by `.` and `0`
0b101e;  // this is not a suffixed literal, or `0b101` followed by `e`
0b;      // this is not an integer literal, or `0` followed by `b`
0b_;     // this is not an integer literal, or `0` followed by `b_`
2e;      // this is not a floating-point literal, or `2` followed by `e`
2.0e;    // this is not a floating-point literal, or `2.0` followed by `e`
2em;     // this is not a suffixed literal, or `2` followed by `em`
2.0em;   // this is not a suffixed literal, or `2.0` followed by `em`
}
```

## [Lifetimes and loop labels](#lifetimes-and-loop-labels)

Lifetime parameters and [loop labels](https://doc.rust-lang.org/reference/expressions/loop-expr.html#loop-labels) use LIFETIME\_OR\_LABEL tokens. Any LIFETIME\_TOKEN will be accepted by the lexer, and for example, can be used in macros.

A raw lifetime is like a normal lifetime, but its identifier is prefixed by `r#`. (Note that the `r#` prefix is not included as part of the actual lifetime.)

Unlike a normal lifetime, a raw lifetime may be any strict or reserved keyword except the ones listed above for `RAW_LIFETIME`.

It is an error to use the [RESERVED\_RAW\_LIFETIME](https://doc.rust-lang.org/reference/tokens.html#grammar-RESERVED_RAW_LIFETIME) token.

> 2021 Edition differences
> 
> Raw lifetimes are accepted in the 2021 edition or later. In earlier editions the token `'r#lt` is lexed as `'r # lt`.

## [Punctuation](#punctuation)

Punctuation tokens are used as operators, separators, and other parts of the grammar.

**Lexer**  
[PUNCTUATION](https://doc.rust-lang.org/reference/tokens.html#railroad-PUNCTUATION) →  
      ...  
    | ..=  
    | &lt;&lt;=  
    | &gt;&gt;=  
    | !=  
    | %=  
    | &&  
    | &=  
    | \*=  
    | +=  
    | -=  
    | -&gt;  
    | ..  
    | /=  
    | ::  
    | &lt;-  
    | &lt;&lt;  
    | &lt;=  
    | ==  
    | =&gt;  
    | &gt;=  
    | &gt;&gt;  
    | ^=  
    | |=  
    | ||  
    | !  
    | #  
    | $  
    | %  
    | &  
    | (  
    | )  
    | *  
    | +  
    | ,  
    | -  
    | .  
    | /  
    | :  
    | ;  
    | &lt;  
    | =  
    | &gt;  
    | ?  
    | @  
    | [  
    | ]  
    | ^  
    | {  
    | |  
    | }  
    | ~

> Note
> 
> See the [syntax index](https://doc.rust-lang.org/reference/syntax-index.html#operators-and-punctuation) for links to how punctuation characters are used.

## [Delimiters](#delimiters)

Bracket punctuation is used in various parts of the grammar. An open bracket must always be paired with a close bracket. Brackets and the tokens within them are referred to as “token trees” in [macros](https://doc.rust-lang.org/reference/macros-by-example.html). The three types of brackets are:

BracketType `{` `}`Curly braces `[` `]`Square brackets `(` `)`Parentheses

## [Reserved tokens](#reserved-tokens)

Several token forms are reserved for future use or to avoid confusion. It is an error for the source input to match one of these forms.

## [Reserved prefixes](#reserved-prefixes)

Some lexical forms known as *reserved prefixes* are reserved for future use.

Source input which would otherwise be lexically interpreted as a non-raw identifier (or a keyword) which is immediately followed by a `#`, `'`, or `"` character (without intervening whitespace) is identified as a reserved prefix.

Note that raw identifiers, raw string literals, and raw byte string literals may contain a `#` character but are not interpreted as containing a reserved prefix.

Similarly the `r`, `b`, `br`, `c`, and `cr` prefixes used in raw string literals, byte literals, byte string literals, raw byte string literals, C string literals, and raw C string literals are not interpreted as reserved prefixes.

Source input which would otherwise be lexically interpreted as a non-raw lifetime (or a keyword) which is immediately followed by a `#` character (without intervening whitespace) is identified as a reserved lifetime prefix.

> 2021 Edition differences
> 
> Starting with the 2021 edition, reserved prefixes are reported as an error by the lexer (in particular, they cannot be passed to macros).
> 
> Before the 2021 edition, reserved prefixes are accepted by the lexer and interpreted as multiple tokens (for example, one token for the identifier or keyword, followed by a `#` token).
> 
> Examples accepted in all editions:
> 
> ```rust
> #![allow(unused)]
fn main() {
macro_rules! lexes {($($_:tt)*) => {}}
lexes!{a #foo}
lexes!{continue 'foo}
lexes!{match "..." {}}
lexes!{r#let#foo}         // three tokens: r#let # foo
lexes!{'prefix #lt}
}
> ```
> 
> Examples accepted before the 2021 edition but rejected later:
> 
> ```rust
> #![allow(unused)]
fn main() {
macro_rules! lexes {($($_:tt)*) => {}}
lexes!{a#foo}
lexes!{continue'foo}
lexes!{match"..." {}}
lexes!{'prefix#lt}
}
> ```

## [Reserved guards](#reserved-guards)

The reserved guards are syntax reserved for future use, and will generate a compile error if used.

The *reserved guarded string literal* is a token of one or more `U+0023` (`#`) immediately followed by a [STRING\_LITERAL](https://doc.rust-lang.org/reference/tokens.html#grammar-STRING_LITERAL).

The *reserved pounds* is a token of two or more `U+0023` (`#`).

> 2024 Edition differences
> 
> Before the 2024 edition, reserved guards are accepted by the lexer and interpreted as multiple tokens. For example, the `#"foo"#` form is interpreted as three tokens. `##` is interpreted as two tokens.

* * *

1. The number of `#`s on each side of the same literal must be equivalent. [↩](#fr-nsets-1)
2. All number literals allow `_` as a visual separator: `1_234.0E+18f64` [↩](#fr-nl-1)
3. See [lex.token.literal.char-escape.unicode](https://doc.rust-lang.org/reference/tokens.html#r-lex.token.literal.char-escape.unicode). [↩](#fr-valid-hex-char-1)