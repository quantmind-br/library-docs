---
title: ir - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/ir/
source: sitemap
fetched_at: 2026-05-07T21:22:00.948054653-03:00
rendered_js: false
word_count: 92
summary: This document describes the register_op decorator function used to define and register new intermediate representation operations within the vLLM framework.
tags:
    - vllm
    - ir-op
    - decorator
    - python-api
    - model-compilation
category: api
---

Register a new vLLM IR op.

:param f: the native implementation of the op :param name: the name of the op, defaults to the function name :param activations: list of activation params, defaults to params starting with 'x' :param allow\_inplace: add a maybe\_inplace overload that allows inplace impls :return: the IrOp object if f is provided, otherwise a decorator

Example usage: \`\`\`python @vllm.ir.register\_op def my\_add(x: torch.Tensor, y: torch.Tensor) -&gt; torch.Tensor: return x + y

@vllm.ir.register\_op(name="custom\_mul") def multiply(x: torch.Tensor, y: torch.Tensor) -&gt; torch.Tensor: return x * y

Source code in `vllm/ir/op.py`

````
defregister_op(
    f: Callable | None = None,
    *,
    name: str | None = None,
    activations: list[str] | None = None,
    allow_inplace: bool = False,
) -> "IrOp | Callable[[Callable], IrOp]":
"""
    Register a new vLLM IR op.

    :param f: the native implementation of the op
    :param name: the name of the op, defaults to the function name
    :param activations: list of activation params, defaults to params starting with 'x'
    :param allow_inplace: add a maybe_inplace overload that allows inplace impls
    :return: the IrOp object if f is provided, otherwise a decorator

    Example usage:
    ```python
    @vllm.ir.register_op
    def my_add(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return x + y


    @vllm.ir.register_op(name="custom_mul")
    def multiply(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return x * y"""

    defdecorator(_f: Callable):
        op_name: str = _f.__name__ if name is None else name
        assert op_name not in IrOp.registry
        if allow_inplace:
            op: IrOp = IrOpInplace(op_name, _f, activations)
        else:
            op = IrOp(op_name, _f, activations)
        IrOp.registry[op_name] = op
        return op

    if f is not None:
        return decorator(f)

    return decorator
````