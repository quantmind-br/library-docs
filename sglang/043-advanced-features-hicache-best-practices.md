---
title: SGLang HiCache Best Practices — SGLang
url: https://docs.sglang.io/advanced_features/hicache_best_practices.html
source: crawler
fetched_at: 2026-02-04T08:47:48.625059127-03:00
rendered_js: false
word_count: 379
summary: This document provides best practices and configuration guidelines for SGLang HiCache, a three-tier hierarchical KV caching system designed to improve performance for long-context and multi-turn conversation scenarios.
tags:
    - sglang
    - hicache
    - kv-cache
    - hierarchical-caching
    - performance-optimization
    - distributed-inference
    - storage-backends
category: guide
---

## Contents

## SGLang HiCache Best Practices[#](#sglang-hicache-best-practices "Link to this heading")

## Why HiCache Matters[#](#why-hicache-matters "Link to this heading")

SGLang HiCache extends the traditional RadixAttention with a three-tier hierarchical KV caching system that dramatically improves performance for long-context and multi-turn conversation scenarios. By intelligently managing KV caches across GPU memory, host memory, and external storage backends, HiCache addresses the fundamental capacity bottleneck that limits cache hit rates in conventional systems.

## Configuration Guidelines[#](#configuration-guidelines "Link to this heading")

## Core HiCache Parameters[#](#core-hicache-parameters "Link to this heading")

```
# Essential HiCache flags
--page-size64# Page size for cache management
--enable-hierarchical-cache# Enable HiCache
--hicache-ratio2# Host memory ratio (2x GPU memory)
--hicache-size100# Host memory size in GBs, will override the above ratio
--hicache-io-backendkernel# The I/O backend of moving data between CPU and GPU
--hicache-write-policywrite_through# Cache write policy from GPU to CPU
--hicache-storage-backend# Optional storage backend (e.g., hf3fs, mooncake, etc.)
```

Notes:

