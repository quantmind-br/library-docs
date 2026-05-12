---
title: env_override - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/env_override/
source: sitemap
fetched_at: 2026-05-07T21:21:53.199948911-03:00
rendered_js: false
word_count: 429
summary: This document provides utility functions for patching PyTorch internals and managing environment configurations to ensure compatibility and stability within the vLLM environment.
tags:
    - python
    - patching
    - pytorch
    - environment-configuration
    - cuda
    - vllm-internals
category: reference
---

## \_apply\_constrain\_to\_fx\_strides\_patch [¶](#vllm.env_override._apply_constrain_to_fx_strides_patch "Permanent link")

```
_apply_constrain_to_fx_strides_patch()
```

Patch lowering.constrain\_to\_fx\_strides globally. Safe to call multiple times; only the first call does anything. Only applies for torch &gt;= 2.11 and &lt; 2.12.

Source code in `vllm/env_override.py`

```
def_apply_constrain_to_fx_strides_patch():
"""Patch lowering.constrain_to_fx_strides globally. Safe to call
    multiple times; only the first call does anything.
    Only applies for torch >= 2.11 and < 2.12."""
    global _constrain_to_fx_strides_patched
    if _constrain_to_fx_strides_patched:
        return
    _constrain_to_fx_strides_patched = True

    if not is_torch_equal_or_newer("2.11.0.dev") or is_torch_equal_or_newer(
        "2.12.0.dev"
    ):
        return

    importtorch._inductor.iras_ir
    importtorch._inductor.loweringas_lowering
    fromtorch._inductor.virtualizedimport V as _V

    def_patched(fx_node, *args, **kwargs):
        defapply_constraint(arg, fx_arg):
            if isinstance(arg, _ir.IRNode):
                meta_val = fx_arg.meta.get("val")
                if isinstance(meta_val, torch.Tensor):
                    stride_order = _ir.get_stride_order(
                        meta_val.stride(), _V.graph.sizevars.shape_env
                    )
                    return _ir.ExternKernel.require_stride_order(arg, stride_order)
                return arg
            if isinstance(arg, dict):
                return {key: apply_constraint(arg[key], fx_arg[key]) for key in arg}
            return arg

        args = tuple(
            apply_constraint(arg, fx_arg) for arg, fx_arg in zip(args, fx_node.args)
        )
        kwargs = {k: apply_constraint(v, fx_node.kwargs[k]) for k, v in kwargs.items()}
        return args, kwargs

    _lowering.constrain_to_fx_strides = _patched
```

## \_apply\_cpp\_indirect\_assert\_patch [¶](#vllm.env_override._apply_cpp_indirect_assert_patch "Permanent link")

```
_apply_cpp_indirect_assert_patch()
```

Replace CppVecKernel.indirect\_assert with a fixed copy that uses `VecMask<...>::from(scalar)` for scalar masks.

Idempotent: marks the class with `_vllm_indirect_assert_patched` after the first apply.

Source code in `vllm/env_override.py`

