---
title: weight_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_utils/
source: sitemap
fetched_at: 2026-05-07T21:28:53.858495313-03:00
rendered_js: false
word_count: 1172
summary: This document provides a set of utility functions for managing model checkpoints, including hardware resource estimation, filesystem inspection, sorting, and efficient background prefetching into the page cache.
tags:
    - model-loading
    - checkpoint-management
    - utility-functions
    - io-optimization
    - file-system-operations
    - page-cache
category: reference
---

Utilities for downloading and initializing model weights.

## \_get\_available\_ram\_bytes [¶](#vllm.model_executor.model_loader.weight_utils._get_available_ram_bytes "Permanent link")

```
_get_available_ram_bytes() -> int
```

Return the available RAM in bytes.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
def_get_available_ram_bytes() -> int:
"""Return the available RAM in bytes."""
    importpsutil

    return psutil.virtual_memory().available
```

## \_get\_checkpoints\_size\_bytes [¶](#vllm.model_executor.model_loader.weight_utils._get_checkpoints_size_bytes "Permanent link")

```
_get_checkpoints_size_bytes(files: list[str]) -> int
```

Return the total size of the checkpoint files in bytes.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
def_get_checkpoints_size_bytes(files: list[str]) -> int:
"""Return the total size of the checkpoint files in bytes."""
    if not files:
        return 0
    return sum(os.path.getsize(f) for f in files)
```

## \_get\_fs\_type [¶](#vllm.model_executor.model_loader.weight_utils._get_fs_type "Permanent link")

Get the filesystem type of the first file in *files* (Linux only).

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
def_get_fs_type(files: list[str]) -> str:
"""Get the filesystem type of the first file in *files* (Linux only)."""
    if not files:
        return ""
    try:
        # Only the first file is checked — all checkpoint shards reside
        # in the same directory and therefore on the same filesystem.
        resolved = os.path.realpath(files[0])
        best_mount = ""
        best_fstype = ""
        # /proc/mounts may contain nested mount points (e.g. "/" -> ext4,
        # "/data" -> nfs4, "/data/local" -> ext4).  We pick the entry with
        # the longest matching mount_point — the same "longest prefix match"
        # rule the kernel uses to decide which filesystem serves a path.
        with open("/proc/mounts") as f:
            for line in f:
                parts = line.split()
                if len(parts) < 3:
                    continue
                mount_point, fstype = parts[1], parts[2]
                if (
                    resolved == mount_point
                    or resolved.startswith(os.path.join(mount_point, ""))
                ) and len(mount_point) > len(best_mount):
                    best_mount = mount_point
                    best_fstype = fstype
        return best_fstype
    except Exception:
        # /proc/mounts is Linux-specific; on other OSes (or if the read
        # fails for any reason) we fall back to an empty string.
        return ""
```

## \_natural\_sort\_key [¶](#vllm.model_executor.model_loader.weight_utils._natural_sort_key "Permanent link")

```
_natural_sort_key(filepath: str) -> list
```

Natural sort key for filenames with numeric components, such as model-00001-of-00005.safetensors -&gt; \['model-', 1, '-of-', 5, '.safetensors']

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
def_natural_sort_key(filepath: str) -> list:
"""Natural sort key for filenames with numeric components, such as
    model-00001-of-00005.safetensors -> ['model-', 1, '-of-', 5, '.safetensors']"""
    return [
        int(s) if s.isdigit() else s
        for s in re.split(r"(\d+)", os.path.basename(filepath))
    ]
```

## \_prefetch\_all\_checkpoints [¶](#vllm.model_executor.model_loader.weight_utils._prefetch_all_checkpoints "Permanent link")

```
_prefetch_all_checkpoints(sorted_files: list[str]) -> None
```

Start prefetching checkpoint files into page cache in a background thread.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
def_prefetch_all_checkpoints(sorted_files: list[str]) -> None:
"""Start prefetching checkpoint files into page cache in a background thread."""
    if torch.distributed.is_initialized():
        rank = torch.distributed.get_rank()
        world_size = torch.distributed.get_world_size()
    else:
        rank = 0
        world_size = 1
    num_prefetch_threads = 8
    paths_to_prefetch = sorted_files[rank::world_size]
    total_for_rank = len(paths_to_prefetch)

    async def_prefetch_all() -> None:
        semaphore = asyncio.Semaphore(num_prefetch_threads)
        completed = 0
        next_log_pct = 10

        async defprefetch_one(path: str) -> None:
            nonlocal completed, next_log_pct
            try:
                async with semaphore:
                    await asyncio.to_thread(_prefetch_checkpoint, path)
                completed += 1
                if total_for_rank > 0 and next_log_pct <= 100:
                    pct = 100 * completed / total_for_rank
                    if pct >= next_log_pct:
                        logger.info(
                            "Prefetching checkpoint files: %d%% (%d/%d)",
                            next_log_pct,
                            completed,
                            total_for_rank,
                        )
                        next_log_pct += 10
            except Exception:
                logger.warning(
                    "Failed to prefetch checkpoint file %r.", path, exc_info=True
                )

        await asyncio.gather(*(prefetch_one(p) for p in paths_to_prefetch))

    def_run_prefetch() -> None:
        start = time.perf_counter()
        asyncio.run(_prefetch_all())
        elapsed = time.perf_counter() - start
        logger.info(
            "Prefetching checkpoint files into page cache finished in %.2fs",
            elapsed,
        )

    logger.info("Prefetching checkpoint files into page cache started (in background)")
    threading.Thread(target=_run_prefetch, daemon=True).start()
```

## \_prefetch\_checkpoint [¶](#vllm.model_executor.model_loader.weight_utils._prefetch_checkpoint "Permanent link")

```
_prefetch_checkpoint(file_path: str) -> None
```

Prefetch a checkpoint file into the OS page cache.

Reads the file in 16MB blocks so the kernel caches its pages before workers load the same file.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
def_prefetch_checkpoint(file_path: str) -> None:
"""Prefetch a checkpoint file into the OS page cache.

    Reads the file in 16MB blocks so the kernel caches its pages before
    workers load the same file.
    """
    block_size = 16 * 1024 * 1024  # 16MB
    with open(file_path, "rb") as f:
        while f.read(block_size):
            pass
```

