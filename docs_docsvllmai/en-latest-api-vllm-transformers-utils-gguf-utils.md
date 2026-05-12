---
title: gguf_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/gguf_utils/
source: sitemap
fetched_at: 2026-05-07T21:37:44.39509619-03:00
rendered_js: false
word_count: 558
summary: This document provides utility functions for identifying GGUF model files, locating multimodal projector files, extracting vision configuration parameters from metadata, and retrieving GGUF files from the HuggingFace Hub.
tags:
    - gguf
    - model-loading
    - multimodal
    - huggingface
    - vision-config
    - file-utilities
    - vllm
category: api
---

GGUF utility functions.

## check\_gguf\_file `cached` [¶](#vllm.transformers_utils.gguf_utils.check_gguf_file "Permanent link")

Check if the file is a GGUF model.

Source code in `vllm/transformers_utils/gguf_utils.py`

```
@cache
defcheck_gguf_file(model: str | PathLike) -> bool:
"""Check if the file is a GGUF model."""
    model = Path(model)
    if not model.is_file():
        return False
    elif model.suffix == ".gguf":
        return True

    try:
        with model.open("rb") as f:
            header = f.read(4)

        return header == b"GGUF"
    except Exception as e:
        logger.debug("Error reading file %s: %s", model, e)
        return False
```

## detect\_gguf\_multimodal [¶](#vllm.transformers_utils.gguf_utils.detect_gguf_multimodal "Permanent link")

```
detect_gguf_multimodal(model: str) -> Path | None
```

Check if GGUF model has multimodal projector file.

Parameters:

Name Type Description Default `model` `str`

Model path string

*required*

Returns:

Type Description `Path | None`

Path to mmproj file if found, None otherwise

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defdetect_gguf_multimodal(model: str) -> Path | None:
"""Check if GGUF model has multimodal projector file.

    Args:
        model: Model path string

    Returns:
        Path to mmproj file if found, None otherwise
    """
    if not model.endswith(".gguf"):
        return None

    try:
        model_path = Path(model)
        if not model_path.is_file():
            return None

        model_dir = model_path.parent
        mmproj_patterns = ["mmproj.gguf", "mmproj-*.gguf", "*mmproj*.gguf"]
        for pattern in mmproj_patterns:
            mmproj_files = list(model_dir.glob(pattern))
            if mmproj_files:
                return mmproj_files[0]
        return None
    except Exception:
        return None