```
def_apply_cpp_indirect_assert_patch():
"""Replace CppVecKernel.indirect_assert with a fixed copy that uses
    `VecMask<...>::from(scalar)` for scalar masks.

    Idempotent: marks the class with `_vllm_indirect_assert_patched` after
    the first apply.
    """
    fromtorch._inductor.codegen.cppimport CppVecKernel

    if getattr(CppVecKernel, "_vllm_indirect_assert_patched", False):
        return

    fromtorch._inductor.codegen.cppimport CppCSEVariable, cexpr_index

    defpatched_indirect_assert(self, var, lower, upper, mask=None):
        assert isinstance(var, CppCSEVariable)
        assert var.dtype is not None
        if not var.is_vec:
            if isinstance(mask, CppCSEVariable) and mask.is_vec:
                mask = f"({mask}).all_masked()"
            return super(CppVecKernel, self).indirect_assert(var, lower, upper, mask)
        lower_scalar = lower
        upper_scalar = upper
        if lower:
            lower = f"{self._get_vec_type(var.dtype)}({lower})"
        if upper:
            upper = f"{self._get_vec_type(var.dtype)}({upper})"
        if lower and upper:
            cond = f"({lower} <= {var}) & ({var} < {upper})"
            cond_print = f"{lower_scalar} <= {var} < {upper_scalar}"
        elif lower:
            cond = f"{lower} <= {var}"
            cond_print = f"{lower_scalar} <= {var}"
        else:
            assert upper
            cond = f"{var} < {upper}"
            cond_print = f"{var} < {upper_scalar}"
        cond = f"{self._get_mask_type(var.dtype)}({cond})"
        if mask:
            if not mask.is_vec:
                # Backport of pytorch/pytorch#178148 -- use ::from for
                # scalar masks so g++ picks the correct overload.
                mask = f"{self._get_mask_type(var.dtype)}::from({mask})"
            cond = f"({cond}) | ~({mask})"
        if self.tail_size:
            cond = (
                f"{self._get_mask_type(var.dtype)}::set("
                f"{self._get_mask_type(var.dtype)}::from(1)"
                f", ({cond}), {cexpr_index(self.tail_size)})"
            )
        cond = f"({cond}).all_masked()"
        return f'{self.assert_function}({cond}, "index out of bounds: {cond_print}")'

    CppVecKernel.indirect_assert = patched_indirect_assert
    CppVecKernel._vllm_indirect_assert_patched = True  # type: ignore[attr-defined]
```

## \_apply\_fxgraphcache\_pickle\_patch [¶](#vllm.env_override._apply_fxgraphcache_pickle_patch "Permanent link")

```
_apply_fxgraphcache_pickle_patch(pickler_cls, bypass_cls)
```

Wrap pickler\_cls.dumps to convert ValueError into bypass\_cls.

Idempotent: sets `_vllm_fxgraph_dumps_patched` on the class after the first apply to prevent re-application. The wrapper function is also marked with `_vllm_patched` as an additional safeguard.

Source code in `vllm/env_override.py`

```
def_apply_fxgraphcache_pickle_patch(pickler_cls, bypass_cls):
"""Wrap pickler_cls.dumps to convert ValueError into bypass_cls.

    Idempotent: sets `_vllm_fxgraph_dumps_patched` on the class after the
    first apply to prevent re-application. The wrapper function is also
    marked with `_vllm_patched` as an additional safeguard.
    """
    if getattr(pickler_cls, "_vllm_fxgraph_dumps_patched", False):
        return

    original_dumps = pickler_cls.dumps
    if hasattr(original_dumps, "_vllm_patched"):
        return

    defpatched_dumps(self, obj):
        try:
            return original_dumps(self, obj)
        except ValueError as e:
            raise bypass_cls("Failed to pickle cache key") frome

    patched_dumps._vllm_patched = True  # type: ignore[attr-defined]
    pickler_cls.dumps = patched_dumps
    pickler_cls._vllm_fxgraph_dumps_patched = True  # type: ignore[attr-defined]
```

## \_get\_torch\_cuda\_version [¶](#vllm.env_override._get_torch_cuda_version "Permanent link")

```
_get_torch_cuda_version()
```

Peripheral function to \_maybe\_set\_cuda\_compatibility\_path(). PyTorch version must not be determined by importing directly because it will trigger the CUDA initialization, losing the chance to set the LD\_LIBRARY\_PATH beforehand.

Source code in `vllm/env_override.py`

```
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36

def_get_torch_cuda_version():
"""Peripheral function to _maybe_set_cuda_compatibility_path().
    PyTorch version must not be determined by importing directly
    because it will trigger the CUDA initialization, losing the
    chance to set the LD_LIBRARY_PATH beforehand.
    """
    try:
        spec = importlib.util.find_spec("torch")
        if not spec:
            return None
        if spec.origin:
            torch_root = os.path.dirname(spec.origin)
        elif spec.submodule_search_locations:
            torch_root = spec.submodule_search_locations[0]
        else:
            return None
        version_path = os.path.join(torch_root, "version.py")
        if not os.path.exists(version_path):
            return None
        # Load the version module without importing torch
        ver_spec = importlib.util.spec_from_file_location("torch.version", version_path)
        if not ver_spec or not ver_spec.loader:
            return None
        module = importlib.util.module_from_spec(ver_spec)
        # Avoid registering in sys.modules to not confuse future imports
        ver_spec.loader.exec_module(module)
        return getattr(module, "cuda", None)
    except Exception:
        return None
```