## atomic\_writer [¶](#vllm.model_executor.model_loader.weight_utils.atomic_writer "Permanent link")

Context manager that provides an atomic file writing routine.

The context manager writes to a temporary file and, if successful, atomically replaces the original file.

Parameters:

Name Type Description Default `filepath` `str or Path`

The path to the file to write.

*required* `mode` `str`

The file mode for the temporary file (e.g., 'w', 'wb').

`'w'` `encoding` `str`

The encoding for text mode.

`None`

Yields:

Type Description `Generator[IO]`

file object: A handle to the temporary file.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
@contextmanager
defatomic_writer(
    filepath: str | Path, mode: str = "w", encoding: str | None = None
) -> Generator[IO]:
"""
    Context manager that provides an atomic file writing routine.

    The context manager writes to a temporary file and, if successful,
    atomically replaces the original file.

    Args:
        filepath (str or Path): The path to the file to write.
        mode (str): The file mode for the temporary file (e.g., 'w', 'wb').
        encoding (str): The encoding for text mode.

    Yields:
        file object: A handle to the temporary file.
    """
    # Create a temporary file in the same directory as the target file
    # to ensure it's on the same filesystem for an atomic replace.
    temp_dir = os.path.dirname(filepath)
    temp_fd, temp_path = tempfile.mkstemp(dir=temp_dir)

    try:
        # Open the temporary file for writing
        with os.fdopen(temp_fd, mode=mode, encoding=encoding) as temp_file:
            yield temp_file

        # If the 'with' block completes successfully,
        # perform the atomic replace.
        os.replace(temp_path, filepath)

    except Exception:
        logger.exception(
            "Error during atomic write. Original file '%s' not modified", filepath
        )
        raise
    finally:
        # Clean up the temporary file if it still exists.
        if os.path.exists(temp_path):
            os.remove(temp_path)
```

## composed\_weight\_loader [¶](#vllm.model_executor.model_loader.weight_utils.composed_weight_loader "Permanent link")

Create a weight loader that post-processes the weights after loading

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defcomposed_weight_loader(
    loader: LoaderFunction, fn: Callable[[torch.Tensor], torch.Tensor]
) -> LoaderFunction:
"""Create a weight loader that post-processes the weights after loading"""

    defcomposed_loader(param: torch.Tensor, loaded_weight: torch.Tensor) -> None:
        loader(param, loaded_weight)
        param.data.copy_(fn(param))
        return

    return composed_loader
```

## convert\_pyslice\_to\_tensor [¶](#vllm.model_executor.model_loader.weight_utils.convert_pyslice_to_tensor "Permanent link")

convert PySafeSlice object from safetensors to torch.Tensor

PySafeSlice object supports indexing, which is done before loading the actual tensor and can reduce the amount of memory being read into the memory. However, it does not support more advanced functionalities like `.view()` or `.t()`. Therefore, if we need to modify the loaded tensor with these more complicated operators, we need to convert to tensor first.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defconvert_pyslice_to_tensor(x: Any) -> torch.Tensor:
"""convert PySafeSlice object from safetensors to torch.Tensor

    PySafeSlice object supports indexing, which is done before loading the
    actual tensor and can reduce the amount of memory being read into the
    memory. However, it does not support more advanced functionalities
    like `.view()` or `.t()`. Therefore, if we need to modify the loaded
    tensor with these more complicated operators, we need to convert to
    tensor first.
    """
    if not isinstance(x, torch.Tensor):
        x = x[:]
    return x
```

## default\_weight\_loader [¶](#vllm.model_executor.model_loader.weight_utils.default_weight_loader "Permanent link")

```
default_weight_loader(
    param: Tensor, loaded_weight: Tensor
) -> None
```

Default weight loader.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defdefault_weight_loader(param: torch.Tensor, loaded_weight: torch.Tensor) -> None:
"""Default weight loader."""
    try:
        if param.numel() == 1 and loaded_weight.numel() == 1:
            # Sometimes scalar values aren't considered tensors with shapes
            # so if both param and loaded_weight are a scalar,
            # reshape to match before copying
            param.data.copy_(loaded_weight.view(param.shape))
        else:
            assert param.size() == loaded_weight.size(), (
                f"Attempted to load weight ({loaded_weight.size()}) "
                f"into parameter ({param.size()})"
            )

            param.data.copy_(loaded_weight)
    except Exception:
        # NOTE: This exception is added for the purpose of setting breakpoint to
        # debug weight loading issues.
        raise
```

## download\_safetensors\_index\_file\_from\_hf [¶](#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf "Permanent link")

```
download_safetensors_index_file_from_hf(
    model_name_or_path: str,
    index_file: str,
    cache_dir: str | None,
    subfolder: str | None = None,
    revision: str | None = None,
) -> None
```

Download hf safetensors index file from Hugging Face Hub.

Parameters:

Name Type Description Default `model_name_or_path` `str`

The model name or path.

*required* `index_file` `str`

The safetensors index file name

*required* `cache_dir` `Optional[str]`

The cache directory to store the model weights. If None, will use HF defaults.

*required* `subfolder` `Optional[str]`

The subfolder within the model repository to download weights from.

`None` `revision` `Optional[str]`

The revision of the model.