extract_vision_config_from_gguf(
    mmproj_path: str,
) -> SiglipVisionConfig | None
```

Extract vision config parameters from mmproj.gguf metadata.

Reads vision encoder configuration from GGUF metadata fields using standardized GGUF constants. Automatically detects the projector type (e.g., gemma3, llama4) and applies model-specific parameters accordingly.

The function extracts standard CLIP vision parameters from GGUF metadata and applies projector-type-specific customizations. For unknown projector types, it uses safe defaults from SiglipVisionConfig.

Parameters:

Name Type Description Default `mmproj_path` `str`

Path to mmproj.gguf file (str or Path)

*required*

Returns:

Type Description `SiglipVisionConfig | None`

SiglipVisionConfig if extraction succeeds, None if any required

`SiglipVisionConfig | None`

field is missing from the GGUF metadata

Raises:

Type Description `Exception`

Exceptions from GGUF reading (file not found, corrupted file, etc.) propagate directly from gguf.GGUFReader

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defextract_vision_config_from_gguf(mmproj_path: str) -> "SiglipVisionConfig | None":
"""Extract vision config parameters from mmproj.gguf metadata.

    Reads vision encoder configuration from GGUF metadata fields using
    standardized GGUF constants. Automatically detects the projector type
    (e.g., gemma3, llama4) and applies model-specific parameters accordingly.

    The function extracts standard CLIP vision parameters from GGUF metadata
    and applies projector-type-specific customizations. For unknown projector
    types, it uses safe defaults from SiglipVisionConfig.

    Args:
        mmproj_path: Path to mmproj.gguf file (str or Path)

    Returns:
        SiglipVisionConfig if extraction succeeds, None if any required
        field is missing from the GGUF metadata

    Raises:
        Exception: Exceptions from GGUF reading (file not found, corrupted
            file, etc.) propagate directly from gguf.GGUFReader
    """
    reader = gguf.GGUFReader(str(mmproj_path))

    # Detect projector type to apply model-specific parameters
    projector_type = None
    projector_type_field = reader.get_field(Keys.Clip.PROJECTOR_TYPE)
    if projector_type_field:
        try:
            projector_type = bytes(projector_type_field.parts[-1]).decode("utf-8")
        except (AttributeError, UnicodeDecodeError) as e:
            logger.warning("Failed to decode projector type from GGUF: %s", e)

    # Map GGUF field constants to SiglipVisionConfig parameters.
    # Uses official GGUF constants from gguf-py for standardization.
    # Format: {gguf_constant: (param_name, dtype)}
    VISION_CONFIG_FIELDS = {
        Keys.ClipVision.EMBEDDING_LENGTH: ("hidden_size", int),
        Keys.ClipVision.FEED_FORWARD_LENGTH: ("intermediate_size", int),
        Keys.ClipVision.BLOCK_COUNT: ("num_hidden_layers", int),
        Keys.ClipVision.Attention.HEAD_COUNT: ("num_attention_heads", int),
        Keys.ClipVision.IMAGE_SIZE: ("image_size", int),
        Keys.ClipVision.PATCH_SIZE: ("patch_size", int),
        Keys.ClipVision.Attention.LAYERNORM_EPS: ("layer_norm_eps", float),
    }

    # Extract and validate all required fields
    config_params = {}
    for gguf_key, (param_name, dtype) in VISION_CONFIG_FIELDS.items():
        field = reader.get_field(gguf_key)
        if field is None:
            logger.warning(
                "Missing required vision config field '%s' in mmproj.gguf",
                gguf_key,
            )
            return None
        # Extract scalar value from GGUF field and convert to target type
        config_params[param_name] = dtype(field.parts[-1])

    # Apply model-specific parameters based on projector type
    if projector_type == VisionProjectorType.GEMMA3:
        # Gemma3 doesn't use the vision pooling head (multihead attention)
        # This is a vLLM-specific parameter used in SiglipVisionTransformer
        config_params["vision_use_head"] = False
        logger.info("Detected Gemma3 projector, disabling vision pooling head")
    # Add other projector-type-specific customizations here as needed
    # elif projector_type == VisionProjectorType.LLAMA4:
    #     config_params["vision_use_head"] = ...

    # Create config with extracted parameters
    # Note: num_channels and attention_dropout use SiglipVisionConfig defaults
    # (3 and 0.0 respectively) which are correct for all models
    config = SiglipVisionConfig(**config_params)

    if projector_type:
        logger.info(
            "Extracted vision config from mmproj.gguf (projector_type: %s)",
            projector_type,
        )
    else:
        logger.info("Extracted vision config from mmproj.gguf metadata")

    return config
```

## get\_gguf\_file\_path\_from\_hf [¶](#vllm.transformers_utils.gguf_utils.get_gguf_file_path_from_hf "Permanent link")

```
get_gguf_file_path_from_hf(
    repo_id: str | Path,
    quant_type: str,
    revision: str | None = None,
) -> str
```

Get the GGUF file path from HuggingFace Hub based on repo\_id and quant\_type.

Parameters:

Name Type Description Default `repo_id` `str | Path`

The HuggingFace repository ID (e.g., "Qwen/Qwen3-0.6B")

*required* `quant_type` `str`

The quantization type (e.g., "Q4\_K\_M", "F16")

*required* `revision` `str | None`

Optional revision/branch name

`None`

Returns:

Type Description `str`

The path to the GGUF file on HuggingFace Hub (e.g., "filename.gguf"),

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defget_gguf_file_path_from_hf(
    repo_id: str | Path,
    quant_type: str,
    revision: str | None = None,
) -> str:
"""Get the GGUF file path from HuggingFace Hub based on repo_id and quant_type.

    Args:
        repo_id: The HuggingFace repository ID (e.g., "Qwen/Qwen3-0.6B")
        quant_type: The quantization type (e.g., "Q4_K_M", "F16")
        revision: Optional revision/branch name

    Returns:
        The path to the GGUF file on HuggingFace Hub (e.g., "filename.gguf"),
    """
    repo_id = str(repo_id)
    gguf_patterns = [
        f"*-{quant_type}.gguf",
        f"*-{quant_type}-*.gguf",
        f"*/*-{quant_type}.gguf",
        f"*/*-{quant_type}-*.gguf",
    ]
    matching_files = list_filtered_repo_files(
        repo_id,
        allow_patterns=gguf_patterns,
        revision=revision,
    )

    if len(matching_files) == 0:
        raise ValueError(
            "Could not find GGUF file for repo %s with quantization %s.",
            repo_id,
            quant_type,
        )

    # Sort to ensure consistent ordering (prefer non-sharded files)
    matching_files.sort(key=lambda x: (x.count("-"), x))
    gguf_filename = matching_files[0]
    return gguf_filename