## \_maybe\_set\_cuda\_compatibility\_path [¶](#vllm.env_override._maybe_set_cuda_compatibility_path "Permanent link")

```
_maybe_set_cuda_compatibility_path()
```

Set LD\_LIBRARY\_PATH for CUDA forward compatibility if enabled.

Must run before 'import torch' since torch loads CUDA shared libraries at import time and the dynamic linker only consults LD\_LIBRARY\_PATH when a library is first loaded.

CUDA forward compatibility is only supported on select professional and datacenter NVIDIA GPUs. Consumer GPUs (GeForce, RTX) do not support it and will get Error 803 if compat libs are loaded.

Source code in `vllm/env_override.py`

```
def_maybe_set_cuda_compatibility_path():
"""Set LD_LIBRARY_PATH for CUDA forward compatibility if enabled.

    Must run before 'import torch' since torch loads CUDA shared libraries
    at import time and the dynamic linker only consults LD_LIBRARY_PATH when
    a library is first loaded.

    CUDA forward compatibility is only supported on select professional and
    datacenter NVIDIA GPUs. Consumer GPUs (GeForce, RTX) do not support it
    and will get Error 803 if compat libs are loaded.
    """
    enable = os.environ.get("VLLM_ENABLE_CUDA_COMPATIBILITY", "0").strip().lower() in (
        "1",
        "true",
    )
    if not enable:
        return

    cuda_compat_path = os.environ.get("VLLM_CUDA_COMPATIBILITY_PATH", "")
    if not cuda_compat_path or not os.path.isdir(cuda_compat_path):
        conda_prefix = os.environ.get("CONDA_PREFIX", "")
        conda_compat = os.path.join(conda_prefix, "cuda-compat")
        if conda_prefix and os.path.isdir(conda_compat):
            cuda_compat_path = conda_compat
    if not cuda_compat_path or not os.path.isdir(cuda_compat_path):
        torch_cuda_version = _get_torch_cuda_version()
        if torch_cuda_version:
            default_path = f"/usr/local/cuda-{torch_cuda_version}/compat"
            if os.path.isdir(default_path):
                cuda_compat_path = default_path
    if not cuda_compat_path or not os.path.isdir(cuda_compat_path):
        return

    norm_path = os.path.normpath(cuda_compat_path)
    existing = os.environ.get("LD_LIBRARY_PATH", "")
    ld_paths = existing.split(os.pathsep) if existing else []

    if ld_paths and ld_paths[0] and os.path.normpath(ld_paths[0]) == norm_path:
        return  # Already at the front

    new_paths = [norm_path] + [
        p for p in ld_paths if not p or os.path.normpath(p) != norm_path
    ]
    os.environ["LD_LIBRARY_PATH"] = os.pathsep.join(new_paths)
```

## \_patch\_cpp\_indirect\_assert\_if\_needed [¶](#vllm.env_override._patch_cpp_indirect_assert_if_needed "Permanent link")

```
_patch_cpp_indirect_assert_if_needed()
```

Apply cpp codegen indirect\_assert backport when on torch 2.11.x.

Defers application until torch.\_inductor.codegen.cpp is naturally imported by Inductor. Importing it eagerly during vllm.**init** pulls in torch.\_inductor.scheduler, whose top-level `import torch._inductor.async_compile` can fail with `ModuleNotFoundError: import of torch._inductor.async_compile halted; None in sys.modules` depending on the import order on the runner (observed in vLLM CPU CI).

Source code in `vllm/env_override.py`