`None`

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defdownload_safetensors_index_file_from_hf(
    model_name_or_path: str,
    index_file: str,
    cache_dir: str | None,
    subfolder: str | None = None,
    revision: str | None = None,
) -> None:
"""Download hf safetensors index file from Hugging Face Hub.

    Args:
        model_name_or_path (str): The model name or path.
        index_file (str): The safetensors index file name
        cache_dir (Optional[str]): The cache directory to store the model
            weights. If None, will use HF defaults.
        subfolder (Optional[str]): The subfolder within the model repository
            to download weights from.
        revision (Optional[str]): The revision of the model.
    """
    # Use file lock to prevent multiple processes from
    # downloading the same model weights at the same time.
    with get_lock(model_name_or_path, cache_dir):
        try:
            # Download the safetensors index file.
            hf_hub_download(
                repo_id=model_name_or_path,
                filename=index_file,
                cache_dir=cache_dir,
                revision=revision,
                subfolder=subfolder,
                local_files_only=huggingface_hub.constants.HF_HUB_OFFLINE,
            )
        # If file not found on remote or locally, we should not fail since
        # only some models will have index_file.
        except huggingface_hub.utils.LocalEntryNotFoundError:
            logger.info("No %s found in local cache.", index_file)
        except huggingface_hub.utils.EntryNotFoundError:
            logger.info("No %s found in remote.", index_file)
```

## download\_weights\_from\_hf [¶](#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf "Permanent link")

```
download_weights_from_hf(
    model_name_or_path: str,
    cache_dir: str | None,
    allow_patterns: list[str],
    revision: str | None = None,
    subfolder: str | None = None,
    ignore_patterns: str | list[str] | None = None,
) -> str
```

Download model weights from Hugging Face Hub.

Parameters:

Name Type Description Default `model_name_or_path` `str`

The model name or path.

*required* `cache_dir` `Optional[str]`

The cache directory to store the model weights. If None, will use HF defaults.

*required* `allow_patterns` `list[str]`

The allowed patterns for the weight files. Files matched by any of the patterns will be downloaded.

*required* `revision` `Optional[str]`

The revision of the model.

`None` `subfolder` `Optional[str]`

The subfolder within the model repository to download weights from.

`None` `ignore_patterns` `Optional[Union[str, list[str]]]`

The patterns to filter out the weight files. Files matched by any of the patterns will be ignored.

`None`

Returns:

Name Type Description `str` `str`

The path to the downloaded model weights.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
@instrument(span_name="Download weights - HF")
defdownload_weights_from_hf(
    model_name_or_path: str,
    cache_dir: str | None,
    allow_patterns: list[str],
    revision: str | None = None,
    subfolder: str | None = None,
    ignore_patterns: str | list[str] | None = None,
) -> str:
"""Download model weights from Hugging Face Hub.

    Args:
        model_name_or_path (str): The model name or path.
        cache_dir (Optional[str]): The cache directory to store the model
            weights. If None, will use HF defaults.
        allow_patterns (list[str]): The allowed patterns for the
            weight files. Files matched by any of the patterns will be
            downloaded.
        revision (Optional[str]): The revision of the model.
        subfolder (Optional[str]): The subfolder within the model repository
            to download weights from.
        ignore_patterns (Optional[Union[str, list[str]]]): The patterns to
            filter out the weight files. Files matched by any of the patterns
            will be ignored.

    Returns:
        str: The path to the downloaded model weights.
    """
    assert len(allow_patterns) > 0
    local_only = huggingface_hub.constants.HF_HUB_OFFLINE
    if not local_only:
        # Attempt to reduce allow_patterns to a single pattern
        # so we only have to call snapshot_download once.
        try:
            fs = HfFileSystem()
            file_list = fs.ls(
                os.path.join(model_name_or_path, subfolder or ""),
                detail=False,
                revision=revision,
            )

            # If downloading safetensors and an index file exists, use the
            # specific file names from the index to avoid downloading
            # unnecessary files (e.g., from subdirectories like "original/").
            index_file = f"{model_name_or_path}/{SAFE_WEIGHTS_INDEX_NAME}"
            if "*.safetensors" in allow_patterns and index_file in file_list:
                index_path = hf_hub_download(
                    repo_id=model_name_or_path,
                    filename=SAFE_WEIGHTS_INDEX_NAME,
                    cache_dir=cache_dir,
                    revision=revision,
                    subfolder=subfolder,
                )
                with open(index_path) as f:
                    weight_map = json.load(f)["weight_map"]
                if weight_map:
                    # Extra [] so that weight_map files are treated as a
                    # single allow_pattern in the loop below
                    allow_patterns = [list(set(weight_map.values()))]  # type: ignore[list-item]
                else:
                    allow_patterns = ["*.safetensors"]
            else:
                # Use the first pattern found in the HF repo's files.
                for pattern in allow_patterns:
                    if fnmatch.filter(file_list, pattern):
                        allow_patterns = [pattern]
                        break
        except Exception as e:
            logger.warning(
                "Failed to get file list for '%s'. Trying each pattern in "
                "allow_patterns individually until weights have been "
                "downloaded. Error: %s",
                model_name_or_path,
                e,
            )

    logger.debug("Using model weights format %s", allow_patterns)
    # Use file lock to prevent multiple processes from
    # downloading the same model weights at the same time.
    with get_lock(model_name_or_path, cache_dir):
        start_time = time.perf_counter()
        for allow_pattern in allow_patterns:
            hf_folder = snapshot_download(
                model_name_or_path,
                allow_patterns=allow_pattern,
                ignore_patterns=ignore_patterns,
                cache_dir=cache_dir,
                tqdm_class=DisabledTqdm,
                revision=revision,
                local_files_only=local_only,
            )
            # If we have downloaded weights for this allow_pattern,
            # we don't need to check the rest.
            # allow_pattern can be a list (from weight_map) or str (glob)
            if isinstance(allow_pattern, list):
                break
            if any(Path(hf_folder).glob(allow_pattern)):
                break
        time_taken = time.perf_counter() - start_time
        if time_taken > 0.5:
            logger.info(
                "Time spent downloading weights for %s: %.6f seconds",
                model_name_or_path,
                time_taken,
            )
    return hf_folder
```

## enable\_hf\_transfer [¶](#vllm.model_executor.model_loader.weight_utils.enable_hf_transfer "Permanent link")

automatically activates hf\_transfer

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defenable_hf_transfer():
"""automatically activates hf_transfer"""
    if "HF_HUB_ENABLE_HF_TRANSFER" not in os.environ:
        try:
            # enable hf hub transfer if available
            importhf_transfer  # type: ignore # noqa

            huggingface_hub.constants.HF_HUB_ENABLE_HF_TRANSFER = True
        except ImportError:
            pass