- Besides configuring `--hicache-storage-backend` at startup, SGLang also supports **runtime attach/detach** of the HiCache storage backend (no restart required) via HTTP admin endpoints. See [Runtime Attach/Detach HiCache Storage Backend](https://docs.sglang.io/advanced_features/hicache_storage_runtime_attach_detach.html).

## Key Configurations with Storage Backends Enabled[#](#key-configurations-with-storage-backends-enabled "Link to this heading")

### Memory Layout Optimization[#](#memory-layout-optimization "Link to this heading")

```
# Page-first: Optimized for I/O efficiency with zero-copy (recommended with kernel backend)
--hicache-mem-layoutpage_first
# Page-first-direct: Optimized for direct I/O operations (Compatible with fa3 and same zero-copy performance as page_first)
--hicache-mem-layoutpage_first_direct
# Layer-first
--hicache-mem-layoutlayer_first
```

**Layout Compatibility:**

- `page_first`: Only compatible with `kernel` I/O backend, automatically switches to `layer_first` with `direct` backend
- `page_first_direct`: Specifically designed for `direct` I/O backend with optimized memory organization

### Prefetch Policies[#](#prefetch-policies "Link to this heading")

```
# Best-effort: Terminate prefetch when needed
--hicache-storage-prefetch-policybest_effort
# Wait-complete: Ensure complete prefetch, higher cache reuse
--hicache-storage-prefetch-policywait_complete
# Timeout: Balance between completion and best-effort
--hicache-storage-prefetch-policytimeout
```

### Integration with PD Disaggregation[#](#integration-with-pd-disaggregation "Link to this heading")

HiCache works seamlessly with PD Disaggregation. You can choose between two configurations:

1. **Prefill-only HiCache**: Enable HiCache only on Prefill nodes, allowing KV cache sharing among Prefill instances
2. **Full HiCache with async offloading**: Enable HiCache on Prefill nodes and async KV cache offloading on Decode nodes, allowing Prefill nodes to reuse KV caches from Decode nodes in multi-turn dialogue scenarios

```
# Prefill node with HiCache enabled for cross-prefill sharing (ideal for SystemPrompt scenarios)
python3-msglang.launch_server\
--model-path/xxx/DeepSeek-R1/\
--tp8\
--host0.0.0.0\
--port10000\
--enable-metrics\
--enable-cache-report\
--mem-fraction-static0.85\
--page-size64\
--enable-hierarchical-cache\
--hicache-ratio2\
--hicache-size0\
--hicache-mem-layoutpage_first_direct\
--hicache-io-backenddirect\
--hicache-write-policywrite_through\
--hicache-storage-backendhf3fs\
--hicache-storage-prefetch-policywait_complete\
--disaggregation-ib-devicemlx5_0\
--disaggregation-modeprefill\
--disaggregation-transfer-backendmooncake

# Decode node with async offloading enabled for KV cache reuse by Prefill (ideal for multi-turn conversations)
python3-msglang.launch_server\
--model-path/xxx/DeepSeek-R1/\
--tp8\
--host0.0.0.0\
--port10000\
--enable-metrics\
--enable-cache-report\
--page-size64\
--hicache-ratio2\
--hicache-size0\
--hicache-mem-layoutpage_first_direct\
--hicache-io-backenddirect\
--hicache-write-policywrite_through\
--hicache-storage-backendhf3fs\
--hicache-storage-prefetch-policywait_complete\
--disaggregation-decode-enable-offload-kvcache\ # Enable async KV cache offloading in decode node
--disaggregation-ib-devicemlx5_0\
--disaggregation-modedecode\
--disaggregation-transfer-backendmooncake
```

### Deployment with HF3FS[#](#deployment-with-hf3fs "Link to this heading")

Here is an example of deploying DeepSeek-R1 with HiCache-HF3FS. For more details, see the HF3FS Documentation.

```
python3-msglang.launch_server\
--model-path/xxx/DeepSeek-R1/\
--log-levelinfo\
--tp8\
--host0.0.0.0\
--port10000\
--enable-metrics\
--enable-cache-report\
--page-size64\
--mem-fraction-static0.85\
--enable-hierarchical-cache\
--hicache-ratio2\
--hicache-size0\
--hicache-mem-layoutpage_first_direct\
--hicache-io-backenddirect\
--hicache-write-policywrite_through\
--hicache-storage-backendhf3fs\
--hicache-storage-prefetch-policywait_complete\
```

### Deployment with Mooncake[#](#deployment-with-mooncake "Link to this heading")

Here is an example of deploying Qwen3-235B-A22B-Instruct-2507 with Mooncake. For more details, see the Mooncake Documentation.

```
# Set Mooncake environment variables
exportMOONCAKE_TE_META_DATA_SERVER="http://127.0.0.1:8080/metadata"
exportMOONCAKE_GLOBAL_SEGMENT_SIZE=816043786240
exportMOONCAKE_PROTOCOL="rdma"
exportMOONCAKE_DEVICE="$DEVICE_LIST"
exportMOONCAKE_MASTER=127.0.0.1:50051

# Launch SGLang server with Mooncake backend
python3-msglang.launch_server\
--model-path$MODEL_PATH\
--tp8\
--page-size64\
--enable-hierarchical-cache\
--hicache-ratio2\
--hicache-mem-layoutpage_first_direct\
--hicache-io-backenddirect\
--hicache-storage-backendmooncake\
--hicache-write-policywrite_through\
--hicache-storage-prefetch-policytimeout
```

## Custom Storage Backend Integration[#](#custom-storage-backend-integration "Link to this heading")

To integrate a new storage backend:

1. **Implement three core methods:**
   
   - `get(key)`: Retrieve value by key
   - `exists(key)`: Check key existence
   - `set(key, value)`: Store key-value pair
2. **Register your backend:** Add your storage backend to the HiCache [BackendFactory](https://docs.sglang.io/_downloads/62f9aec5f652f3712fb96e8201110e73/backend_factory.py)

The HiCache controller handles all scheduling and synchronization automatically.

### Dynamic Backend Loading[#](#dynamic-backend-loading "Link to this heading")

Alternatively, you can use dynamic loading to avoid hard-coding your backend in the repository:

```
python3-msglang.launch_server\
--model-pathyour-model\
--enable-hierarchical-cache\
--hicache-storage-backenddynamic\
--hicache-storage-backend-extra-config'{"backend_name":"custom_backend_name", "module_path": "your_module_path", "class_name": "YourHiCacheClassName"}'
```

**Configuration Parameters:**

- `--hicache-storage-backend`: Set to `dynamic`
- `--hicache-storage-backend-extra-config`: JSON configuration with:
  
  - `backend_name`: Custom backend identifier
  - `module_path`: Python module path to your implementation
  - `class_name`: Your HiCache implementation class name
  - `interface_v1`: 0 (disable) or 1 (enable) to control usage of batch\_get\_v1 and batch\_set\_v1 methods

## Community and Support[#](#community-and-support "Link to this heading")

- **GitHub Issues**: Report bugs and feature requests
- **Slack Channel**: Join community discussions in #sgl-kv-cache-store
- **Documentation**: Refer to storage backend-specific guides

* * *

*This document will be continuously updated based on community feedback and new features. Contributions and suggestions are welcome!*