```
def_patch_cpp_indirect_assert_if_needed():
"""Apply cpp codegen indirect_assert backport when on torch 2.11.x.

    Defers application until torch._inductor.codegen.cpp is naturally
    imported by Inductor. Importing it eagerly during vllm.__init__ pulls
    in torch._inductor.scheduler, whose top-level
    `import torch._inductor.async_compile` can fail with
    `ModuleNotFoundError: import of torch._inductor.async_compile halted;
    None in sys.modules` depending on the import order on the runner
    (observed in vLLM CPU CI).
    """
    if not is_torch_equal_or_newer("2.11.0") or is_torch_equal_or_newer("2.12.0.dev"):
        return

    importsys

    target_name = "torch._inductor.codegen.cpp"
    if target_name in sys.modules:
        _apply_cpp_indirect_assert_patch()
        return

    importimportlib.abc

    class_CppCodegenPatchFinder(importlib.abc.MetaPathFinder):
        deffind_spec(self, fullname, path, target=None):
            if fullname != target_name:
                return None
            sys.meta_path.remove(self)
            spec = importlib.util.find_spec(fullname)
            if spec is None or spec.loader is None:
                return None
            original_exec = spec.loader.exec_module

            def_exec_then_patch(module):
                original_exec(module)
                _apply_cpp_indirect_assert_patch()

            spec.loader.exec_module = _exec_then_patch  # type: ignore[method-assign]
            return spec

    sys.meta_path.insert(0, _CppCodegenPatchFinder())
```

## \_patch\_fxgraphcache\_pickle\_if\_needed [¶](#vllm.env_override._patch_fxgraphcache_pickle_if_needed "Permanent link")

```
_patch_fxgraphcache_pickle_if_needed()
```

Apply FxGraphCachePickler.dumps ValueError backport when on torch 2.10.x.

Source code in `vllm/env_override.py`

```
def_patch_fxgraphcache_pickle_if_needed():
"""Apply FxGraphCachePickler.dumps ValueError backport when on torch 2.10.x."""
    fromvllm.utils.torch_utilsimport is_torch_equal_or_newer

    if not is_torch_equal_or_newer("2.10.0") or is_torch_equal_or_newer("2.11.0"):
        return

    fromtorch._inductor.codecacheimport BypassFxGraphCache, FxGraphCachePickler

    _apply_fxgraphcache_pickle_patch(FxGraphCachePickler, BypassFxGraphCache)
```

## \_patch\_get\_raw\_stream\_if\_needed [¶](#vllm.env_override._patch_get_raw_stream_if_needed "Permanent link")

```
_patch_get_raw_stream_if_needed()
```

Workaround for TorchInductor autotune get\_raw\_stream() bug.

Source code in `vllm/env_override.py`

```
def_patch_get_raw_stream_if_needed():
"""Workaround for TorchInductor autotune get_raw_stream() bug."""
    fromvllm.utils.torch_utilsimport is_torch_equal

    # Only apply the patch for torch 2.9.0 or 2.9.1
    if is_torch_equal("2.9.0") or is_torch_equal("2.9.1"):
        importbuiltins

        # Check if CUDA functionality is available without initializing CUDA
        # _cuda_getCurrentRawStream only exists in CUDA builds of PyTorch
        if hasattr(torch._C, "_cuda_getCurrentRawStream"):
            fromtorch._Cimport _cuda_getCurrentRawStream as _get_raw_stream

            builtins.get_raw_stream = _get_raw_stream  # type: ignore[attr-defined]
```

## \_safe\_builtins\_dict [¶](#vllm.env_override._safe_builtins_dict "Permanent link")

```
_safe_builtins_dict(builtins_dict: dict) -> dict
```

Filter a builtins dict to only picklable entries for serialization.

Source code in `vllm/env_override.py`

```
def_safe_builtins_dict(builtins_dict: dict) -> dict:
"""Filter a builtins dict to only picklable entries for serialization."""
    result = {}
    for k, v in builtins_dict.items():
        try:
            pickle.dumps(v)
            result[k] = v
        except Exception:
            pass
    return result
```

## \_update\_scheduler\_patched [¶](#vllm.env_override._update_scheduler_patched "Permanent link")

```
_update_scheduler_patched(self) -> None
```

(Re)initializes the scheduler member. When initializing the scheduler, no CUBIN files should be generated (to avoid biasing any benchmarks and pessimizing fusion decisions).