```

## enable\_xet\_high\_performance [¶](#vllm.model_executor.model_loader.weight_utils.enable_xet_high_performance "Permanent link")

```
enable_xet_high_performance()
```

automatically activates xet high performance mode

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defenable_xet_high_performance():
"""automatically activates xet high performance mode"""
    if "HF_XET_HIGH_PERFORMANCE" not in os.environ:
        huggingface_hub.constants.HF_XET_HIGH_PERFORMANCE = True
```

## fastsafetensors\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.fastsafetensors_weights_iterator "Permanent link")

Iterate over the weights in the model safetensor files using fastsafetensor library.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
deffastsafetensors_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Iterate over the weights in the model safetensor files
    using fastsafetensor library."""
    if torch.distributed.is_initialized():
        pg = torch.distributed.group.WORLD
    else:
        pg = SingleGroup()

    device = torch.device(f"cuda:{current_platform.current_device()}")
    hf_weights_files = sorted(hf_weights_files, key=_natural_sort_key)
    weight_files_sub_lists = [
        hf_weights_files[i : i + pg.size()]
        for i in range(0, len(hf_weights_files), pg.size())
    ]

    # Use nogds=True for TP > 1 to avoid cuFileDriverOpen() which
    # initializes the GDS DMA subsystem for all visible GPUs, creating
    # unwanted CUDA contexts on every device.
    nogds = pg.size() > 1

    for f_list in tqdm(
        weight_files_sub_lists,
        desc="Loading safetensors using Fastsafetensor loader",
        disable=not enable_tqdm(use_tqdm_on_load),
        bar_format=_BAR_FORMAT,
    ):
        loader = _init_fastsafetensors_loader(pg, device, f_list, nogds=nogds)
        try:
            try:
                fb = loader.copy_files_to_device()
            except RuntimeError as e:
                if "gds" not in str(e):
                    raise

                loader.close()
                nogds = True
                logger.warning_once(
                    "GDS not enabled, setting `nogds=True`.\n"
                    "For more information, see: https://github.com/foundation-model-stack/fastsafetensors?tab=readme-ov-file#basic-api-usages"
                )
                loader = _init_fastsafetensors_loader(pg, device, f_list, nogds=nogds)
                fb = loader.copy_files_to_device()

            try:
                keys = list(fb.key_to_rank_lidx.keys())
                for k in keys:
                    t = fb.get_tensor(k)
                    yield k, t
            finally:
                fb.close()
        finally:
            loader.close()
```

## filter\_files\_not\_needed\_for\_inference [¶](#vllm.model_executor.model_loader.weight_utils.filter_files_not_needed_for_inference "Permanent link")

```
filter_files_not_needed_for_inference(
    hf_weights_files: list[str],
) -> list[str]
```

Exclude files that are not needed for inference.

See https://github.com/huggingface/transformers/blob/v4.34.0/src/transformers/trainer.py#L227-L233

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
deffilter_files_not_needed_for_inference(hf_weights_files: list[str]) -> list[str]:
"""
    Exclude files that are not needed for inference.

    See https://github.com/huggingface/transformers/blob/v4.34.0/src/transformers/trainer.py#L227-L233
    """
    blacklist = [
        "training_args.bin",
        "optimizer.bin",
        "optimizer.pt",
        "scheduler.pt",
        "scaler.pt",
    ]
    hf_weights_files = [
        f for f in hf_weights_files if not any(f.endswith(x) for x in blacklist)
    ]
    return hf_weights_files
```

## get\_gguf\_weight\_type\_map [¶](#vllm.model_executor.model_loader.weight_utils.get_gguf_weight_type_map "Permanent link")

Return GGUF mapped weight's name and its quant type

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defget_gguf_weight_type_map(
    gguf_file: str | Path, gguf_to_hf_name_map: dict[str, str]
) -> dict[str, str]:
"""
    Return GGUF mapped weight's name and its quant type
    """
    reader = gguf.GGUFReader(gguf_file)
    return {
        gguf_to_hf_name_map[tensor.name]: tensor.tensor_type.name
        for tensor in reader.tensors
        if tensor.name in gguf_to_hf_name_map
    }
```

## gguf\_quant\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.gguf_quant_weights_iterator "Permanent link")

Iterate over the quant weights in the model gguf files and convert them to torch tensors. Be careful of the order of yielding weight types and weights data, we have to yield all weight types first before yielding any weights. Otherwise it would cause issue when loading weights with for packed layer with different quant types.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defgguf_quant_weights_iterator(
    gguf_file: str | Path, gguf_to_hf_name_map: dict[str, str]
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""
    Iterate over the quant weights in the model gguf files and convert
    them to torch tensors.
    Be careful of the order of yielding weight types and weights data,
    we have to yield all weight types first before yielding any weights.
    Otherwise it would cause issue when loading weights with for packed
    layer with different quant types.
    """

    reader = gguf.GGUFReader(gguf_file)

    for tensor in reader.tensors:
        if tensor.name in gguf_to_hf_name_map:
            weight_type = tensor.tensor_type
            name = gguf_to_hf_name_map[tensor.name]

            if weight_type.name not in ("F32", "BF16", "F16"):
                weight_type_name = name.replace("weight", "qweight_type")
                weight_type = torch.tensor(weight_type)
                yield weight_type_name, weight_type

    for tensor in reader.tensors:
        if tensor.name in gguf_to_hf_name_map:
            weight = tensor.data
            weight_type = tensor.tensor_type
            name = gguf_to_hf_name_map[tensor.name]
            if weight_type.name not in ("F32", "BF16", "F16"):
                name = name.replace("weight", "qweight")
            if weight_type.name == "BF16" and tensor.data.dtype == np.uint8:
                # BF16 is currently the only "quantization" type that isn't
                # actually quantized but is read as a raw byte tensor.
                # Reinterpret as `torch.bfloat16` tensor.
                weight = weight.view(np.uint16)
                if reader.byte_order == "S":
                    # GGUF endianness != system endianness
                    weight = weight.byteswap()
                param = torch.tensor(weight).view(torch.bfloat16)
            else:
                param = torch.tensor(weight)
            yield name, param
