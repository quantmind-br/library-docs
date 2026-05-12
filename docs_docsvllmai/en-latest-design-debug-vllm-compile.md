---
title: How to debug the vLLM-torch.compile integration
url: https://docs.vllm.ai/en/latest/design/debug_vllm_compile/
source: sitemap
fetched_at: 2026-05-07T21:12:14.925439649-03:00
rendered_js: false
word_count: 1559
summary: This document provides guidance on debugging the vLLM torch.compile integration, including how to use tlparse for log analysis and how to configure flags to isolate and disable specific compilation subsystems.
tags:
    - vllm
    - torch-compile
    - debugging
    - performance-tuning
    - cuda-graphs
    - tlparse
    - dynamic-shapes
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/debug_vllm_compile.md "Edit this page")

TL;DR:

- use tlparse to acquire torch.compile logs. Include these logs in bug reports and/or support asks.
- The vLLM-torch.compile integration is multiple pieces. vLLM exposes flags to turn off each piece:

Online Flag Offline Flag Result --enforce-eager enforce\_eager=True Turn off torch.compile and CUDAGraphs -cc.mode=0 compilation\_config=CompilationConfig(mode=CompilationMode.NONE) Turn off torch.compile only -cc.mode=1 compilation\_config=CompilationConfig(mode=CompilationMode.STOCK\_TORCH\_COMPILE) Turn off vLLM-compile modifications to torch.compile -cc.cudagraph\_mode=NONE compilation\_config=CompilationConfig(cudagraph\_mode=CUDAGraphMode.NONE) Turn off CUDAGraphs only -cc.backend=eager compilation\_config=CompilationConfig(backend='eager') Turn off TorchInductor -cc.ir\_enable\_torch\_wrap=False compilation\_config=CompilationConfig(ir\_enable\_torch\_wrap=False) Turn off vLLM IR wrapping

## vLLM-torch.compile overview[¶](#vllm-torchcompile-overview "Permanent link")

To improve performance, vLLM leverages torch.compile and CUDAGraphs to speed things up. torch.compile generates optimized kernels for PyTorch code while CUDAGraphs eliminates overhead. Most notably, vLLM-compile is NOT torch.compile, it is a custom compiler built using internal PyTorch Compile APIs.

[![vLLM-compile diagram](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/design_diagram.png)](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/design_diagram.png)

- Given a model, we do a full graph capture via TorchDynamo that is dynamic on the batch size (number of tokens)
- vLLM then optionally splits and/or specializes this graph and then uses TorchInductor to compile each graph into a compiled artifact. This step may use vLLM custom Inductor passes to further optimize the graph. This includes vLLM IR lowering to remove dispatch overhead.
- The compiled artifact is saved to vLLM's compile cache so that it can be loaded in the future.
- vLLM applies CUDAGraphs to reduce CPU overheads.

Things can go wrong in each of the four steps. When something does go wrong, please try to isolate the subsystem that went wrong -- this will allow you to turn off the minimal number of things to keep reliability goals while minimizing impact to performance and also helps us (vLLM) when you open a bug report.

For more details on the design, please see the following resources:

- [Introduction to vLLM-torch.compile blogpost](https://blog.vllm.ai/2025/08/20/torch-compile.html)
- [vLLM-torch.compile integration design](https://docs.vllm.ai/en/latest/design/torch_compile/)
- [vLLM IR design](https://docs.vllm.ai/en/latest/design/vllm_ir/)
- [vLLM Office Hours #26](https://www.youtube.com/live/xLyxc7hxCJc?si=Xulo9pe53C6ywf0V&t=561)
- [Talk at PyTorch Conference 2025](https://youtu.be/1wV1ESbGrVQ?si=s1GqymUfwiwOrDTg&t=725)

## Use tlparse[¶](#use-tlparse "Permanent link")

Use [tlparse](https://github.com/meta-pytorch/tlparse) to view torch.compile logs. These logs show all stages of the compilation process, including the fused kernels that torch.compile produces.

Install tlparse:

To enable the torch.compile logs, you can set the envvar `TORCH_TRACE=<dir>`. During tracing, a file per rank will be created inside of that directory, with each file containing the artifacts during compilation. If you can, we recommend sending these log files along with bug reports -- they are very helpful.

Usage (offline inference)

```
TORCH_TRACE=~/trace_dirpythonmy_script.py
tlparse~/trace_dir/<rank_0_log_file>
```

Usage (serving)

```
TORCH_TRACE=~/trace_dirvllmserve
# ctrl-c out of the server
tlparse~/trace_dir/<rank_0_log_file>
```

Given one of the log files, the `tlparse` command outputs some HTML files (perhaps into e.g. `./tl_out/index.html`). Open it to see the logs. It'll look something like the following:

[![tlparse example](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/tlparse_inductor.png)](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/tlparse_inductor.png)

## Turn off vLLM-torch.compile integration[¶](#turn-off-vllm-torchcompile-integration "Permanent link")

Pass `--enforce-eager` to turn off the vLLM-torch.compile integration and run entirely in eager mode. This includes turning off CUDAGraphs.

```
# Online
vllmserve--enforce-eager

# Offline
LLM(model, enforce_eager=True)
```

To turn off just torch.compile, pass `mode = NONE` to the compilation config. (`-cc` is short for `--compilation_config`):

```
# Online
vllmserve-cc.mode=0

# Offline
fromvllm.config.compilationimport CompilationConfig, CompilationMode
LLM(model, compilation_config=CompilationConfig(mode=CompilationMode.NONE))
```

To turn off just CUDAGraphs, pass `cudagraph_mode = NONE`:

```
# Online
vllmserve-cc.cudagraph_mode=NONE

# Offline
fromvllm.config.compilationimport CompilationConfig, CUDAGraphMode
LLM(model, compilation_config=CompilationConfig(cudagraph_mode=CUDAGraphMode.NONE))
```

vLLM IR makes heavy use of the compilation pipeline, from functionalization, custom fusions, and lowering. To turn that off and capture eager-mode dispatching behavior of vLLM IR, run with `ir_enable_torch_wrap=False`. IR torch wrap is only enabled by default when using `mode=VLLM_COMPILE` and `backend="inductor"` (default).

```
# Online
vllmserve-cc.ir_enable_torch_wrap=False

# Offline
fromvllm.config.compilationimport CompilationConfig
LLM(model, compilation_config=CompilationConfig(ir_enable_torch_wrap=False))
```

## Debugging TorchDynamo[¶](#debugging-torchdynamo "Permanent link")

vLLM requires model code be capturable into a full graph via TorchDynamo (torch.compile's frontend). TorchDynamo does not support all of Python. It will error (in fullgraph mode) if it cannot support a feature (this is sometimes known as a graph break).

If you encounter a graph break, please [open an issue to pytorch/pytorch](https://github.com/pytorch/pytorch) so the PyTorch devs can prioritize. Then, try your best to rewrite the code to avoid the graph break. For more information, see this [Dynamo guide](https://docs.pytorch.org/docs/stable/compile/programming_model.dynamo_core_concepts.html).

## Debugging Dynamic Shape full graph capture[¶](#debugging-dynamic-shape-full-graph-capture "Permanent link")

vLLM requires that the model's forward pass be capturable into a full graph that is dynamic on the batch size (i.e. the number of tokens). It (by default) compiles this one graph into one artifact and uses this artifact for all batch sizes.

If your code cannot be captured with Dynamic Shapes, you may see silent incorrectness, loud errors, or CUDA illegal memory accesses. For example, the following is not capturable into a single graph:

```
if data.size[0] % 128 == 0:
    foo(...)
else:
    bar(...)
```

This problem is easy to diagnose. Use tlparse and click on `compilation_metrics`: it will tell you symbolic constraints on the batch size. If there is any constraint that restricts the batch sizes, then we've got a problem.

[![Bad tlparse example](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/dynamic_shapes.png)](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/dynamic_shapes.png)

To avoid this, please either:

1. avoid branching on the number of tokens
2. wrap the branching logic into a custom operator. TorchDynamo does not trace into custom operators.

## Debugging constraint violations and dynamic shapes guards issues[¶](#debugging-constraint-violations-and-dynamic-shapes-guards-issues "Permanent link")

Dynamic-shape guards are a specific category of Dynamo guards. They are constraints that `torch.compile` attaches to dynamic dimensions (e.g., `seq_len`) to ensure the compiled artifact remains valid. These guards typically appear when framework code, custom passes, or user code branches based on dynamic shape values.

**Example:**

```
if x > 10:
    # path A
else:
    # path B
```

This creates a guard `x > 10` or `x <= 10` depending on which path was traced.

**vLLM's Assumption:** vLLM assumes that all guards added by torch.compile are safe to drop and will not constrain the compiled graph to specific input shapes. When this assumption is violated, it can cause issues that users need to debug. Some side effects that indicates this assumption is violated are runtime errors or `ConstraintViolationErrors`.

A `ConstraintViolationErrors` will be thrown if a dynamic shape gets constrained to a single value. If you encounter a constraint violation error or suspect that a dynamic shapes guard is being added incorrectly, you can use stricter dynamic shape modes to help debug the issue:

```
# Online - using unbacked mode
vllmservemeta-llama/Llama-3.2-1B-cc.dynamic_shapes_config.type=unbacked

# Online - using backed_size_oblivious mode
vllmservemeta-llama/Llama-3.2-1B-cc.dynamic_shapes_config.type=backed_size_oblivious

# Offline - using unbacked mode
fromvllm.config.compilationimport CompilationConfig, DynamicShapesConfig, DynamicShapesType
LLM(model, compilation_config=CompilationConfig(
    dynamic_shapes_config=DynamicShapesConfig(type=DynamicShapesType.UNBACKED)
))

# Offline - using backed_size_oblivious mode
fromvllm.config.compilationimport CompilationConfig, DynamicShapesConfig, DynamicShapesType
LLM(model, compilation_config=CompilationConfig(
    dynamic_shapes_config=DynamicShapesConfig(type=DynamicShapesType.BACKED_SIZE_OBLIVIOUS)
))
```

These modes are stricter and reduce or eliminate the need of dynamic shapes guarding, which can help isolate issues:

- `unbacked`: Uses unbacked symints which don't allow guards, making it easier to identify where guards are being incorrectly added
- `backed_size_oblivious`: Uses a mode that is stricter about guarding.

For more details on dynamic shapes modes, see [Dynamic shapes and vLLM guard dropping](https://docs.vllm.ai/en/latest/design/torch_compile/#dynamic-shapes-and-vllm-guard-dropping).

### Printing guards[¶](#printing-guards "Permanent link")

To see all guards that are being added during compilation, you can use `TORCH_LOGS=+dynamic`:

```
TORCH_LOGS=+dynamicvllmservemeta-llama/Llama-3.2-1B
```

Look for `[guard added]` in the logs to see where guards are being added. This can help you identify which operations are causing guards to be added incorrectly.

## Debugging TorchInductor[¶](#debugging-torchinductor "Permanent link")

TorchInductor takes a captured graph and then compiles it down to some Python code that may call 1+ triton kernels. On rare (but unfortunate) occasions, it may produce an incorrect triton kernel. This may manifest as silent incorrectness, CUDA illegal memory accesses, or loud errors.

### Inductor runtime assertions[¶](#inductor-runtime-assertions "Permanent link")

By default (on torch &lt; 2.12), vLLM disables Inductor's runtime assertions (`assert_size_stride`, `assert_alignment`) to avoid ~2ms overhead per forward pass on large models. Setting `VLLM_LOGGING_LEVEL=DEBUG` automatically re-enables them so debugging sessions get full shape/stride validation:

```
VLLM_LOGGING_LEVEL=DEBUGvllmserve<model>
```

You can also override them explicitly via `--compilation-config`:

```
vllmserve<model>-cc.inductor_compile_config='{"size_asserts": true, "alignment_asserts": true, "scalar_asserts": true}'
```

On torch &gt;= 2.12, PyTorch uses an efficient assert-once strategy and these flags are no longer suppressed by vLLM.

To debug if TorchInductor is at fault, you can disable it by passing `backend='eager'` to the compilation config:

```
# online
vllmserve-cc.backend=eager

# offline
LLM(compilation_config=CompilationConfig(backend='eager'))
```

If Inductor is at fault, [file a bug to PyTorch](https://github.com/pytorch/pytorch). If you're feeling adventurous, you can debug the triton kernels in the Inductor output code (that you can locate via using tlparse).

[![tlparse example](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/tlparse_inductor.png)](https://docs.vllm.ai/en/latest/assets/design/debug_vllm_compile/tlparse_inductor.png)

You can also use `TORCH_LOGS=output_code <command>` to print the Inductor output code.

### Editable TorchInductor code[¶](#editable-torchinductor-code "Permanent link")

You can edit the TorchInductor code that gets run by setting `VLLM_COMPILE_CACHE_SAVE_FORMAT=unpacked` or passing `-cc.compile_cache_save_format=unpacked`. The default is `binary`, which means it is not editable.

This is a useful technique: you can put breakpoints (e.g. `torch.distributed.breakpoint()`) and print statements in the output code.

## Debugging vLLM-compile cache[¶](#debugging-vllm-compile-cache "Permanent link")

vLLM built its own cache for torch.compile artifacts. The idea is that the artifacts can be compiled once and then reused after they have been compiled. This is a layer on top of [torch.compile's compiler cache](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html).

While torch.compile's compiler cache is rock-stable, vLLM's compiler cache is unfortunately not always correct. You can disable it via setting `VLLM_DISABLE_COMPILE_CACHE=1`.

You can also manually remove this cache.

- Remove vLLM's compile cache with `rm -rf ~/.cache/vllm` (look at logs to see if the location changed)
- Remove torch.compile's built-in caches with `rm -rf /tmp/torchinductor_$(whoami)`

vLLM's cache is a mapping from cache key to a compiled artifact. vLLM computes the cache key via combining multiple factors (e.g. config flags and model name). If vLLM's compile cache is wrong, this usually means that a factor is missing. Please see [this example](https://github.com/vllm-project/vllm/blob/18b39828d90413d05d770dfd2e2f48304f4ca0eb/vllm/config/model.py#L310) of how vLLM computes part of the cache key.

vLLM's compilation cache requires that the code being compiled ends up being serializable. If this is not the case, then it will error out on save. Usually the fixes are to either:

- rewrite the non-serializable pieces (perhaps difficult because it's difficult to tell right now what is serializable and what isn't)
- file a bug report
- ignore the error by setting `VLLM_DISABLE_COMPILE_CACHE=1` (note that this will make warm server starts a lot slower).

## Debugging CUDAGraphs[¶](#debugging-cudagraphs "Permanent link")

CUDAGraphs is a feature that allows one to:

- Capture a callable that launches 1+ CUDA kernels into a CUDAGraph
- Replay the CUDAGraph

The captured CUDAGraph contains all of the memory used during the capture process. The replay of the CUDAGraph reads and writes to exactly the same regions of memory.

This leads to some restrictions:

1. In order to use CUDAGraphs on new data, you'll need to copy the data into a buffer that the CUDAGraph is reading from
2. CUDAGraphs only capture CUDA kernels, they don't capture work done on CPU.

vLLM uses the raw CUDAGraphs API, which is unsafe when used incorrectly.

To turn off just CUDAGraphs, pass `cudagraph_mode = NONE`:

```
# Online
vllmserve-cc.cudagraph_mode=NONE

# Offline
fromvllm.config.compilationimport CompilationConfig, CUDAGraphMode
LLM(model, compilation_config=CompilationConfig(cudagraph_mode=CUDAGraphMode.NONE))
```