```

## is\_gguf [¶](#vllm.transformers_utils.gguf_utils.is_gguf "Permanent link")

Check if the model is a GGUF model.

Parameters:

Name Type Description Default `model` `str | Path`

Model name, path, or Path object to check.

*required*

Returns:

Type Description `bool`

True if the model is a GGUF model, False otherwise.

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defis_gguf(model: str | Path) -> bool:
"""Check if the model is a GGUF model.

    Args:
        model: Model name, path, or Path object to check.

    Returns:
        True if the model is a GGUF model, False otherwise.
    """
    model = str(model)

    # Check if it's a local GGUF file
    if check_gguf_file(model):
        return True

    # Check if it's a remote GGUF model (repo_id:quant_type format)
    return is_remote_gguf(model)
```

## is\_nonstandard\_gguf\_quant\_type [¶](#vllm.transformers_utils.gguf_utils.is_nonstandard_gguf_quant_type "Permanent link")

```
is_nonstandard_gguf_quant_type(quant_type: str) -> bool
```

Check if a non-standard quant type contains a known GGML type.

Splits the quant type by the last `-` and checks whether the trailing part is a standard GGML type. For example::

```
UD-Q4_K_XL      → rsplit → ["UD", "Q4_K_XL"]      → Q4_K_XL valid ✓
UD-IQ4_NL       → rsplit → ["UD", "IQ4_NL"]       → IQ4_NL  valid ✓
Custom-UD-Q4_K  → rsplit → ["Custom-UD", "Q4_K"]  → Q4_K    valid ✓
RANDOM          → no "-" → False
```

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defis_nonstandard_gguf_quant_type(quant_type: str) -> bool:
"""Check if a non-standard quant type contains a known GGML type.

    Splits the quant type by the last ``-`` and checks whether the
    trailing part is a standard GGML type.  For example::

        UD-Q4_K_XL      → rsplit → ["UD", "Q4_K_XL"]      → Q4_K_XL valid ✓
        UD-IQ4_NL       → rsplit → ["UD", "IQ4_NL"]       → IQ4_NL  valid ✓
        Custom-UD-Q4_K  → rsplit → ["Custom-UD", "Q4_K"]  → Q4_K    valid ✓
        RANDOM          → no "-" → False
    """
    if "-" not in quant_type:
        return False
    _, remainder = quant_type.rsplit("-", 1)
    return is_valid_gguf_quant_type(remainder)
```

## is\_remote\_gguf `cached` [¶](#vllm.transformers_utils.gguf_utils.is_remote_gguf "Permanent link")

Check if the model is a remote GGUF model.

Recognizes two forms: 1. Standard: `repo_id:quant_type` where *quant\_type* is a known GGML quantization type (e.g. `Q4_K_M`). 2. Non-standard: `repo_id:quant_type` where *quant\_type* contains a known GGML type with extra prefixes (e.g. `UD-Q4_K_XL`). A warning is logged and actual file existence is validated later during download.

Source code in `vllm/transformers_utils/gguf_utils.py`

```
@cache
defis_remote_gguf(model: str | Path) -> bool:
"""Check if the model is a remote GGUF model.

    Recognizes two forms:
    1. Standard: ``repo_id:quant_type`` where *quant_type* is a known
       GGML quantization type (e.g. ``Q4_K_M``).
    2. Non-standard: ``repo_id:quant_type`` where *quant_type* contains
       a known GGML type with extra prefixes (e.g. ``UD-Q4_K_XL``).
       A warning is logged and actual file existence is validated later
       during download.
    """
    pattern = r"^[a-zA-Z0-9][a-zA-Z0-9._-]*/[a-zA-Z0-9][a-zA-Z0-9._-]*:[A-Za-z0-9_+-]+$"
    model = str(model)
    if re.fullmatch(pattern, model):
        _, quant_type = model.rsplit(":", 1)
        if is_valid_gguf_quant_type(quant_type):
            return True
        if is_nonstandard_gguf_quant_type(quant_type):
            logger.warning(
                "Non-standard GGUF quant type '%s' detected.",
                quant_type,
            )
            return True
    return False
