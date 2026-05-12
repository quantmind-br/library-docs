---
title: std::cmp - Rust
url: https://doc.rust-lang.org/stable/std/cmp/index.html
source: crawler
fetched_at: 2026-05-06T21:25:30.69981955-03:00
rendered_js: false
word_count: 392
summary: This module provides essential traits, enums, and functions for comparing, ordering, and finding the extrema of values in Rust.
tags:
    - rust
    - comparison
    - ordering
    - traits
    - operators
category: reference
---

## Module cmp

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#273)

Expand description

Utilities for comparing and ordering values.

This module contains various tools for comparing and ordering values. In summary:

- [`PartialEq<Rhs>`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") overloads the `==` and `!=` operators. In cases where `Rhs` (the right hand side’s type) is `Self`, this trait corresponds to a partial equivalence relation.
- [`Eq`](https://doc.rust-lang.org/stable/std/cmp/trait.Eq.html "trait std::cmp::Eq") indicates that the overloaded `==` operator corresponds to an equivalence relation.
- [`Ord`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord") and [`PartialOrd`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") are traits that allow you to define total and partial orderings between values, respectively. Implementing them overloads the `<`, `<=`, `>`, and `>=` operators.
- [`Ordering`](https://doc.rust-lang.org/stable/std/cmp/enum.Ordering.html "enum std::cmp::Ordering") is an enum returned by the main functions of [`Ord`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord") and [`PartialOrd`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd"), and describes an ordering of two values (less, equal, or greater).
- [`Reverse`](https://doc.rust-lang.org/stable/std/cmp/struct.Reverse.html "struct std::cmp::Reverse") is a struct that allows you to easily reverse an ordering.
- [`max`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html#method.max "method std::cmp::Ord::max") and [`min`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html#method.min "method std::cmp::Ord::min") are functions that build off of [`Ord`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord") and allow you to find the maximum or minimum of two values.

For more details, see the respective documentation of each item in the list.

[Reverse](https://doc.rust-lang.org/stable/std/cmp/struct.Reverse.html "struct std::cmp::Reverse")

A helper struct for reverse ordering.

[Ordering](https://doc.rust-lang.org/stable/std/cmp/enum.Ordering.html "enum std::cmp::Ordering")

An `Ordering` is the result of a comparison between two values.

[Eq](https://doc.rust-lang.org/stable/std/cmp/trait.Eq.html "trait std::cmp::Eq")

Trait for comparisons corresponding to [equivalence relations](https://en.wikipedia.org/wiki/Equivalence_relation).

[Ord](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord")

Trait for types that form a [total order](https://en.wikipedia.org/wiki/Total_order).

[PartialEq](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq")

Trait for comparisons using the equality operator.

[PartialOrd](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd")

Trait for types that form a [partial order](https://en.wikipedia.org/wiki/Partial_order).

[max](https://doc.rust-lang.org/stable/std/cmp/fn.max.html "fn std::cmp::max")

Compares and returns the maximum of two values.

[max\_by](https://doc.rust-lang.org/stable/std/cmp/fn.max_by.html "fn std::cmp::max_by")

Returns the maximum of two values with respect to the specified comparison function.

[max\_by\_key](https://doc.rust-lang.org/stable/std/cmp/fn.max_by_key.html "fn std::cmp::max_by_key")

Returns the element that gives the maximum value from the specified function.

[min](https://doc.rust-lang.org/stable/std/cmp/fn.min.html "fn std::cmp::min")

Compares and returns the minimum of two values.

[min\_by](https://doc.rust-lang.org/stable/std/cmp/fn.min_by.html "fn std::cmp::min_by")

Returns the minimum of two values with respect to the specified comparison function.

[min\_by\_key](https://doc.rust-lang.org/stable/std/cmp/fn.min_by_key.html "fn std::cmp::min_by_key")

Returns the element that gives the minimum value from the specified function.

[minmax](https://doc.rust-lang.org/stable/std/cmp/fn.minmax.html "fn std::cmp::minmax")Experimental

Compares and sorts two values, returning minimum and maximum.

[minmax\_by](https://doc.rust-lang.org/stable/std/cmp/fn.minmax_by.html "fn std::cmp::minmax_by")Experimental

Returns minimum and maximum values with respect to the specified comparison function.

[minmax\_by\_key](https://doc.rust-lang.org/stable/std/cmp/fn.minmax_by_key.html "fn std::cmp::minmax_by_key")Experimental

Returns minimum and maximum values with respect to the specified key function.

[Eq](https://doc.rust-lang.org/stable/std/cmp/derive.Eq.html "derive std::cmp::Eq")

Derive macro generating an impl of the trait [`Eq`](https://doc.rust-lang.org/stable/std/cmp/trait.Eq.html "trait std::cmp::Eq").

[Ord](https://doc.rust-lang.org/stable/std/cmp/derive.Ord.html "derive std::cmp::Ord")

Derive macro generating an impl of the trait [`Ord`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord"). The behavior of this macro is described in detail [here](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html#derivable "trait std::cmp::Ord").

[PartialEq](https://doc.rust-lang.org/stable/std/cmp/derive.PartialEq.html "derive std::cmp::PartialEq")

Derive macro generating an impl of the trait [`PartialEq`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq"). The behavior of this macro is described in detail [here](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html#derivable "trait std::cmp::PartialEq").

[PartialOrd](https://doc.rust-lang.org/stable/std/cmp/derive.PartialOrd.html "derive std::cmp::PartialOrd")

Derive macro generating an impl of the trait [`PartialOrd`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd"). The behavior of this macro is described in detail [here](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#derivable "trait std::cmp::PartialOrd").