Source code in `vllm/env_override.py`

```
def_update_scheduler_patched(self) -> None:
    # Copied from torch._inductor.graph.GrahLowering._update_scheduler. Patches
    # this method so that we can patch Scheduler.should_partition with the
    # function above
"""
    (Re)initializes the scheduler member.  When initializing the scheduler, no CUBIN
    files should be generated (to avoid biasing any benchmarks and pessimizing
    fusion decisions).
    """
    importtorch._inductor.configasconfig
    fromtorch._inductor.schedulerimport Scheduler

    Scheduler.should_partition = should_partition_patched
    Scheduler.get_graph_partition_signature = get_graph_partition_signature_patched

    with config.patch("triton.store_cubin", False):
        self.scheduler = Scheduler(self.operations)
```

## get\_graph\_partition\_signature\_patched [¶](#vllm.env_override.get_graph_partition_signature_patched "Permanent link")

```
get_graph_partition_signature_patched(
    self, partitions, skip_cudagraphs: list[bool]
)
```

Gets signature for each graph partition, including input nodes, output nodes, and whether deallocating an input within graph partition.

Source code in `vllm/env_override.py`

```
defget_graph_partition_signature_patched(
    self, partitions, skip_cudagraphs: list[bool]
):
"""
    Gets signature for each graph partition, including input nodes, output nodes, and
    whether deallocating an input within graph partition.
    """
    fromtorch._inductorimport dependencies
    fromtorch._inductor.irimport GraphPartitionSignature, MutationOutput, NoneLayout
    fromtorch._inductor.virtualizedimport V
    fromtorch.utils._ordered_setimport OrderedSet

    signatures = []

    unmet_output_names = OrderedSet(V.graph.get_output_names())
    name_to_node = self.get_name_to_nodes()

    defis_none_layout(buf_name: str) -> bool:
"""
        Checks if buf_name is NoneLayout. Buffers with NoneLayout is not allocated
        so graph partition should not take it as inputs or outputs.
        """
        buf = self.name_to_buf.get(buf_name, None)

        if buf is None:
            return False

        if isinstance(buf.node.layout, NoneLayout):
            if isinstance(buf.node, MutationOutput) and (
                real_name := self.mutation_real_name.get(buf_name, None)
            ):
                return is_none_layout(real_name)

            return True

        return False

    for partition, skip_cudagraph in zip(
        reversed(partitions), reversed(skip_cudagraphs)
    ):
        output_names: OrderedSet[str] = OrderedSet()

        for node in partition:
            output_names.update(node.outputs_by_name.keys())

        returned_output_names = output_names.intersection(unmet_output_names)

        # all reads/writes are partition inputs except those generated
        # within the partition and tensor constants
        read_writes = dependencies.ReadWrites.merge_list(
            [node.read_writes for node in partition]
        )

        # WeakDep is fake dependency on unused buffer. It should not appear
        # in partition_input_names for inputs that are actually read or written.
        partition_input_names = (
            OrderedSet(
                [
                    x.name
                    for x in read_writes.reads | read_writes.writes
                    if not is_none_layout(x.name)
                ]
            )
            - output_names
        )

        partition_input_names = OrderedSet(
            self.mutation_real_name.get(name, name) for name in partition_input_names
        )

        buffer_names_to_free: OrderedSet[str] = OrderedSet()
        for node in partition:
            buffer_names_to_free.update(node.last_usage)

        # buffer_names_to_free may contain buffers allocated in previous
        # graph partitions. These buffers should also be a partition
        # input.
        extra_input_names = [
            name
            for name in (buffer_names_to_free - output_names)
            if name in name_to_node
        ]
        partition_input_names.update(extra_input_names)

        input_nodes = {
            name: name_to_node[name]
            for name in partition_input_names
            if name in name_to_node
        }
        input_deallocation = {
            name: name in buffer_names_to_free
            for name in partition_input_names
            if name in name_to_node
        }

        # if an input tensor is not freed in the partition function, it should
        # also be returned as an output. This brings benefits to cudagraph
        # since the returned output tensor is a cudagraph managed tensor with
        # a static tensor address.
        extra_output_names = [
            name
            for name in partition_input_names
            if name in name_to_node and name not in buffer_names_to_free
        ]

        returned_output_names.update(extra_output_names)

        returned_output_names = OrderedSet(
            self.mutation_real_name.get(name, name) for name in returned_output_names
        )

        output_nodes = [
            name_to_node[name]
            for name in returned_output_names
            if not is_none_layout(name)
        ]

        constant_names = [
            name for name in partition_input_names if name in V.graph.constants
        ]

        symbol_inputs = self.get_graph_partition_symbol_inputs(partition, input_nodes)

        partition_signature = GraphPartitionSignature(
            symbol_inputs,
            input_nodes,
            output_nodes,
            input_deallocation,
            skip_cudagraph,
            constant_names,
        )

        signatures.append(partition_signature)

        unmet_output_names = partition_input_names.union(
            unmet_output_names - returned_output_names
        )

    return signatures[::-1]
```

