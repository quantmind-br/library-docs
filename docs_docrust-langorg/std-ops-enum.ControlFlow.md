---
title: ControlFlow in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/enum.ControlFlow.html
source: crawler
fetched_at: 2026-05-06T21:31:54.891116888-03:00
rendered_js: false
word_count: 516
summary: The ControlFlow enum provides a standard mechanism for operations to signal whether execution should continue or terminate early, commonly used in visitors and traversals.
tags:
    - rust
    - control-flow
    - enum
    - early-exit
    - traversal
    - language-features
category: reference
---

## Enum ControlFlow

1.55.0 · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#89)

```rust
pub enum ControlFlow<B, C = ()> {
    Continue(C),
    Break(B),
}
```

Expand description

Used to tell an operation whether it should exit early or go on as usual.

This is used when exposing things (like graph traversals or visitors) where you want the user to be able to choose whether to exit early. Having the enum makes it clearer – no more wondering “wait, what did `false` mean again?” – and allows including a value.

Similar to [`Option`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option") and [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result"), this enum can be used with the `?` operator to return immediately if the [`Break`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Break "variant std::ops::ControlFlow::Break") variant is present or otherwise continue normally with the value inside the [`Continue`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Continue "variant std::ops::ControlFlow::Continue") variant.

## [§](#examples)Examples

Early-exiting from [`Iterator::try_for_each`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_for_each "method std::iter::Iterator::try_for_each"):

```rust
use std::ops::ControlFlow;

let r = (2..100).try_for_each(|x| {
    if 403 % x == 0 {
        return ControlFlow::Break(x)
    }

    ControlFlow::Continue(())
});
assert_eq!(r, ControlFlow::Break(13));
```

A basic tree traversal:

```rust
use std::ops::ControlFlow;

pub struct TreeNode<T> {
    value: T,
    left: Option<Box<TreeNode<T>>>,
    right: Option<Box<TreeNode<T>>>,
}

impl<T> TreeNode<T> {
    pub fn traverse_inorder<B>(&self, f: &mut impl FnMut(&T) -> ControlFlow<B>) -> ControlFlow<B> {
        if let Some(left) = &self.left {
            left.traverse_inorder(f)?;
        }
        f(&self.value)?;
        if let Some(right) = &self.right {
            right.traverse_inorder(f)?;
        }
        ControlFlow::Continue(())
    }
    fn leaf(value: T) -> Option<Box<TreeNode<T>>> {
        Some(Box::new(Self { value, left: None, right: None }))
    }
}

let node = TreeNode {
    value: 0,
    left: TreeNode::leaf(1),
    right: Some(Box::new(TreeNode {
        value: -1,
        left: TreeNode::leaf(5),
        right: TreeNode::leaf(2),
    }))
};
let mut sum = 0;

let res = node.traverse_inorder(&mut |val| {
    if *val < 0 {
        ControlFlow::Break(*val)
    } else {
        sum += *val;
        ControlFlow::Continue(())
    }
});
assert_eq!(res, ControlFlow::Break(-1));
assert_eq!(sum, 6);
```