```

## gguf\_quant\_weights\_iterator\_multi [¶](#vllm.model_executor.model_loader.weight_utils.gguf_quant_weights_iterator_multi "Permanent link")

Iterate over the quant weights across multiple GGUF shard files and convert them to torch tensors.

Like gguf\_quant\_weights\_iterator, we yield all weight types first before yielding any weights data to avoid issues with packed layers that have different quant types.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defgguf_quant_weights_iterator_multi(
    gguf_files: list[str], gguf_to_hf_name_map: dict[str, str]
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""
    Iterate over the quant weights across multiple GGUF shard files
    and convert them to torch tensors.

    Like gguf_quant_weights_iterator, we yield all weight types first
    before yielding any weights data to avoid issues with packed layers
    that have different quant types.
    """
    readers = [gguf.GGUFReader(f) for f in gguf_files]

    # First pass: yield all weight types across all shards
    for reader in readers:
        for tensor in reader.tensors:
            if tensor.name in gguf_to_hf_name_map:
                weight_type = tensor.tensor_type
                name = gguf_to_hf_name_map[tensor.name]
                if weight_type.name not in ("F32", "BF16", "F16"):
                    weight_type_name = name.replace("weight", "qweight_type")
                    weight_type = torch.tensor(weight_type)
                    yield weight_type_name, weight_type

    # Second pass: yield all weight data across all shards
    for reader in readers:
        for tensor in reader.tensors:
            if tensor.name in gguf_to_hf_name_map:
                weight = tensor.data
                weight_type = tensor.tensor_type
                name = gguf_to_hf_name_map[tensor.name]
                if weight_type.name not in ("F32", "BF16", "F16"):
                    name = name.replace("weight", "qweight")
                if weight_type.name == "BF16" and tensor.data.dtype == np.uint8:
                    weight = weight.view(np.uint16)
                    if reader.byte_order == "S":
                        weight = weight.byteswap()
                    param = torch.tensor(weight).view(torch.bfloat16)
                else:
                    param = torch.tensor(weight)
                yield name, param
```

## initialize\_dummy\_weights [¶](#vllm.model_executor.model_loader.weight_utils.initialize_dummy_weights "Permanent link")

Initialize model weights with random values.

The model weights must be randomly initialized for accurate performance measurements. Additionally, the model weights should not cause NaNs in the forward pass. We empirically found that initializing the weights with values between -1e-3 and 1e-3 works well for most models.

We use per-parameter random seed, so that dummy weights are consistent, even if the model is partitioned across multiple devices. When the seed is fixed, the random values generated by this function only depends on the parameter's number of elements and its data type.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
definitialize_dummy_weights(
    model: torch.nn.Module,
    model_config: ModelConfig,
    low: float = -1e-3,
    high: float = 1e-3,
    seed: int = 1234,
) -> None:
"""Initialize model weights with random values.

    The model weights must be randomly initialized for accurate performance
    measurements. Additionally, the model weights should not cause NaNs in the
    forward pass. We empirically found that initializing the weights with
    values between -1e-3 and 1e-3 works well for most models.

    We use per-parameter random seed, so that dummy weights are consistent,
    even if the model is partitioned across multiple devices. When the seed
    is fixed, the random values generated by this function only depends on
    the parameter's number of elements and its data type.
    """
    for param in model.state_dict().values():
        initialize_single_dummy_weight(param, low, high, seed)
```

## instanttensor\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.instanttensor_weights_iterator "Permanent link")

Iterate over the weights in the model safetensor files using instanttensor library.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
definstanttensor_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Iterate over the weights in the model safetensor files
    using instanttensor library."""
    try:
        importinstanttensor
    except ImportError as e:
        raise ImportError(
            "Please install instanttensor via `pip install instanttensor`"
        ) frome

    if not current_platform.is_cuda():
        raise ValueError("InstantTensor requires NVIDIA GPUs")

    try:
        world_group = get_world_group()
    except AssertionError:
        # Entering here only in unit tests where the world group is not initialized.
        process_group = None
    else:
        process_group = world_group.device_group if world_group.world_size > 1 else None

    device = current_platform.current_device()

    with instanttensor.safe_open(
        hf_weights_files, framework="pt", device=device, process_group=process_group
    ) as f:
        yield from tqdm(
            f.tensors(),
            desc="Loading safetensors using InstantTensor loader",
            disable=not enable_tqdm(use_tqdm_on_load),
            bar_format=_BAR_FORMAT,
            position=tqdm._get_free_pos(),
            total=len(f.keys()),
            mininterval=1.0,
        )
```

## maybe\_download\_from\_modelscope [¶](#vllm.model_executor.model_loader.weight_utils.maybe_download_from_modelscope "Permanent link")

```
maybe_download_from_modelscope(
    model: str,
    revision: str | None = None,
    download_dir: str | None = None,
    ignore_patterns: str | list[str] | None = None,
    allow_patterns: list[str] | str | None = None,
) -> str | None
```

Download model from ModelScope hub if VLLM\_USE\_MODELSCOPE is True.

Returns the path to the downloaded model, or None if the model is not downloaded from ModelScope.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defmaybe_download_from_modelscope(
    model: str,
    revision: str | None = None,
    download_dir: str | None = None,
    ignore_patterns: str | list[str] | None = None,
    allow_patterns: list[str] | str | None = None,
) -> str | None:
"""Download model from ModelScope hub if VLLM_USE_MODELSCOPE is True.

    Returns the path to the downloaded model, or None if the model is not
    downloaded from ModelScope."""
    if envs.VLLM_USE_MODELSCOPE:
        # download model from ModelScope hub,
        # lazy import so that modelscope is not required for normal use.
        # pylint: disable=C.
        frommodelscope.hub.snapshot_downloadimport snapshot_download

        # Use file lock to prevent multiple processes from
        # downloading the same model weights at the same time.
        with get_lock(model, download_dir):
            if not os.path.exists(model):
                model_path = snapshot_download(
                    model_id=model,
                    cache_dir=download_dir,
                    local_files_only=huggingface_hub.constants.HF_HUB_OFFLINE,
                    revision=revision,
                    ignore_file_pattern=ignore_patterns,
                    allow_patterns=allow_patterns,
                )
            else:
                model_path = model
        return model_path
    return None
