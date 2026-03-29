---
title: Runtime Attach/Detach HiCache Storage Backend (No Restart) — SGLang
url: https://docs.sglang.io/advanced_features/hicache_storage_runtime_attach_detach.html
source: crawler
fetched_at: 2026-02-04T08:47:50.032945963-03:00
rendered_js: false
word_count: 501
summary: This document explains how to dynamically attach or detach HiCache L3 storage backends in SGLang at runtime via an HTTP API without restarting the service. It details the architecture, strict idle-state requirements, and operational steps for managing storage backend configurations.
tags:
    - sglang
    - hicache
    - storage-backend
    - runtime-configuration
    - http-api
    - storage-management
    - dynamic-attachment
category: guide
---

## Contents

## Runtime Attach/Detach HiCache Storage Backend (No Restart)[#](#runtime-attach-detach-hicache-storage-backend-no-restart "Link to this heading")

This document explains how to **dynamically attach/detach the HiCache L3 storage backend at runtime** (e.g., `mooncake` / `hf3fs` / `nixl` / `file` / `aibrix` / `eic`) while **SGLang is already running and serving traffic**, without restarting the process.

For safety and consistency, the current implementation **strictly requires** these operations to happen only when the service is **idle**:

- **No running requests**
- **No waiting/queued requests**

If the idle condition is not met, the API will fail fast (HTTP 400) and **will not modify** the current service state.

* * *

## 1. Background and implementation overview[#](#background-and-implementation-overview "Link to this heading")

### 1.1 Architecture / control path[#](#architecture-control-path "Link to this heading")

The control path is:

1. **HTTP Server** (`python/sglang/srt/entrypoints/http_server.py`)
   
   - Exposes `PUT /hicache/storage-backend`, `DELETE /hicache/storage-backend`, `GET /hicache/storage-backend`
2. **TokenizerManager** (`python/sglang/srt/managers/tokenizer_communicator_mixin.py`)
   
   - Sends the request to the Scheduler via `_Communicator`
3. **Scheduler** (`python/sglang/srt/managers/scheduler.py`)
   
   - Performs a **strict idle check**
   - Calls `tree_cache.attach_storage_backend(...)` / `detach_storage_backend(...)`
4. **HiRadixCache** (`python/sglang/srt/mem_cache/hiradix_cache.py`)
   
   - Parses `hicache_storage_backend_extra_config_json` (supports both backend config and prefetch knobs)
   - Calls `cache_controller.attach_storage_backend(...)` / `detach_storage_backend(...)`
5. **HiCacheController** (`python/sglang/srt/managers/cache_controller.py`)
   
   - Creates/destroys the storage backend instance (via `StorageBackendFactory`)
   - Starts/stops backend background threads at runtime (prefetch/backup)

* * *

## 2. Idle-state requirement (strict)[#](#idle-state-requirement-strict "Link to this heading")

The Scheduler uses a stricter `_is_idle_for_hicache_storage_op()`:

- `_is_no_request()` is true (covers running/overlap/pp/disagg and other active states)
- `waiting_queue` is empty
- `grammar_queue` is empty (if the grammar backend is enabled)

If the condition is not met, attach/detach returns an error like:

- `Reject attach: scheduler is not idle. #queue-req=... #running-req=...`

> Tip: before switching, drain upstream traffic and wait for the server to become idle, then call attach/detach.

### 2.1 DP (data parallel) semantics[#](#dp-data-parallel-semantics "Link to this heading")

When `dp_size > 1`, the tokenizer dispatches the request to **all DP scheduler instances** and aggregates their responses:

- The final `success` is **true only if all DP ranks return success**
- The final `message` concatenates messages from all DP ranks

This is intended to prevent “silent partial success”, but it also means you may see:

- Overall **failure** even though **some ranks already succeeded**

Currently there is **no automatic partial rollback** across DP ranks (see TODO in code). Operationally:

- Prefer to keep backend config identical across ranks
- If attach fails, immediately call detach (best-effort/idempotent), fix config, then retry attach

* * *

## 3. How to use (HTTP Admin API)[#](#how-to-use-http-admin-api "Link to this heading")

The examples below assume your SGLang HTTP server is at `http://127.0.0.1:30000`.

### 3.1 Query current storage backend status[#](#query-current-storage-backend-status "Link to this heading")

```
curl-shttp://127.0.0.1:30000/hicache/storage-backend
```

Example response:

```
{
"hicache_storage_backend":"mooncake",
"hicache_storage_backend_extra_config":"{\"master_server_address\":\"127.0.0.1:50051\", ...}"
}
```

### 3.2 Attach (enable) a storage backend[#](#attach-enable-a-storage-backend "Link to this heading")

```
curl-s-XPUThttp://127.0.0.1:30000/hicache/storage-backend\
-H'Content-Type: application/json'\
-d'{
    "hicache_storage_backend": "mooncake"
  }'
```

```
curl-s-XPUThttp://127.0.0.1:30000/hicache/storage-backend\
-H'Content-Type: application/json'\
-d'{
    "hicache_storage_backend": "mooncake",
    "hicache_storage_backend_extra_config_json": "{\"master_server_address\":\"127.0.0.1:50051\",\"protocol\":\"tcp\",\"global_segment_size\":\"4gb\",\"prefetch_threshold\":256}",
    "hicache_storage_prefetch_policy": "timeout"
  }'
```

Notes:

- `hicache_storage_backend_extra_config_json` can include both:
  
  - **Backend configuration** (e.g., Mooncake master/metadata/protocol, etc.)
  - **Prefetch configuration** (`prefetch_threshold`, `prefetch_timeout_base`, `prefetch_timeout_per_ki_token`, `hicache_storage_pass_prefix_keys`)

### 3.3 Detach (disable) the storage backend[#](#detach-disable-the-storage-backend "Link to this heading")

```
curl-s-XDELETEhttp://127.0.0.1:30000/hicache/storage-backend
```

Notes:

- Detach only makes SGLang **stop using** the L3 storage backend and stops prefetch/backup threads
- It **does not automatically delete** data stored in Mooncake/HF3FS (or other remote backends)

* * *

## 4. Behavior and caveats[#](#behavior-and-caveats "Link to this heading")

- **No restart required**: attach/detach switches in-process at runtime
- **Must be idle**: otherwise the request is rejected to avoid consistency issues
- **Host KV layout constraints still apply**: for example, Mooncake still requires layouts like `page_first/page_first_direct/page_head`; if the server’s HiCache host-memory layout does not satisfy the backend requirements, attach will fail with an error
- **Observability**:
  
  - After attach, `server_args.hicache_storage_backend*` is updated on both the tokenizer and scheduler sides
  - If metrics are enabled, attach will create a storage metrics collector in `HiRadixCache` on demand