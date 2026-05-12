---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/lib/utils/
source: sitemap
fetched_at: 2026-05-07T21:15:52.007637934-03:00
rendered_js: false
word_count: 65
summary: This document outlines utility functions for formatting benchmark results for PyTorch OSS integration, managing default vLLM configurations during testing, and detecting torch.compile usage.
tags:
    - vllm
    - benchmarking
    - pytorch-oss
    - configuration
    - utility-functions
    - performance-testing
category: reference
---

## convert\_to\_pytorch\_benchmark\_format [¶](#vllm.benchmarks.lib.utils.convert_to_pytorch_benchmark_format "Permanent link")

Save the benchmark results in the format used by PyTorch OSS benchmark with on metric per record https://github.com/pytorch/pytorch/wiki/How-to-integrate-with-PyTorch-OSS-benchmark-database

Source code in `vllm/benchmarks/lib/utils.py`

```
defconvert_to_pytorch_benchmark_format(
    args: argparse.Namespace, metrics: dict[str, list], extra_info: dict[str, Any]
) -> list:
"""
    Save the benchmark results in the format used by PyTorch OSS benchmark with
    on metric per record
    https://github.com/pytorch/pytorch/wiki/How-to-integrate-with-PyTorch-OSS-benchmark-database
    """
    records = []
    if not os.environ.get("SAVE_TO_PYTORCH_BENCHMARK_FORMAT", False):
        return records

    for name, benchmark_values in metrics.items():
        if not isinstance(benchmark_values, list):
            raise TypeError(
                f"benchmark_values for metric '{name}' must be a list, "
                f"but got {type(benchmark_values).__name__}"
            )

        record = {
            "benchmark": {
                "name": "vLLM benchmark",
                "extra_info": {
                    "args": vars(args),
                    "compilation_config.mode": extract_field(
                        args, extra_info, "compilation_config.mode"
                    ),
                    "optimization_level": extract_field(
                        args, extra_info, "optimization_level"
                    ),
                    # A boolean field used by vLLM benchmark HUD dashboard
                    "use_compile": use_compile(args, extra_info),
                },
            },
            "model": {
                "name": args.model,
            },
            "metric": {
                "name": name,
                "benchmark_values": benchmark_values,
                "extra_info": extra_info,
            },
        }

        tp = record["benchmark"]["extra_info"]["args"].get("tensor_parallel_size")
        # Save tensor_parallel_size parameter if it's part of the metadata
        if not tp and "tensor_parallel_size" in extra_info:
            record["benchmark"]["extra_info"]["args"]["tensor_parallel_size"] = (
                extra_info["tensor_parallel_size"]
            )

        records.append(record)

    return records
```

## default\_vllm\_config [¶](#vllm.benchmarks.lib.utils.default_vllm_config "Permanent link")

Set a default VllmConfig for cases that directly test CustomOps or pathways that use get\_current\_vllm\_config() outside of a full engine context.

Source code in `vllm/benchmarks/lib/utils.py`

```
@contextmanager
defdefault_vllm_config():
"""Set a default VllmConfig for cases that directly test CustomOps or pathways
    that use get_current_vllm_config() outside of a full engine context.
    """
    fromvllm.configimport VllmConfig, set_current_vllm_config

    with set_current_vllm_config(VllmConfig()):
        yield
```

## use\_compile [¶](#vllm.benchmarks.lib.utils.use_compile "Permanent link")

Check if the benchmark is run with torch.compile

Source code in `vllm/benchmarks/lib/utils.py`

```
defuse_compile(args: argparse.Namespace, extra_info: dict[str, Any]) -> bool:
"""
    Check if the benchmark is run with torch.compile
    """
    return not (
        extract_field(args, extra_info, "compilation_config.mode") == "0"
        or "eager" in getattr(args, "output_json", "")
        or "eager" in getattr(args, "result_filename", "")
    )
```