```

## maybe\_remap\_kv\_scale\_name [¶](#vllm.model_executor.model_loader.weight_utils.maybe_remap_kv_scale_name "Permanent link")

```
maybe_remap_kv_scale_name(
    name: str, params_dict: dict
) -> str | None
```

Remap the name of FP8 k/v\_scale parameters.

This function handles the remapping of FP8 k/v\_scale parameter names. It detects if the given name ends with a suffix and attempts to remap it to the expected name format in the model. If the remapped name is not found in the params\_dict, a warning is printed and None is returned.

Parameters:

Name Type Description Default `name` `str`

The original loaded checkpoint parameter name.

*required* `params_dict` `dict`

Dictionary containing the model's named parameters.

*required*

Returns:

Name Type Description `str` `str | None`

The remapped parameter name if successful, or the original name if no remapping is needed.

`None` `str | None`

If the remapped name is not found in params\_dict.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defmaybe_remap_kv_scale_name(name: str, params_dict: dict) -> str | None:
"""Remap the name of FP8 k/v_scale parameters.

    This function handles the remapping of FP8 k/v_scale parameter names.
    It detects if the given name ends with a suffix and attempts to remap
    it to the expected name format in the model. If the remapped name is not
    found in the params_dict, a warning is printed and None is returned.

    Args:
        name (str): The original loaded checkpoint parameter name.
        params_dict (dict): Dictionary containing the model's named parameters.

    Returns:
        str: The remapped parameter name if successful, or the original name
             if no remapping is needed.
        None: If the remapped name is not found in params_dict.
    """
    if name.endswith(".kv_scale"):
        logger.warning_once(
            "DEPRECATED. Found kv_scale in the checkpoint. "
            "This format is deprecated in favor of separate k_scale and "
            "v_scale tensors and will be removed in a future release. "
            "Functionally, we will remap kv_scale to k_scale and duplicate "
            "k_scale to v_scale"
        )
        # NOTE: we remap the deprecated kv_scale to k_scale
        remapped_name = name.replace(".kv_scale", ".attn.k_scale")
        if remapped_name not in params_dict:
            logger.warning_once(
                "Found kv_scale in the checkpoint (e.g. %s), but not found the expected name in the model (e.g. %s). kv_scale is not loaded.",  #  noqa: E501
                name,
                remapped_name,
            )
            return None
        return remapped_name

    if any("mla_attn" in key for key in params_dict):
        attn_str = "mla_attn.mla_attn"
        logger.debug_once(
            f"Found mla_attn with k_scale and v_scale in "
            f"the checkpoint, using {attn_str} as attn_str"
        )
    else:
        attn_str = "attn"
    # Define scale name mapping patterns in order of precedence
    scale_mapping_patterns = [
        # ModelOpt format: .self_attn.{k,v}_proj.{k,v}_scale ->
        # .self_attn.attn.{k,v}_scale
        (
            r"\.self_attn\.([kv])_proj\.([kv])_scale$",
            rf".self_attn.{attn_str}.\2_scale",
        ),
        # QKV proj format: .self_attn.qkv_proj.{k,v}_scale ->
        # .self_attn.attn.{k,v}_scale
        (r"\.self_attn\.qkv_proj\.([kv])_scale$", r".self_attn.attn.\1_scale"),
        # Qwen3 MoE format: .self_attn.qkqkv_proj.{k,v}_scale ->
        # .self_attn.attn.{k,v}_scale
        (r"\.self_attn\.qkqkv_proj\.([kv])_scale$", r".self_attn.attn.\1_scale"),
        # NemotronH format: .mixer.{k,v}_proj.{k,v}_scale ->
        # .mixer.attn.{k,v}_scale
        (r"\.mixer\.[kv]_proj\.([kv])_scale$", r".mixer.attn.\1_scale"),
        # HYV3 format: .self_attn.q.scale -> .self_attn.attn.q_scale
        (r"\.self_attn\.q\.scale$", r".self_attn.attn.q_scale"),
        # HYV3 format: .self_attn.{k,v}_cache.scale ->
        # .self_attn.attn.{k,v}_scale
        (r"\.self_attn\.([kv])_cache\.scale$", r".self_attn.attn.\1_scale"),
        # Default format: .{k,v}_scale -> .attn.{k,v}_scale
        (r"\.([qkv])_scale$", r".attn.\1_scale"),
        (r"\.([qkv])_zero_point$", r".attn.\1_zero_point"),
    ]

    # Check if name ends with k_scale or v_scale
    if name.endswith(
        (
            ".k_scale",
            ".v_scale",
            ".q_scale",
            ".k_zero_point",
            ".v_zero_point",
            ".q_zero_point",
            ".q.scale",
            ".k_cache.scale",
            ".v_cache.scale",
        )
    ):
        importregexasre

        for pattern, replacement in scale_mapping_patterns:
            if re.search(pattern, name):
                remapped_name = re.sub(pattern, replacement, name)
                if remapped_name not in params_dict:
                    scale_type = name.split(".")[-1]
                    logger.warning_once(
                        "Found %s in the checkpoint (e.g. %s), but not found the expected name in the model (e.g. %s). %s is not loaded.",  # noqa: E501
                        scale_type,
                        name,
                        remapped_name,
                        scale_type,
                    )
                    return None
                return remapped_name

    # If there were no matches, return the untouched param name
    return name
```

## multi\_thread\_pt\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.multi_thread_pt_weights_iterator "Permanent link")