[§](#variant.Continue)1.55.0

Move on to the next phase of the operation as normal.

[§](#variant.Break)1.55.0

Exit the operation without running subsequent phases.

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#141)[§](#impl-ControlFlow%3CB,+C%3E)

1.59.0 (const: 1.95.0) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#155)

Returns `true` if this is a `Break` variant.

##### [§](#examples-1)Examples

```rust
use std::ops::ControlFlow;

assert!(ControlFlow::<&str, i32>::Break("Stop right there!").is_break());
assert!(!ControlFlow::<&str, i32>::Continue(3).is_break());
```

1.59.0 (const: 1.95.0) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#172)

Returns `true` if this is a `Continue` variant.

##### [§](#examples-2)Examples

```rust
use std::ops::ControlFlow;

assert!(!ControlFlow::<&str, i32>::Break("Stop right there!").is_continue());
assert!(ControlFlow::<&str, i32>::Continue(3).is_continue());
```

1.83.0 (const: [unstable](https://github.com/rust-lang/rust/issues/148739 "Tracking issue for const_control_flow")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#190-192)

Converts the `ControlFlow` into an `Option` which is `Some` if the `ControlFlow` was `Break` and `None` otherwise.

##### [§](#examples-3)Examples

```rust
use std::ops::ControlFlow;

assert_eq!(ControlFlow::<&str, i32>::Break("Stop right there!").break_value(), Some("Stop right there!"));
assert_eq!(ControlFlow::<&str, i32>::Continue(3).break_value(), None);
```

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#268)

🔬This is a nightly-only experimental API. (`control_flow_ok` [#140266](https://github.com/rust-lang/rust/issues/140266))

Converts the `ControlFlow` into a `Result` which is `Ok` if the `ControlFlow` was `Break` and `Err` if otherwise.

##### [§](#examples-4)Examples

```rust
#![feature(control_flow_ok)]

use std::ops::ControlFlow;

struct TreeNode<T> {
    value: T,
    left: Option<Box<TreeNode<T>>>,
    right: Option<Box<TreeNode<T>>>,
}

impl<T> TreeNode<T> {
    fn find<'a>(&'a self, mut predicate: impl FnMut(&T) -> bool) -> Result<&'a T, ()> {
        let mut f = |t: &'a T| -> ControlFlow<&'a T> {
            if predicate(t) {
                ControlFlow::Break(t)
            } else {
                ControlFlow::Continue(())
            }
        };

        self.traverse_inorder(&mut f).break_ok()
    }

    fn traverse_inorder<'a, B>(
        &'a self,
        f: &mut impl FnMut(&'a T) -> ControlFlow<B>,
    ) -> ControlFlow<B> {
        if let Some(left) = &self.left {
            left.traverse_inorder(f)?;
        }
        f(&self.value)?;
        if let Some(right) = &self.right {
            right.traverse_inorder(f)?;
        }
        ControlFlow::Continue(())
    }

    fn leaf(value: T) -> Option<Box<TreeNode<T>>> {
        Some(Box::new(Self {
            value,
            left: None,
            right: None,
        }))
    }
}

let node = TreeNode {
    value: 0,
    left: TreeNode::leaf(1),
    right: Some(Box::new(TreeNode {
        value: -1,
        left: TreeNode::leaf(5),
        right: TreeNode::leaf(2),
    })),
};

let res = node.find(|val: &i32| *val > 3);
assert_eq!(res, Ok(&5));
```

1.83.0 (const: [unstable](https://github.com/rust-lang/rust/issues/148739 "Tracking issue for const_control_flow")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#280-282)

Maps `ControlFlow<B, C>` to `ControlFlow<T, C>` by applying a function to the break value in case it exists.

1.83.0 (const: [unstable](https://github.com/rust-lang/rust/issues/148739 "Tracking issue for const_control_flow")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#304-306)

Converts the `ControlFlow` into an `Option` which is `Some` if the `ControlFlow` was `Continue` and `None` otherwise.

##### [§](#examples-5)Examples

```rust
use std::ops::ControlFlow;

assert_eq!(ControlFlow::<&str, i32>::Break("Stop right there!").continue_value(), None);
assert_eq!(ControlFlow::<&str, i32>::Continue(3).continue_value(), Some(3));
```

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#381)

🔬This is a nightly-only experimental API. (`control_flow_ok` [#140266](https://github.com/rust-lang/rust/issues/140266))

Converts the `ControlFlow` into a `Result` which is `Ok` if the `ControlFlow` was `Continue` and `Err` if otherwise.

##### [§](#examples-6)Examples

```rust
#![feature(control_flow_ok)]

use std::ops::ControlFlow;

struct TreeNode<T> {
    value: T,
    left: Option<Box<TreeNode<T>>>,
    right: Option<Box<TreeNode<T>>>,
}

impl<T> TreeNode<T> {
    fn validate<B>(&self, f: &mut impl FnMut(&T) -> ControlFlow<B>) -> Result<(), B> {
        self.traverse_inorder(f).continue_ok()
    }

    fn traverse_inorder<B>(&self, f: &mut impl FnMut(&T) -> ControlFlow<B>) -> ControlFlow<B> {
        if let Some(left) = &self.left {
            left.traverse_inorder(f)?;
        }
        f(&self.value)?;
        if let Some(right) = &self.right {
            right.traverse_inorder(f)?;
        }
        ControlFlow::Continue(())
    }

    fn leaf(value: T) -> Option<Box<TreeNode<T>>> {
        Some(Box::new(Self {
            value,
            left: None,
            right: None,
        }))
    }
}

let node = TreeNode {
    value: 0,
    left: TreeNode::leaf(1),
    right: Some(Box::new(TreeNode {
        value: -1,
        left: TreeNode::leaf(5),
        right: TreeNode::leaf(2),
    })),
};

let res = node.validate(&mut |val| {
    if *val < 0 {
        return ControlFlow::Break("negative value detected");
    }

    if *val > 4 {
        return ControlFlow::Break("too big value detected");
    }

    ControlFlow::Continue(())
});
assert_eq!(res, Err("too big value detected"));
```

1.83.0 (const: [unstable](https://github.com/rust-lang/rust/issues/148739 "Tracking issue for const_control_flow")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#393-395)

Maps `ControlFlow<B, C>` to `ControlFlow<B, T>` by applying a function to the continue value in case it exists.

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#404)[§](#impl-ControlFlow%3CT,+T%3E)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#418)

🔬This is a nightly-only experimental API. (`control_flow_into_value` [#137461](https://github.com/rust-lang/rust/issues/137461))

Extracts the value `T` that is wrapped by `ControlFlow<T, T>`.

##### [§](#examples-7)Examples

```rust
#![feature(control_flow_into_value)]
use std::ops::ControlFlow;

assert_eq!(ControlFlow::<i32, i32>::Break(1024).into_value(), 1024);
assert_eq!(ControlFlow::<i32, i32>::Continue(512).into_value(), 512);
```

1.55.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#88)[§](#impl-Clone-for-ControlFlow%3CB,+C%3E)

1.55.0 · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#87)[§](#impl-Debug-for-ControlFlow%3CB,+C%3E)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#127)[§](#impl-FromResidual%3CControlFlow%3CB,+Infallible%3E%3E-for-ControlFlow%3CB,+C%3E)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#129)[§](#method.from_residual)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/std/ops/trait.FromResidual.html#tymethod.from_residual)

1.55.0 · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#87)[§](#impl-Hash-for-ControlFlow%3CB,+C%3E)

1.55.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#88)[§](#impl-PartialEq-for-ControlFlow%3CB,+C%3E)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#88)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#137)[§](#impl-Residual%3CC%3E-for-ControlFlow%3CB,+Infallible%3E)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#138)[§](#associatedtype.TryType)

🔬This is a nightly-only experimental API. (`try_trait_v2_residual` [#91285](https://github.com/rust-lang/rust/issues/91285))

The “return” type of this meta-function.

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#105)[§](#impl-Try-for-ControlFlow%3CB,+C%3E)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#106)[§](#associatedtype.Output)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

The type of the value produced by `?` when *not* short-circuiting.

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#107)[§](#associatedtype.Residual)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#110)[§](#method.from_output)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from its `Output` type. [Read more](https://doc.rust-lang.org/std/ops/trait.Try.html#tymethod.from_output)

[Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#115)[§](#method.branch)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Used in `?` to decide whether the operator should produce a value (because this returned [`ControlFlow::Continue`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Continue "variant std::ops::ControlFlow::Continue")) or propagate a value back to the caller (because this returned [`ControlFlow::Break`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Break "variant std::ops::ControlFlow::Break")). [Read more](https://doc.rust-lang.org/std/ops/trait.Try.html#tymethod.branch)

1.55.0 · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#87)[§](#impl-Copy-for-ControlFlow%3CB,+C%3E)

1.55.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#88)[§](#impl-Eq-for-ControlFlow%3CB,+C%3E)

1.55.0 · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#88)[§](#impl-StructuralPartialEq-for-ControlFlow%3CB,+C%3E)