```

## is\_valid\_gguf\_quant\_type [¶](#vllm.transformers_utils.gguf_utils.is_valid_gguf_quant_type "Permanent link")

```
is_valid_gguf_quant_type(gguf_quant_type: str) -> bool
```

Check if the quant type is a valid GGUF quant type.

Supports both exact GGML quant types (e.g., Q4\_K, IQ1\_S) and extended naming conventions (e.g., Q4\_K\_M, Q3\_K\_S, Q5\_K\_L).

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defis_valid_gguf_quant_type(gguf_quant_type: str) -> bool:
"""Check if the quant type is a valid GGUF quant type.

    Supports both exact GGML quant types (e.g., Q4_K, IQ1_S) and
    extended naming conventions (e.g., Q4_K_M, Q3_K_S, Q5_K_L).
    """
    # Check for exact match first
    if getattr(GGMLQuantizationType, gguf_quant_type, None) is not None:
        return True

    # Check for extended naming conventions (e.g., Q4_K_M -> Q4_K)
    for suffix in _GGUF_QUANT_SUFFIXES:
        if gguf_quant_type.endswith(suffix):
            base_type = gguf_quant_type[: -len(suffix)]
            if getattr(GGMLQuantizationType, base_type, None) is not None:
                return True

    return False
```

## maybe\_patch\_hf\_config\_from\_gguf [¶](#vllm.transformers_utils.gguf_utils.maybe_patch_hf_config_from_gguf "Permanent link")

```
maybe_patch_hf_config_from_gguf(
    model: str, hf_config: PretrainedConfig
) -> PretrainedConfig
```

Patch HF config for GGUF models.

Applies GGUF-specific patches to HuggingFace config: 1. For multimodal models: patches architecture and vision config 2. For all GGUF models: overrides vocab\_size from embedding tensor

This ensures compatibility with GGUF models that have extended vocabularies (e.g., Unsloth) where the GGUF file contains more tokens than the HuggingFace tokenizer config specifies.

Parameters:

Name Type Description Default `model` `str`

Model path string

*required* `hf_config` `PretrainedConfig`

HuggingFace config to patch in-place

*required*

Returns:

Type Description `PretrainedConfig`

Updated HuggingFace config

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defmaybe_patch_hf_config_from_gguf(
    model: str,
    hf_config: PretrainedConfig,
) -> PretrainedConfig:
"""Patch HF config for GGUF models.

    Applies GGUF-specific patches to HuggingFace config:
    1. For multimodal models: patches architecture and vision config
    2. For all GGUF models: overrides vocab_size from embedding tensor

    This ensures compatibility with GGUF models that have extended
    vocabularies (e.g., Unsloth) where the GGUF file contains more
    tokens than the HuggingFace tokenizer config specifies.

    Args:
        model: Model path string
        hf_config: HuggingFace config to patch in-place

    Returns:
        Updated HuggingFace config
    """
    # Patch multimodal config if mmproj.gguf exists
    mmproj_path = detect_gguf_multimodal(model)
    if mmproj_path is not None:
        vision_config = extract_vision_config_from_gguf(str(mmproj_path))

        # Create HF config for Gemma3 multimodal
        text_config = hf_config.get_text_config()
        is_gemma3 = hf_config.model_type in ("gemma3", "gemma3_text")
        if vision_config is not None and is_gemma3:
            new_hf_config = Gemma3Config(
                text_config=text_config,
                vision_config=vision_config,
                architectures=["Gemma3ForConditionalGeneration"],
            )
            hf_config = new_hf_config

    return hf_config
```

## split\_remote\_gguf [¶](#vllm.transformers_utils.gguf_utils.split_remote_gguf "Permanent link")

Split the model into repo\_id and quant type.

Source code in `vllm/transformers_utils/gguf_utils.py`

```
defsplit_remote_gguf(model: str | Path) -> tuple[str, str]:
"""Split the model into repo_id and quant type."""
    model = str(model)
    if is_remote_gguf(model):
        parts = model.rsplit(":", 1)
        return (parts[0], parts[1])
    raise ValueError(
        f"Wrong GGUF model or invalid GGUF quant type: {model}.\n"
        "- It should be in repo_id:quant_type format.\n"
        f"- Valid base quant types: {GGMLQuantizationType._member_names_}\n"
        f"- Extended suffixes also supported: {_GGUF_QUANT_SUFFIXES}\n"
        "- Non-standard GGUF quant types also supported: "
        "dash-separated prefixes (e.g. UD-Q4_K_XL, Custom-Q8_0)",
    )
```