Multi-Thread iterate over the weights in the model bin/pt files.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defmulti_thread_pt_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    pt_load_map_location: str | dict[str, str] = "cpu",
    max_workers: int = 4,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Multi-Thread iterate over the weights in the model bin/pt files."""

    def_load_file(bin_file: str):
        return torch.load(
            bin_file, map_location=pt_load_map_location, weights_only=True
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(_load_file, bin_file) for bin_file in hf_weights_files
        ]
        futures_iter = tqdm(
            concurrent.futures.as_completed(futures),
            total=len(hf_weights_files),
            desc="Multi-thread loading pt checkpoint shards",
            disable=not enable_tqdm(use_tqdm_on_load),
            bar_format=_BAR_FORMAT,
        )

        for future in futures_iter:
            state = future.result()
            yield from state.items()
            del state
```

## multi\_thread\_safetensors\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.multi_thread_safetensors_weights_iterator "Permanent link")

Multi-Thread iterate over the weights in the model safetensor files.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defmulti_thread_safetensors_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    max_workers: int = 4,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Multi-Thread iterate over the weights in the model safetensor files."""

    def_load_file(st_file: str):
        result = load_file(st_file, device="cpu")
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Note to use generator here so we do not store all the loaded files in memory
        # at the same time, which can cause OOM for large models.
        futures = (executor.submit(_load_file, st_file) for st_file in hf_weights_files)
        futures_iter = tqdm(
            concurrent.futures.as_completed(futures),
            total=len(hf_weights_files),
            desc="Multi-thread loading shards",
            disable=not enable_tqdm(use_tqdm_on_load),
            bar_format=_BAR_FORMAT,
        )

        for future in futures_iter:
            state_dict = future.result()
            del future
            for key in list(state_dict):
                yield key, state_dict.pop(key)
```

## np\_cache\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.np_cache_weights_iterator "Permanent link")

Iterate over the weights in the model np files.

Will dump the model weights to numpy files if they are not already dumped.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defnp_cache_weights_iterator(
    model_name_or_path: str,
    cache_dir: str | None,
    hf_folder: str,
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Iterate over the weights in the model np files.

    Will dump the model weights to numpy files if they are not already dumped.
    """
    # Convert the model weights from torch tensors to numpy arrays for
    # faster loading.
    np_folder = os.path.join(hf_folder, "np")
    os.makedirs(np_folder, exist_ok=True)
    weight_names_file = os.path.join(np_folder, "weight_names.json")
    # Use file lock to prevent multiple processes from
    # dumping the same model weights to numpy at the same time.
    with get_lock(model_name_or_path, cache_dir):
        if not os.path.exists(weight_names_file):
            weight_names: list[str] = []
            for bin_file in tqdm(
                hf_weights_files,
                desc="Loading np_cache checkpoint shards",
                disable=not enable_tqdm(use_tqdm_on_load),
                bar_format=_BAR_FORMAT,
            ):
                state = torch.load(bin_file, map_location="cpu", weights_only=True)
                for name, param in state.items():
                    param_path = os.path.join(np_folder, name)
                    with open(param_path, "wb") as f:
                        np.save(f, param.cpu().detach().numpy())
                    weight_names.append(name)
            with open(weight_names_file, "w") as f:
                json.dump(weight_names, f)

    with open(weight_names_file) as f:
        weight_names = json.load(f)

    for name in weight_names:
        param_path = os.path.join(np_folder, name)
        with open(param_path, "rb") as f:
            param = np.load(f)
        yield name, torch.from_numpy(param)
```

## pt\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.pt_weights_iterator "Permanent link")

Iterate over the weights in the model bin/pt files.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defpt_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    pt_load_map_location: str | dict[str, str] = "cpu",
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Iterate over the weights in the model bin/pt files."""
    for bin_file in tqdm(
        hf_weights_files,
        desc="Loading pt checkpoint shards",
        disable=not enable_tqdm(use_tqdm_on_load),
        bar_format=_BAR_FORMAT,
    ):
        state = torch.load(
            bin_file, map_location=pt_load_map_location, weights_only=True
        )
        yield from state.items()
        del state
```

## row\_parallel\_weight\_loader [¶](#vllm.model_executor.model_loader.weight_utils.row_parallel_weight_loader "Permanent link")

```
row_parallel_weight_loader(
    param: Tensor, loaded_weight: Tensor
) -> None
```

Load weights that are row-parallelized.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defrow_parallel_weight_loader(
    param: torch.Tensor, loaded_weight: torch.Tensor
) -> None:
"""Load weights that are row-parallelized."""
    tp_rank = get_tensor_model_parallel_rank()
    shard_dim = 0 if param.dim() != 1 else None

    if shard_dim is not None:
        shard_size = param.data.shape[shard_dim]
        start_idx = tp_rank * shard_size
        loaded_weight = loaded_weight.narrow(shard_dim, start_idx, shard_size)

    return default_weight_loader(param, loaded_weight)
```

## runai\_safetensors\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.runai_safetensors_weights_iterator "Permanent link")

Iterate over the weights in the model safetensor files.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defrunai_safetensors_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    is_distributed: bool = False,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Iterate over the weights in the model safetensor files."""
    with SafetensorsStreamer() as streamer:
        is_cuda_alike = current_platform.is_cuda_alike()
        device = (
            f"cuda:{current_platform.current_device()}"
            if is_distributed and is_cuda_alike
            else "cpu"
        )

        streamer.stream_files(
            hf_weights_files,
            device=device,
            is_distributed=is_distributed,
        )
        total_tensors = sum(
            len(tensors_meta)
            for tensors_meta in streamer.files_to_tensors_metadata.values()
        )

        tensor_iter = tqdm(
            streamer.get_tensors(),
            total=total_tensors,
            desc="Loading safetensors using Runai Model Streamer",
            bar_format=_BAR_FORMAT,
            disable=not enable_tqdm(use_tqdm_on_load),
            mininterval=2,
        )

        yield from tensor_iter
