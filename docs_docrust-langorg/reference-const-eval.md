---
title: Constant evaluation - The Rust Reference
url: https://doc.rust-lang.org/reference/const_eval.html
source: crawler
fetched_at: 2026-05-06T21:21:47.187496811-03:00
rendered_js: false
word_count: 1308
summary: This document defines the rules for constant evaluation in Rust, specifying which expressions are eligible for compile-time evaluation and the restrictions applied to constant contexts.
tags:
    - rust
    - constant-evaluation
    - compile-time
    - language-reference
    - expressions
    - memory-safety
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Constant evaluation](#constant-evaluation)

Constant evaluation is the process of computing the result of [expressions](https://doc.rust-lang.org/reference/expressions.html) during compilation. Only a subset of all expressions can be evaluated at compile-time.

## [Constant expressions](#constant-expressions)

Certain forms of expressions, called constant expressions, can be evaluated at compile time.

[\[const-eval.const-expr.const-context\]](#r-const-eval.const-expr.const-context "const-eval.const-expr.const-context")

Expressions in a [const context](#const-context) must be constant expressions.

Expressions in const contexts are always evaluated at compile time.

[\[const-eval.const-expr.runtime-context\]](#r-const-eval.const-expr.runtime-context "const-eval.const-expr.runtime-context")

Outside of const contexts, constant expressions *may* be, but are not guaranteed to be, evaluated at compile time.

Behaviors such as out of bounds [array indexing](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions) or [overflow](https://doc.rust-lang.org/reference/expressions/operator-expr.html#overflow) are compiler errors if the value must be evaluated at compile time (i.e. in const contexts). Otherwise, these behaviors are warnings, but will likely panic at run-time.

The following expressions are constant expressions, so long as any operands are also constant expressions and do not cause any [`Drop::drop`](https://doc.rust-lang.org/reference/destructors.html) calls to be run.

- [Literals](https://doc.rust-lang.org/reference/expressions/literal-expr.html).

<!--THE END-->

- [Const parameters](https://doc.rust-lang.org/reference/items/generics.html).

<!--THE END-->

- [Paths](https://doc.rust-lang.org/reference/expressions/path-expr.html) to [functions](https://doc.rust-lang.org/reference/items/functions.html) and [constants](https://doc.rust-lang.org/reference/items/constant-items.html). Recursively defining constants is not allowed.

<!--THE END-->

- Paths to [statics](https://doc.rust-lang.org/reference/items/static-items.html) with these restrictions:
  
  - Writes to `static` items are not allowed in any constant evaluation context.
  - Reads from `extern` statics are not allowed in any constant evaluation context.
  - If the evaluation is *not* carried out in an initializer of a `static` item, then reads from any mutable `static` are not allowed. A mutable `static` is a `static mut` item, or a `static` item with an interior-mutable type.
  
  These requirements are checked only when the constant is evaluated. In other words, having such accesses syntactically occur in const contexts is allowed as long as they never get executed.

<!--THE END-->

- [Tuple expressions](https://doc.rust-lang.org/reference/expressions/tuple-expr.html).

<!--THE END-->

- [Array expressions](https://doc.rust-lang.org/reference/expressions/array-expr.html).

<!--THE END-->

- [Struct expressions](https://doc.rust-lang.org/reference/expressions/struct-expr.html).

<!--THE END-->

- [Block expressions](https://doc.rust-lang.org/reference/expressions/block-expr.html), including `unsafe` and `const` blocks.
  
  - [let statements](https://doc.rust-lang.org/reference/statements.html#let-statements) and thus irrefutable [patterns](https://doc.rust-lang.org/reference/patterns.html), including mutable bindings
  - [assignment expressions](https://doc.rust-lang.org/reference/expressions/operator-expr.html#assignment-expressions)
  - [compound assignment expressions](https://doc.rust-lang.org/reference/expressions/operator-expr.html#compound-assignment-expressions)
  - [expression statements](https://doc.rust-lang.org/reference/statements.html#expression-statements)

<!--THE END-->

- [Field expressions](https://doc.rust-lang.org/reference/expressions/field-expr.html).

<!--THE END-->

- [Array and slice indexing expressions](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions), where the index is a `usize`.

<!--THE END-->

- [Range expressions](https://doc.rust-lang.org/reference/expressions/range-expr.html).

<!--THE END-->

- [Closure expressions](https://doc.rust-lang.org/reference/expressions/closure-expr.html) which don’t capture variables from the environment.

<!--THE END-->

- Built-in [negation](https://doc.rust-lang.org/reference/expressions/operator-expr.html#negation-operators), [arithmetic](https://doc.rust-lang.org/reference/expressions/operator-expr.html#arithmetic-and-logical-binary-operators), [logical](https://doc.rust-lang.org/reference/expressions/operator-expr.html#arithmetic-and-logical-binary-operators), [comparison](https://doc.rust-lang.org/reference/expressions/operator-expr.html#comparison-operators) or [lazy boolean](https://doc.rust-lang.org/reference/expressions/operator-expr.html#lazy-boolean-operators) operators used on integer and floating point types, `bool`, and `char`.

<!--THE END-->

- All forms of [borrow](https://doc.rust-lang.org/reference/expressions/operator-expr.html#borrow-operators)s, including raw borrows, except borrows of expressions whose temporary scopes would be extended (see [temporary lifetime extension](https://doc.rust-lang.org/reference/destructors.html#r-destructors.scope.lifetime-extension)) to the end of the program and which are either:
  
  - Mutable borrows.
  - Shared borrows of expressions that result in values with [interior mutability](https://doc.rust-lang.org/reference/interior-mutability.html).
  
  ```rust
  #![allow(unused)]
  fn main() {
  // Due to being in tail position, this borrow extends the scope of the
  // temporary to the end of the program. Since the borrow is mutable,
  // this is not allowed in a const expression.
  const C: &u8 = &mut 0; // ERROR not allowed
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  // Const blocks are similar to initializers of `const` items.
  let _: &u8 = const { &mut 0 }; // ERROR not allowed
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  use core::sync::atomic::AtomicU8;
  // This is not allowed as 1) the temporary scope is extended to the
  // end of the program and 2) the temporary has interior mutability.
  const C: &AtomicU8 = &AtomicU8::new(0); // ERROR not allowed
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  use core::sync::atomic::AtomicU8;
  // As above.
  let _: &_ = const { &AtomicU8::new(0) }; // ERROR not allowed
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  #![allow(static_mut_refs)]
  // Even though this borrow is mutable, it's not of a temporary, so
  // this is allowed.
  const C: &u8 = unsafe { static mut S: u8 = 0; &mut S }; // OK
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  use core::sync::atomic::AtomicU8;
  // Even though this borrow is of a value with interior mutability,
  // it's not of a temporary, so this is allowed.
  const C: &AtomicU8 = {
      static S: AtomicU8 = AtomicU8::new(0); &S // OK
  };
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  use core::sync::atomic::AtomicU8;
  // This shared borrow of an interior mutable temporary is allowed
  // because its scope is not extended.
  const C: () = { _ = &AtomicU8::new(0); }; // OK
  }
  ```
  
  ```rust
  #![allow(unused)]
  fn main() {
  // Even though the borrow is mutable and the temporary lives to the
  // end of the program due to promotion, this is allowed because the
  // borrow is not in tail position and so the scope of the temporary
  // is not extended via temporary lifetime extension.
  const C: () = { let _: &'static mut [u8] = &mut []; }; // OK
  //                                              ~~
  //                                     Promoted temporary.
  }
  ```
  
  > Note
  > 
  > In other words — to focus on what’s allowed rather than what’s not allowed — shared borrows of interior mutable data and mutable borrows are only allowed in a [const context](#const-context) when the borrowed [place expression](https://doc.rust-lang.org/reference/expressions.html#r-expr.place-value.place-memory-location) is *transient*, *indirect*, or *static*.
  > 
  > A place expression is *transient* if it is a variable local to the current const context or an expression whose temporary scope is contained inside the current const context.
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  // The borrow is of a variable local to the initializer, therefore
  // this place expression is transient.
  const C: () = { let mut x = 0; _ = &mut x; };
  }
  > ```
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  // The borrow is of a temporary whose scope has not been extended,
  // therefore this place expression is transient.
  const C: () = { _ = &mut 0u8; };
  }
  > ```
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  // When a temporary is promoted but not lifetime extended, its
  // place expression is still treated as transient.
  const C: () = { let _: &'static mut [u8] = &mut []; };
  }
  > ```
  > 
  > A place expression is *indirect* if it is a [dereference expression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#r-expr.deref).
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  const C: () = { _ = &mut *(&mut 0); };
  }
  > ```
  > 
  > A place expression is *static* if it is a `static` item.
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  #![allow(static_mut_refs)]
  const C: &u8 = unsafe { static mut S: u8 = 0; &mut S };
  }
  > ```
  
  > Note
  > 
  > One surprising consequence of these rules is that we allow this,
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  const C: &[u8] = { let x: &mut [u8] = &mut []; x }; // OK
  //                                    ~~~~~~~
  // Empty arrays are promoted even behind mutable borrows.
  }
  > ```
  > 
  > but we disallow this similar code:
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  const C: &[u8] = &mut []; // ERROR
  //               ~~~~~~~
  //           Tail expression.
  }
  > ```
  > 
  > The difference between these is that, in the first, the empty array is [promoted](https://doc.rust-lang.org/reference/destructors.html#constant-promotion) but its scope does not undergo [temporary lifetime extension](https://doc.rust-lang.org/reference/destructors.html#r-destructors.scope.lifetime-extension), so we consider the [place expression](https://doc.rust-lang.org/reference/expressions.html#r-expr.place-value.place-memory-location) to be transient (even though after promotion the place indeed lives to the end of the program). In the second, the scope of the empty array temporary does undergo lifetime extension, and so it is rejected due to being a mutable borrow of a lifetime-extended temporary (and therefore borrowing a non-transient place expression).
  > 
  > The effect is surprising because temporary lifetime extension, in this case, causes less code to compile than would without it.
  > 
  > See [issue #143129](https://github.com/rust-lang/rust/issues/143129) for more details.

<!--THE END-->

- [Dereference expressions](https://doc.rust-lang.org/reference/expressions/operator-expr.html#r-expr.deref).
  
  ```rust
  #![allow(unused)]
  fn main() {
  use core::cell::UnsafeCell;
  const _: u8 = unsafe {
      let x: *mut u8 = &raw mut *&mut 0;
      //                        ^^^^^^^
      //             Dereference of mutable reference.
      *x = 1; // Dereference of mutable pointer.
      *(x as *const u8) // Dereference of constant pointer.
  };
  const _: u8 = unsafe {
      let x = &UnsafeCell::new(0);
      *x.get() = 1; // Mutation of interior mutable value.
      *x.get()
  };
  }
  ```

<!--THE END-->

- [Grouped](https://doc.rust-lang.org/reference/expressions/grouped-expr.html) expressions.

<!--THE END-->

- [Cast](https://doc.rust-lang.org/reference/expressions/operator-expr.html#type-cast-expressions) expressions, except
  
  - pointer to address casts and
  - function pointer to address casts.

<!--THE END-->

- Calls of [const functions](https://doc.rust-lang.org/reference/items/functions.html#const-functions) and const methods.

<!--THE END-->

- [loop](https://doc.rust-lang.org/reference/expressions/loop-expr.html#infinite-loops) and [while](https://doc.rust-lang.org/reference/expressions/loop-expr.html#predicate-loops) expressions.

<!--THE END-->

- [if](https://doc.rust-lang.org/reference/expressions/if-expr.html#if-expressions) and [match](https://doc.rust-lang.org/reference/expressions/match-expr.html) expressions.

[\[const-eval.const-context\]](#r-const-eval.const-context "const-eval.const-context")

## [Const context](#const-context)

[\[const-eval.const-context.def\]](#r-const-eval.const-context.def "const-eval.const-context.def")

A *const context* is one of the following:

[\[const-eval.const-context.array-length\]](#r-const-eval.const-context.array-length "const-eval.const-context.array-length")

- [Array type length expressions](https://doc.rust-lang.org/reference/types/array.html)

[\[const-eval.const-context.repeat-length\]](#r-const-eval.const-context.repeat-length "const-eval.const-context.repeat-length")

- [Array repeat length expressions](https://doc.rust-lang.org/reference/expressions/array-expr.html)

[\[const-eval.const-context.init\]](#r-const-eval.const-context.init "const-eval.const-context.init")

- The initializer of
  
  - [constants](https://doc.rust-lang.org/reference/items/constant-items.html)
  - [statics](https://doc.rust-lang.org/reference/items/static-items.html)
  - [enum discriminants](https://doc.rust-lang.org/reference/items/enumerations.html#discriminants)

[\[const-eval.const-context.generic\]](#r-const-eval.const-context.generic "const-eval.const-context.generic")

- A [const generic argument](https://doc.rust-lang.org/reference/items/generics.html#const-generics)

[\[const-eval.const-context.block\]](#r-const-eval.const-context.block "const-eval.const-context.block")

- A [const block](https://doc.rust-lang.org/reference/expressions/block-expr.html#const-blocks)

[\[const-eval.const-context.outer-generics\]](#r-const-eval.const-context.outer-generics "const-eval.const-context.outer-generics")

Array type length expressions, array repeat length expressions, and const generic arguments are restricted in their use of outer generic parameters: such an expression must either be a single const generic parameter, or an expression that does not reference any generic parameters.

## [Const functions](#const-functions)

A *const function* is a function that can be called from a const context. It is defined with the `const` qualifier, and also includes [tuple struct](https://doc.rust-lang.org/reference/items/structs.html) and [tuple enum variant](https://doc.rust-lang.org/reference/items/enumerations.html) constructors.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
const fn square(x: i32) -> i32 { x * x }

const VALUE: i32 = square(12);
}
> ```

[\[const-eval.const-fn.const-context\]](#r-const-eval.const-fn.const-context "const-eval.const-fn.const-context")

When called from a const context, a const function is interpreted by the compiler at compile time. The interpretation happens in the environment of the compilation target and not the host. So `usize` is `32` bits if you are compiling against a `32` bit system, irrelevant of whether you are building on a `64` bit or a `32` bit system.

[\[const-eval.const-fn.outside-context\]](#r-const-eval.const-fn.outside-context "const-eval.const-fn.outside-context")

When a const function is called from outside a const context, it behaves the same as if it did not have the `const` qualifier.

[\[const-eval.const-fn.body-restriction\]](#r-const-eval.const-fn.body-restriction "const-eval.const-fn.body-restriction")

The body of a const function may only use [constant expressions](#constant-expressions).

Const functions are not allowed to be [async](https://doc.rust-lang.org/reference/items/functions.html#async-functions).

The types of a const function’s parameters and return type are restricted to those that are compatible with a const context.