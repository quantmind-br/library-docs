---
title: codegen - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/codegen/
source: sitemap
fetched_at: 2026-05-07T21:16:12.940461637-03:00
rendered_js: false
word_count: 316
summary: This module provides utilities to generate and compile optimized Python source code from FX GraphModules, reducing execution overhead by replacing interpreter-based stitching with direct function calls.
tags:
    - code-generation
    - fx-graph
    - compilation
    - vllm
    - performance-optimization
    - torch-fx
category: reference
---

## vllm.compilation.codegen [¶](#vllm.compilation.codegen "Permanent link")

Code generation for split\_gm stitching graph execution.

Generates a plain Python function that replaces the FX GraphModule's interpreter-based execution of the stitching graph, eliminating nn.Module.**call** overhead and **getattr** dispatch.

## \_node\_ref [¶](#vllm.compilation.codegen._node_ref "Permanent link")

Convert an FX node argument to a source code reference.

Source code in `vllm/compilation/codegen.py`

```
def_node_ref(arg: Any, consts: list[Any], const_index: dict[int, int]) -> str:
"""Convert an FX node argument to a source code reference."""
    if isinstance(arg, torch.fx.Node):
        return arg.name
    if isinstance(arg, list):
        return f"[{', '.join(_node_ref(x,consts,const_index)forxinarg)}]"
    if isinstance(arg, tuple):
        items = ", ".join(_node_ref(x, consts, const_index) for x in arg)
        return f"({items},)" if len(arg) == 1 else f"({items})"
    if isinstance(arg, dict):
        return (
            "{"
            + ", ".join(
                f"{_node_ref(k,consts,const_index)}: "
                f"{_node_ref(v,consts,const_index)}"
                for k, v in arg.items()
            )
            + "}"
        )
    if isinstance(arg, (int, float, bool, str, bytes, type(None))):
        return repr(arg)
    # Dedup by identity, not equality: safe because FX graph args
    # are live for the entire code-generation pass. Objects stored
    # here must be picklable (for compile-artifact caching).
    key = id(arg)
    if key not in const_index:
        const_index[key] = len(consts)
        consts.append(arg)
    return f"__vllm_consts__[{const_index[key]}]"
```

## compile\_execution\_fn [¶](#vllm.compilation.codegen.compile_execution_fn "Permanent link")

Compile execution code and bind submodule callables.

Parameters:

Name Type Description Default `code` `str`

Python source from generate\_execution\_code().

*required* `submod_callables` `dict[str, Callable[..., Any]]`

Mapping of submodule names to their callables.

*required* `submod_names` `list[str]`

Ordered list of submodule names matching the indices used in the generated code.

*required* `consts` `list[Any] | None`

List of non-primitive constant objects referenced by the generated code via **vllm\_consts**. None for legacy cached code that predates this feature.

`None`

Returns:

Type Description `Callable[..., Any]`

A callable that executes the stitching logic.

Source code in `vllm/compilation/codegen.py`

```
@dynamo_timed("vllm.compile_execution_fn")
defcompile_execution_fn(
    code: str,
    submod_callables: dict[str, Callable[..., Any]],
    submod_names: list[str],
    consts: list[Any] | None = None,
) -> Callable[..., Any]:
"""Compile execution code and bind submodule callables.

    Args:
        code: Python source from generate_execution_code().
        submod_callables: Mapping of submodule names to their callables.
        submod_names: Ordered list of submodule names matching the indices
            used in the generated code.
        consts: List of non-primitive constant objects referenced by the
            generated code via __vllm_consts__. None for legacy cached
            code that predates this feature.

    Returns:
        A callable that executes the stitching logic.
    """
    trace_structured(
        "artifact",
        metadata_fn=lambda: {
            "name": "vllm_execution_code",
            "encoding": "string",
        },
        payload_fn=lambda: code,
    )
    namespace: dict[str, Any] = {}
    if consts is not None:
        namespace["__vllm_consts__"] = consts
    exec(code, namespace)  # noqa: S102
    fn = namespace["execution_fn"]
    # Using .get() is intentional here because only piecewise backend will
    # be stored in submod_callables. The other submodules are inlined and
    # we don't need to bind them to the execution function. Instead, we
    # should use None as placeholder to ensure the list indices are preserved
    # for better debuggability.
    submods_list = [submod_callables.get(name) for name in submod_names]
    return partial(fn, __vllm_submods__=submods_list)
```

## generate\_execution\_code [¶](#vllm.compilation.codegen.generate_execution_code "Permanent link")

Generate Python source code from a split\_gm's stitching graph.

Walks split\_gm.graph.nodes and produces a function that calls submodules via a **vllm\_submods** list, avoiding FX GraphModule overhead and dict lookup cost.

Non-primitive constant arguments (e.g. torch.device, DTensor placement types) are collected into a constants list and referenced by index in the generated code, avoiding reliance on repr() being eval-able.

If a submodule is a plain torch.fx.GraphModule, it is inlined directly in the generated code and we do not need to serialize it in the artifact.

Parameters:

Name Type Description Default `split_gm` `GraphModule`

The split graph module produced by split\_graph().

*required*

Returns:

Type Description `str`

A tuple of (code, submod\_names, consts) where code is the Python

`list[str]`

source, submod\_names is the ordered list of submodule target names

`list[Any]`

corresponding to list indices used in the generated code, and

`tuple[str, list[str], list[Any]]`

consts is a list of non-primitive constant objects referenced

`tuple[str, list[str], list[Any]]`

by the generated code via **vllm\_consts**. These objects are

`tuple[str, list[str], list[Any]]`

kept alive for the lifetime of the compiled function.

Source code in `vllm/compilation/codegen.py`

```
@dynamo_timed("vllm.generate_execution_code")
defgenerate_execution_code(
    split_gm: torch.fx.GraphModule,
) -> tuple[str, list[str], list[Any]]:
"""Generate Python source code from a split_gm's stitching graph.

    Walks split_gm.graph.nodes and produces a function that calls
    submodules via a __vllm_submods__ list, avoiding FX GraphModule overhead
    and dict lookup cost.

    Non-primitive constant arguments (e.g. torch.device, DTensor placement
    types) are collected into a constants list and referenced by index
    in the generated code, avoiding reliance on repr() being eval-able.

    If a submodule is a plain torch.fx.GraphModule, it is inlined directly
    in the generated code and we do not need to serialize it in the artifact.

    Args:
        split_gm: The split graph module produced by split_graph().

    Returns:
        A tuple of (code, submod_names, consts) where code is the Python
        source, submod_names is the ordered list of submodule target names
        corresponding to list indices used in the generated code, and
        consts is a list of non-primitive constant objects referenced
        by the generated code via __vllm_consts__. These objects are
        kept alive for the lifetime of the compiled function.
    """
    code, submod_names, consts = generate_execution_code_with_name(
        split_gm, "execution_fn", with_submod=True
    )
    return "import torch\nimport operator\n" + code, submod_names, consts
```