```

## safetensors\_weights\_iterator [¶](#vllm.model_executor.model_loader.weight_utils.safetensors_weights_iterator "Permanent link")

```
safetensors_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    safetensors_load_strategy: str | None = None,
    local_expert_ids: set[int] | None = None,
) -> Generator[tuple[str, Tensor], None, None]
```

Iterate over the weights in the model safetensor files.

When *local\_expert\_ids* is provided, expert weights not belonging to this rank are skipped **before** reading from disk, which drastically reduces storage I/O for MoE models under EP.

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defsafetensors_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    safetensors_load_strategy: str | None = None,
    local_expert_ids: set[int] | None = None,
) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Iterate over the weights in the model safetensor files.

    When *local_expert_ids* is provided, expert weights not belonging to
    this rank are skipped **before** reading from disk, which drastically
    reduces storage I/O for MoE models under EP.
    """
    loading_desc = "Loading safetensors checkpoint shards"
    if safetensors_load_strategy == "eager":
        loading_desc += " (eager)"

    sorted_files = sorted(hf_weights_files, key=_natural_sort_key)

    fs_type = _get_fs_type(sorted_files)
    is_net_fs = fs_type in ("nfs", "nfs4", "lustre")
    total_bytes = _get_checkpoints_size_bytes(sorted_files)
    avail_bytes = _get_available_ram_bytes()
    ram_threshold_pct = 90
    fits_in_ram = total_bytes <= (ram_threshold_pct / 100.0) * avail_bytes
    fs_name = fs_type.upper() if fs_type else "unknown"

    logger.info_once(
        "Filesystem type for checkpoints: %s. Checkpoint size: %.2f GiB. "
        "Available RAM: %.2f GiB.",
        fs_name,
        total_bytes / 1024**3,
        avail_bytes / 1024**3,
    )

    should_prefetch = safetensors_load_strategy == "prefetch"
    if safetensors_load_strategy is None:
        if is_net_fs and fits_in_ram:
            should_prefetch = True
        elif is_net_fs and not fits_in_ram:
            logger.warning_once(
                "Network filesystem (%s) detected but checkpoint total size "
                "(%.2f GiB) exceeds %d%% of available RAM (%.2f GiB). "
                "Skipping auto-prefetch.",
                fs_name,
                total_bytes / 1024**3,
                ram_threshold_pct,
                avail_bytes / 1024**3,
            )
        elif not is_net_fs and fits_in_ram:
            logger.info_once(
                "Auto-prefetch is disabled because the filesystem (%s) is not a "
                "recognized network FS (NFS/Lustre). If you want to force "
                "prefetching, start vLLM with --safetensors-load-strategy=prefetch.",
                fs_name,
            )
        elif not is_net_fs and not fits_in_ram:
            logger.info_once(
                "Auto-prefetch is disabled because the filesystem (%s) is not a "
                "recognized network FS (NFS/Lustre) and the checkpoint size "
                "(%.2f GiB) exceeds %d%% of available RAM (%.2f GiB).",
                fs_name,
                total_bytes / 1024**3,
                ram_threshold_pct,
                avail_bytes / 1024**3,
            )
    elif should_prefetch and not fits_in_ram:
        logger.warning_once(
            "safetensors_load_strategy='prefetch' was explicitly specified, but "
            "checkpoint total size (%.2f GiB) exceeds %d%% of available RAM "
            "(%.2f GiB). This may cause out-of-memory errors.",
            total_bytes / 1024**3,
            ram_threshold_pct,
            avail_bytes / 1024**3,
        )

    if should_prefetch:
        _prefetch_all_checkpoints(sorted_files)

    leftover_state_dict: dict[str, torch.Tensor] = {}
    for st_file in tqdm(
        sorted_files,
        desc=loading_desc,
        disable=not enable_tqdm(use_tqdm_on_load),
        bar_format=_BAR_FORMAT,
    ):
        if safetensors_load_strategy == "eager":
            with open(st_file, "rb") as f:
                state_dict = load(f.read())
            for name, param in state_dict.items():
                if not should_skip_weight(name, local_expert_ids):
                    yield name, param
        elif safetensors_load_strategy == "torchao":
            # we can't load flattened torchao tensor subclasses directly into the model
            # instead we reconstruct the subclasses here before returning
            if not torchao_version_at_least("0.15.0"):
                raise ValueError(
                    "Please use torchao version >= 0.15.0 "
                    "to load torchao safetensors checkpoint"
                )
            fromtorchao.prototype.safetensors.safetensors_supportimport (
                unflatten_tensor_state_dict,
            )

            with safe_open(st_file, framework="pt") as f:
                state_dict = {}
                for name in f.keys():  # noqa: SIM118
                    if should_skip_weight(name, local_expert_ids):
                        continue
                    state_dict[name] = f.get_tensor(name)

                # update with leftover tensor data from previous iteration, if any
                state_dict.update(leftover_state_dict)
                metadata = f.metadata()
                # due to sharded checkpoints, we are not guaranteed that we have all
                # tensor subclass data on one file
                # state_dict has the leftover data from this step and we wait for
                # missing information to be provided in a future iteration
                unflattened_state_dict, leftover_state_dict = (
                    unflatten_tensor_state_dict(state_dict, metadata)
                )
            yield from unflattened_state_dict.items()
        else:
            with safe_open(st_file, framework="pt") as f:
                for name in f.keys():  # noqa: SIM118
                    if should_skip_weight(name, local_expert_ids):
                        continue
                    param = f.get_tensor(name)
                    yield name, param
```

## sharded\_weight\_loader [¶](#vllm.model_executor.model_loader.weight_utils.sharded_weight_loader "Permanent link")

```
sharded_weight_loader(shard_axis: int) -> LoaderFunction
```

Create a weight loader that shards the weights along the given axis

Source code in `vllm/model_executor/model_loader/weight_utils.py`

```
defsharded_weight_loader(shard_axis: int) -> LoaderFunction:
"""Create a weight loader that shards the weights along the given axis"""

    defloader(param: torch.Tensor, loaded_weight: torch.Tensor) -> None:
        tp_rank = get_tensor_model_parallel_rank()

        shard_size = param.data.shape[shard_axis]
        start_idx = tp_rank * shard_size
        loaded_weight = loaded_weight.narrow(shard_axis, start_idx, shard_size)

        return default_weight_loader(param, loaded_weight)

    return loader
```