## should\_partition\_patched [¶](#vllm.env_override.should_partition_patched "Permanent link")

```
should_partition_patched(
    self, node, should_log: bool = False
) -> bool
```

Return True if we should partition the inductor graph on this node

Source code in `vllm/env_override.py`

```
defshould_partition_patched(self, node, should_log: bool = False) -> bool:
    # This is a patched version of
    # torch._inductor.scheduler.Scheduler.should_partition that modifies
    # the following piece of code so that we always return True:
    # https://github.com/pytorch/pytorch/blob/ecb53078faf86ca1b33277df33b82985675bb011/torch/_inductor/scheduler.py#L4712-L4724
"""Return True if we should partition the inductor graph on this node"""

    importtorch._inductor.irasir
    fromtorch._inductor.schedulerimport (
        BaseSchedulerNode,
        FusedSchedulerNode,
    )
    fromtorch._inductor.utilsimport (
        _unstable_customized_partition_wrapper,
        is_cudagraph_unsafe_op,
        maybe_log_cudagraph_partition,
    )

    # Allow users to manually specify if a node should be partitioned
    # Can only do this for FallbackKernels
    ir_node = node.node
    if isinstance(ir_node, torch._inductor.ir.FallbackKernel) and (
        op := ir_node.op_overload
    ):
        op_overload_packet_name = op.name()
        op_overload_name = (
            f"{op_overload_packet_name}.{op._overloadname}"
            if isinstance(op, torch._ops.OpOverload)
            else op_overload_packet_name
        )
        if (
            op_overload_packet_name
            in torch._inductor.config.custom_should_partition_ops
            or op_overload_name in torch._inductor.config.custom_should_partition_ops
        ):
            assert isinstance(op, torch._ops.OpOverload)
            return True

    # When not using cudagraphs, keep all kernels in the `call` function
    # instead of graph partition functions, since graph partition only brings
    # benefit to cudagraph
    if (
        not torch._inductor.config.triton.cudagraphs
        and _unstable_customized_partition_wrapper.wrapper is None
    ):
        return True

    # avoid duplicating logs when should_partition is called multiple times
    # on the same node
    defnoop_log(msg: str, node: BaseSchedulerNode | None) -> None:
        return

    log_partition_reason = maybe_log_cudagraph_partition if should_log else noop_log

    if isinstance(node, FusedSchedulerNode):
        return any(self.should_partition(snode) for snode in node.snodes)

    assert node.node is not None

    if not node.is_gpu():
        log_partition_reason("non gpu ops", node=node)

        return True

    if isinstance(node.node, ir.DeviceCopy):
        log_partition_reason("DeviceCopy ops", node=node)
        return True

    if isinstance(node.node, ir.Conditional):
        log_partition_reason("Conditional ops", node=node)
        return True

    if getattr(node.node, "unbacked_bindings", None):
        log_partition_reason("unbacked binding ops", node=node)
        return True

    if is_cudagraph_unsafe_op(node.node):
        log_partition_reason("CUDAGraph-unsafe custom ops", node=node)
        return True

    return False
```