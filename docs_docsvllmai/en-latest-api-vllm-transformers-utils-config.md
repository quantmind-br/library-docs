---
title: config - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/config/
source: sitemap
fetched_at: 2026-05-07T21:36:41.705771664-03:00
rendered_js: false
word_count: 772
summary: This module provides utility functions for parsing, remapping, and retrieving configuration and metadata for Hugging Face transformer models and sentence-transformers, specifically designed for integration with vLLM.
tags:
    - huggingface
    - transformers
    - configuration-management
    - vllm
    - model-loading
    - metadata-parsing
category: api
---

## \_maybe\_remap\_hf\_config\_attrs [¶](#vllm.transformers_utils.config._maybe_remap_hf_config_attrs "Permanent link")

```
_maybe_remap_hf_config_attrs(
    config: PretrainedConfig,
) -> PretrainedConfig
```

Remap config attributes to match the expected names.

Source code in `vllm/transformers_utils/config.py`

```
def_maybe_remap_hf_config_attrs(config: PretrainedConfig) -> PretrainedConfig:
"""Remap config attributes to match the expected names."""
    for old_attr, new_attr in _CONFIG_ATTRS_MAPPING.items():
        if hasattr(config, old_attr):
            if not hasattr(config, new_attr):
                config.update({new_attr: getattr(config, old_attr)})
            logger.debug("Remapped config attribute '%s' to '%s'", old_attr, new_attr)
    return config
```

## \_maybe\_update\_auto\_config\_kwargs [¶](#vllm.transformers_utils.config._maybe_update_auto_config_kwargs "Permanent link")

```
_maybe_update_auto_config_kwargs(
    kwargs: dict[str, Any], model_type: str
)
```

Update kwargs for AutoConfig initialization based on model\_type

Source code in `vllm/transformers_utils/config.py`

```
def_maybe_update_auto_config_kwargs(kwargs: dict[str, Any], model_type: str):
"""
    Update kwargs for AutoConfig initialization based on model_type
    """
    if model_type in _AUTO_CONFIG_KWARGS_OVERRIDES:
        kwargs.update(_AUTO_CONFIG_KWARGS_OVERRIDES[model_type])
    return kwargs
```

## get\_config\_parser [¶](#vllm.transformers_utils.config.get_config_parser "Permanent link")

```
get_config_parser(config_format: str) -> ConfigParserBase
```

Get the config parser for a given config format.

Source code in `vllm/transformers_utils/config.py`

```
defget_config_parser(config_format: str) -> ConfigParserBase:
"""Get the config parser for a given config format."""
    if config_format not in _CONFIG_FORMAT_TO_CONFIG_PARSER:
        raise ValueError(f"Unknown config format `{config_format}`.")
    return _CONFIG_FORMAT_TO_CONFIG_PARSER[config_format]()
```

## get\_hf\_text\_config [¶](#vllm.transformers_utils.config.get_hf_text_config "Permanent link")

```
get_hf_text_config(config: PretrainedConfig)
```

Get the "sub" config relevant to llm for multi modal models. No op for pure text models.

Source code in `vllm/transformers_utils/config.py`

```
defget_hf_text_config(config: PretrainedConfig):
"""Get the "sub" config relevant to llm for multi modal models.
    No op for pure text models.
    """
    text_config = config.get_text_config()

    if text_config is not config and not hasattr(text_config, "num_attention_heads"):
        raise ValueError(
            "The text_config extracted from the model config does not have "
            "`num_attention_heads` attribute. This indicates a mismatch "
            "between the model config and vLLM's expectations. Please "
            "ensure that the model config is compatible with vLLM."
        )

    return text_config
```

## get\_pooling\_config `cached` [¶](#vllm.transformers_utils.config.get_pooling_config "Permanent link")

```
get_pooling_config(
    model: str, revision: str | None = "main"
) -> dict[str, Any] | None
```

This function gets the pooling and normalize config from the model - only applies to sentence-transformers models.

Parameters:

Name Type Description Default `model` `str`

The name of the Hugging Face model.

*required* `revision` `str | None`

The specific version of the model to use. Defaults to 'main'.

`'main'`

Returns:

Type Description `dict[str, Any] | None`

A dictionary containing the pooling type and whether normalization is used, or None if no pooling configuration is found.

Source code in `vllm/transformers_utils/config.py`

```
@cache
defget_pooling_config(
    model: str,
    revision: str | None = "main",
) -> dict[str, Any] | None:
"""
    This function gets the pooling and normalize
    config from the model - only applies to
    sentence-transformers models.

    Args:
        model: The name of the Hugging Face model.
        revision: The specific version of the model to use.
            Defaults to 'main'.

    Returns:
        A dictionary containing the pooling type and whether
            normalization is used, or None if no pooling configuration is found.
    """
    if is_remote_gguf(model):
        model, _ = split_remote_gguf(model)

    modules_file_name = "modules.json"

    modules_dict = None
    if file_or_path_exists(
        model=model, config_name=modules_file_name, revision=revision
    ):
        modules_dict = get_hf_file_to_dict(modules_file_name, model, revision)

    if modules_dict is None:
        return None

    logger.info("Found sentence-transformers modules configuration.")

    pooling = next(
        (
            item
            for item in modules_dict
            if item["type"] == "sentence_transformers.models.Pooling"
        ),
        None,
    )
    normalize = bool(
        next(
            (
                item
                for item in modules_dict
                if item["type"] == "sentence_transformers.models.Normalize"
            ),
            False,
        )
    )

    if pooling:
        fromvllm.config.poolerimport SEQ_POOLING_TYPES, TOK_POOLING_TYPES

        pooling_file_name = "{}/config.json".format(pooling["path"])
        pooling_dict = get_hf_file_to_dict(pooling_file_name, model, revision) or {}

        logger.info("Found pooling configuration.")

        config: dict[str, Any] = {"use_activation": normalize}
        for key, val in pooling_dict.items():
            if val is True:
                pooling_type = parse_pooling_type(key)
                if pooling_type in SEQ_POOLING_TYPES:
                    config["seq_pooling_type"] = pooling_type
                elif pooling_type in TOK_POOLING_TYPES:
                    config["tok_pooling_type"] = pooling_type
                else:
                    logger.debug("Skipping unrelated field: %r=%r", key, val)

        return config

    return None

get_safetensors_params_metadata(
    model: str, *, revision: str | None = None
) -> dict[str, Any]
```

Get the safetensors parameters metadata for remote/local model repository.

Source code in `vllm/transformers_utils/config.py`

```
defget_safetensors_params_metadata(
    model: str,
    *,
    revision: str | None = None,
) -> dict[str, Any]:
"""
    Get the safetensors parameters metadata for remote/local model repository.
    """
    full_metadata = {}
    if (model_path := Path(model)).exists():
        safetensors_to_check = model_path.glob("*.safetensors")
        full_metadata = {
            param_name: info
            for file_path in safetensors_to_check
            if file_path.is_file()
            for param_name, info in parse_safetensors_file_metadata(file_path).items()
        }
    else:
        repo_mt = try_get_safetensors_metadata(model, revision=revision)
        if repo_mt and (files_mt := repo_mt.files_metadata):
            full_metadata = {
                param_name: asdict(info)
                for file_mt in files_mt.values()
                for param_name, info in file_mt.tensors.items()
            }
    return full_metadata
```

## get\_sentence\_transformer\_tokenizer\_config `cached` [¶](#vllm.transformers_utils.config.get_sentence_transformer_tokenizer_config "Permanent link")

```
get_sentence_transformer_tokenizer_config(
    model: str | Path, revision: str | None = "main"
) -> dict[str, Any] | None
```

Returns the tokenization configuration dictionary for a given Sentence Transformer BERT model.

Parameters: - model (str|Path): The name of the Sentence Transformer BERT model. - revision (str, optional): The revision of the m odel to use. Defaults to 'main'.

Returns: - dict: A dictionary containing the configuration parameters for the Sentence Transformer BERT model.

Source code in `vllm/transformers_utils/config.py`

```
@cache
defget_sentence_transformer_tokenizer_config(
    model: str | Path, revision: str | None = "main"
) -> dict[str, Any] | None:
"""
    Returns the tokenization configuration dictionary for a
    given Sentence Transformer BERT model.

    Parameters:
    - model (str|Path): The name of the Sentence Transformer
    BERT model.
    - revision (str, optional): The revision of the m
    odel to use. Defaults to 'main'.

    Returns:
    - dict: A dictionary containing the configuration parameters
    for the Sentence Transformer BERT model.
    """
    sentence_transformer_config_files = [
        "sentence_bert_config.json",
        "sentence_roberta_config.json",
        "sentence_distilbert_config.json",
        "sentence_camembert_config.json",
        "sentence_albert_config.json",
        "sentence_xlm-roberta_config.json",
        "sentence_xlnet_config.json",
    ]
    encoder_dict = None

    for config_file in sentence_transformer_config_files:
        if (
            try_get_local_file(model=model, file_name=config_file, revision=revision)
            is not None
        ):
            encoder_dict = get_hf_file_to_dict(config_file, model, revision)
            if encoder_dict:
                break

    if not encoder_dict and not Path(model).is_absolute():
        try:
            # If model is on HuggingfaceHub, get the repo files
            repo_files = list_repo_files(model, revision=revision)
        except Exception:
            repo_files = []

        for config_name in sentence_transformer_config_files:
            if config_name in repo_files:
                encoder_dict = get_hf_file_to_dict(config_name, model, revision)
                if encoder_dict:
                    break

    if not encoder_dict:
        return None

    logger.info("Found sentence-transformers tokenize configuration.")

    if all(k in encoder_dict for k in ("max_seq_length", "do_lower_case")):
        return encoder_dict
    return None
```

## is\_encoder\_decoder [¶](#vllm.transformers_utils.config.is_encoder_decoder "Permanent link")

```
is_encoder_decoder(config: PretrainedConfig) -> bool
```

Detect if the model with this config is used as an encoder/decoder.

Source code in `vllm/transformers_utils/config.py`

```
defis_encoder_decoder(config: PretrainedConfig) -> bool:
"""Detect if the model with this config is used as an encoder/decoder."""

    def_is_encoder_decoder(config: PretrainedConfig) -> bool:
        return getattr(config, "is_encoder_decoder", False)

    return _is_encoder_decoder(config) or _is_encoder_decoder(config.get_text_config())
```

## is\_interleaved [¶](#vllm.transformers_utils.config.is_interleaved "Permanent link")

```
is_interleaved(config: PretrainedConfig) -> bool
```

Detect if the model with this config is used with interleaved attention.

Source code in `vllm/transformers_utils/config.py`

```
defis_interleaved(config: PretrainedConfig) -> bool:
"""
    Detect if the model with this config is used with interleaved attention.
    """
    text_config = config.get_text_config()
    if layer_types := getattr(text_config, "layer_types", None):
        return len(set(layer_types)) > 1
    return False
```

## is\_rope\_parameters\_nested [¶](#vllm.transformers_utils.config.is_rope_parameters_nested "Permanent link")

Check if rope\_parameters is nested by layer types.

Source code in `vllm/transformers_utils/config.py`

```
defis_rope_parameters_nested(rope_parameters: dict[str, Any]) -> bool:
"""Check if rope_parameters is nested by layer types."""
    # Cannot be nested if rope_parameters is empty
    if not rope_parameters:
        return False
    return set(rope_parameters.keys()).issubset(ALLOWED_ATTENTION_LAYER_TYPES)
```

## maybe\_override\_with\_speculators [¶](#vllm.transformers_utils.config.maybe_override_with_speculators "Permanent link")

```
maybe_override_with_speculators(
    model: str,
    tokenizer: str | None,
    trust_remote_code: bool,
    revision: str | None = None,
    vllm_speculative_config: dict[str, Any] | None = None,
    hf_token: bool | str | None = None,
    **kwargs,
) -> tuple[str, str | None, dict[str, Any] | None]
```

Resolve model configuration when speculators are detected.

Checks if the provided model is a speculators model and if so, extracts the target model configuration and builds the speculative config.

Parameters:

Name Type Description Default `model` `str`

Model name or path

*required* `tokenizer` `str | None`

Tokenizer name or path

*required* `trust_remote_code` `bool`

Whether to trust remote code

*required* `revision` `str | None`

Model revision

`None` `vllm_speculative_config` `dict[str, Any] | None`

Existing vLLM speculative config

`None` `hf_token` `bool | str | None`

HuggingFace token for authenticated model access

`None`

Returns:

Type Description `tuple[str, str | None, dict[str, Any] | None]`

Tuple of (resolved\_model, resolved\_tokenizer, speculative\_config)

Source code in `vllm/transformers_utils/config.py`

```
defmaybe_override_with_speculators(
    model: str,
    tokenizer: str | None,
    trust_remote_code: bool,
    revision: str | None = None,
    vllm_speculative_config: dict[str, Any] | None = None,
    hf_token: bool | str | None = None,
    **kwargs,
) -> tuple[str, str | None, dict[str, Any] | None]:
"""
    Resolve model configuration when speculators are detected.

    Checks if the provided model is a speculators model and if so, extracts
    the target model configuration and builds the speculative config.

    Args:
        model: Model name or path
        tokenizer: Tokenizer name or path
        trust_remote_code: Whether to trust remote code
        revision: Model revision
        vllm_speculative_config: Existing vLLM speculative config
        hf_token: HuggingFace token for authenticated model access

    Returns:
        Tuple of (resolved_model, resolved_tokenizer, speculative_config)
    """
    if check_gguf_file(model):
        kwargs["gguf_file"] = Path(model).name
        gguf_model_repo = Path(model).parent
    elif is_remote_gguf(model):
        repo_id, _ = split_remote_gguf(model)
        gguf_model_repo = Path(repo_id)
    else:
        gguf_model_repo = None
    kwargs["local_files_only"] = huggingface_hub.constants.HF_HUB_OFFLINE
    config_dict, _ = PretrainedConfig.get_config_dict(
        model if gguf_model_repo is None else gguf_model_repo,
        revision=revision,
        token=hf_token,
        **without_trust_remote_code(kwargs),
    )
    speculators_config = config_dict.get("speculators_config")

    if speculators_config is None:
        # No speculators config found, return original values
        return model, tokenizer, vllm_speculative_config

    # Speculators format detected - process overrides
    fromvllm.transformers_utils.configs.speculators.baseimport SpeculatorsConfig

    speculative_config = SpeculatorsConfig.extract_vllm_speculative_config(
        config_dict=config_dict
    )

    # Set the draft model to the speculators model
    speculative_config["model"] = model

    # Override model and tokenizer with the verifier model from config
    verifier_model = speculators_config["verifier"]["name_or_path"]
    model = tokenizer = verifier_model

    return model, tokenizer, speculative_config
```

## maybe\_register\_config\_serialize\_by\_value [¶](#vllm.transformers_utils.config.maybe_register_config_serialize_by_value "Permanent link")

```
maybe_register_config_serialize_by_value() -> None
```

Try to register HF model configuration class to serialize by value

If trust\_remote\_code is set, and the model's config file specifies an `AutoConfig` class, then the config class is typically an instance of a custom class imported from the HF modules cache.

Examples:

> > > from transformers import AutoConfig klass = AutoConfig.from\_pretrained( ... "meta-llama/Meta-Llama-3-8B", trust\_remote\_code=True ... ) klass.**class** # transformers.models.llama.configuration\_llama.LlamaConfig import transformers\_modules # error, not initialized klass = AutoConfig.from\_pretrained( ... "deepseek-ai/DeepSeek-V2.5", trust\_remote\_code=True ... ) import transformers\_modules # success, initialized klass.**class** # transformers\_modules.deepseek-ai.DeepSeek-V2.5.98b11844770b2c3ffc18b175c758a803640f4e77.configuration\_deepseek.DeepseekV2Config

In the DeepSeek example, the config class is an instance of a custom class that is not serializable by default. This class will not be importable in spawned workers, and won't exist at all on other nodes, which breaks serialization of the config.

In this function we tell the cloudpickle serialization library to pass instances of these generated classes by value instead of by reference, i.e. the class definition is serialized along with its data so that the class module does not need to be importable on the receiving end.

See: https://github.com/cloudpipe/cloudpickle?tab=readme-ov-file#overriding-pickles-serialization-mechanism-for-importable-constructs

Source code in `vllm/transformers_utils/config.py`

```
defmaybe_register_config_serialize_by_value() -> None:
"""Try to register HF model configuration class to serialize by value

    If trust_remote_code is set, and the model's config file specifies an
    `AutoConfig` class, then the config class is typically an instance of
    a custom class imported from the HF modules cache.

    Examples:

    >>> from transformers import AutoConfig
    >>> klass = AutoConfig.from_pretrained(
    ...     "meta-llama/Meta-Llama-3-8B", trust_remote_code=True
    ... )
    >>> klass.__class__  # transformers.models.llama.configuration_llama.LlamaConfig
    >>> import transformers_modules  # error, not initialized
    >>> klass = AutoConfig.from_pretrained(
    ...     "deepseek-ai/DeepSeek-V2.5", trust_remote_code=True
    ... )
    >>> import transformers_modules  # success, initialized
    >>> klass.__class__  # transformers_modules.deepseek-ai.DeepSeek-V2.5.98b11844770b2c3ffc18b175c758a803640f4e77.configuration_deepseek.DeepseekV2Config

    In the DeepSeek example, the config class is an instance of a custom
    class that is not serializable by default. This class will not be
    importable in spawned workers, and won't exist at all on
    other nodes, which breaks serialization of the config.

    In this function we tell the cloudpickle serialization library to pass
    instances of these generated classes by value instead of by reference,
    i.e. the class definition is serialized along with its data so that the
    class module does not need to be importable on the receiving end.

    See: https://github.com/cloudpipe/cloudpickle?tab=readme-ov-file#overriding-pickles-serialization-mechanism-for-importable-constructs
    """  # noqa
    try:
        importtransformers_modules

        transformers_modules_available = True
    except ImportError:
        transformers_modules_available = False

    try:
        importmultiprocessing
        importpickle

        importcloudpickle

        fromvllm.configimport VllmConfig

        # Register multiprocessing reducers to handle cross-process
        # serialization of VllmConfig objects that may contain custom configs
        # from transformers_modules
        def_reduce_config(config: VllmConfig):
            return (pickle.loads, (cloudpickle.dumps(config),))

        multiprocessing.reducer.register(VllmConfig, _reduce_config)

        # Register transformers_modules with cloudpickle if available
        if transformers_modules_available:
            cloudpickle.register_pickle_by_value(transformers_modules)

            # ray vendors its own version of cloudpickle
            fromvllm.v1.executor.ray_utilsimport ray

            if ray:
                ray.cloudpickle.register_pickle_by_value(transformers_modules)

    except Exception as e:
        logger.warning(
            "Unable to register remote classes used by"
            " trust_remote_code with by-value serialization. This may"
            " lead to a later error. If remote code is not needed"
            " remove `--trust-remote-code`",
            exc_info=e,
        )
```

## patch\_legacy\_rope\_type [¶](#vllm.transformers_utils.config.patch_legacy_rope_type "Permanent link")

```
patch_legacy_rope_type(
    rope_parameters: dict[str, Any] | None,
) -> None
```

Patch legacy RoPE type fields for backwards compatibility with older custom models which would otherwise fail to load.

Source code in `vllm/transformers_utils/config.py`

```
defpatch_legacy_rope_type(rope_parameters: dict[str, Any] | None) -> None:
"""Patch legacy RoPE type fields for backwards compatibility with
    older custom models which would otherwise fail to load."""

    # No RoPE parameters to patch
    if rope_parameters is None:
        return

    def_patch_legacy_rope_type(rope_parameters: dict[str, Any]) -> None:
        # Case 1: Both legacy and modern fields present - check for conflicts
        if "rope_type" in rope_parameters and "type" in rope_parameters:
            rope_type = rope_parameters["rope_type"]
            rope_type_legacy = rope_parameters["type"]
            if (rope_type_legacy == "su" and rope_type == "longrope") or (
                rope_type_legacy == "mrope" and rope_type == "default"
            ):
                pass  # No action needed
            elif rope_type != rope_type_legacy:
                raise ValueError(
                    f"Found conflicts between 'rope_type={rope_type}' (modern "
                    f"field) and 'type={rope_type_legacy}' (legacy field). "
                    "You should only specify one of them."
                )
        # Case 2: Only legacy field present - patch to modern format with warning
        if "rope_type" not in rope_parameters and "type" in rope_parameters:
            rope_parameters["rope_type"] = rope_parameters["type"]
            logger.info("Replacing legacy 'type' key with 'rope_type'")
        # Case 3: No rope_type field at all - cannot determine RoPE type, raise error
        if "rope_type" not in rope_parameters:
            raise ValueError("rope_parameters should have a 'rope_type' key")
        # Patch legacy rope_type values with warning
        if rope_parameters["rope_type"] == "su":
            rope_parameters["rope_type"] = "longrope"
            logger.warning("Replacing legacy rope_type 'su' with 'longrope'")
        elif rope_parameters["rope_type"] == "mrope":
            if "mrope_section" not in rope_parameters:
                raise ValueError(
                    "Legacy rope_type 'mrope' requires "
                    "'mrope_section' in rope_parameters"
                )
            rope_parameters["rope_type"] = "default"
            logger.warning("Replacing legacy rope_type 'mrope' with 'default'")

    # Handle nested rope_parameters in interleaved sliding attention models
    if is_rope_parameters_nested(rope_parameters):
        for rope_parameters_layer_type in rope_parameters.values():
            _patch_legacy_rope_type(rope_parameters_layer_type)
    else:
        _patch_legacy_rope_type(rope_parameters)
```

## patch\_rope\_parameters [¶](#vllm.transformers_utils.config.patch_rope_parameters "Permanent link")

```
patch_rope_parameters(config: PretrainedConfig) -> None
```

Provide backwards compatibility for RoPE.

Source code in `vllm/transformers_utils/config.py`

```
defpatch_rope_parameters(config: PretrainedConfig) -> None:
"""Provide backwards compatibility for RoPE."""
    fromvllm.config.utilsimport getattr_iter

    # Older custom models may use non-standard field names
    # which need patching for both Transformers v4 and v5.
    names = ["rope_theta", "rotary_emb_base"]
    rope_theta = getattr_iter(config, names, None, warn=True)
    names = ["partial_rotary_factor", "rotary_pct", "rotary_emb_fraction"]
    partial_rotary_factor = getattr_iter(config, names, None, warn=True)
    ompe = getattr(config, "original_max_position_embeddings", None)

    if Version(version("transformers")) < Version("5.0.0"):
        # Transformers v4 installed, legacy config fields may be present.
        if is_rope_parameters_nested(getattr(config, "rope_parameters", {})):
            # Loading nested rope_parameters (from Transformers v5) in Transformers v4.
            # Skip legacy patching since it should already be in the correct format.
            pass
        else:
            if (rope_scaling := getattr(config, "rope_scaling", None)) is not None:
                config.rope_parameters = rope_scaling
            if (
                rope_theta is not None
                or partial_rotary_factor is not None
                or ompe is not None
            ) and not getattr(config, "rope_parameters", None):
                config.rope_parameters = {"rope_type": "default"}
            # Patch legacy fields into rope_parameters
            if rope_theta is not None:
                config.rope_parameters["rope_theta"] = rope_theta
            if partial_rotary_factor is not None:
                config.rope_parameters["partial_rotary_factor"] = partial_rotary_factor
            if ompe is not None:
                config.rope_parameters["original_max_position_embeddings"] = ompe
            patch_legacy_rope_type(getattr(config, "rope_parameters", None))
    elif rope_theta is not None or getattr(config, "rope_parameters", None):
        # Transformers v5 installed
        # Patch these fields in case they used non-standard names
        if rope_theta is not None:
            config.rope_theta = rope_theta
        if partial_rotary_factor is not None:
            config.partial_rotary_factor = partial_rotary_factor
        # Standardize and validate RoPE parameters
        patch_legacy_rope_type(getattr(config, "rope_parameters", None))
        config.standardize_rope_params()
        config.validate_rope()
```

## register\_config\_parser [¶](#vllm.transformers_utils.config.register_config_parser "Permanent link")

```
register_config_parser(config_format: str)
```

Register a customized vllm config parser. When a config format is not supported by vllm, you can register a customized config parser to support it. Args: config\_format (str): The config parser format name. Examples:

```
 >>> from vllm.transformers_utils.config import (get_config_parser,
                                                 register_config_parser)
 >>> from vllm.transformers_utils.config_parser_base import ConfigParserBase
 >>>
 >>> @register_config_parser("custom_config_parser")
 ... class CustomConfigParser(ConfigParserBase):
 ...     def parse(
 ...         self,
 ...         model: Union[str, Path],
 ...         trust_remote_code: bool,
 ...         revision: str | None = None,
 ...         code_revision: str | None = None,
 ...         **kwargs,
 ...     ) -> tuple[dict, PretrainedConfig]:
 ...         raise NotImplementedError
 >>>
 >>> type(get_config_parser("custom_config_parser"))
 <class 'CustomConfigParser'>
```

Source code in `vllm/transformers_utils/config.py`

```
defregister_config_parser(config_format: str):
"""Register a customized vllm config parser.
     When a config format is not supported by vllm, you can register a customized
    config parser to support it.
     Args:
         config_format (str): The config parser format name.
     Examples:

         >>> from vllm.transformers_utils.config import (get_config_parser,
                                                         register_config_parser)
         >>> from vllm.transformers_utils.config_parser_base import ConfigParserBase
         >>>
         >>> @register_config_parser("custom_config_parser")
         ... class CustomConfigParser(ConfigParserBase):
         ...     def parse(
         ...         self,
         ...         model: Union[str, Path],
         ...         trust_remote_code: bool,
         ...         revision: str | None = None,
         ...         code_revision: str | None = None,
         ...         **kwargs,
         ...     ) -> tuple[dict, PretrainedConfig]:
         ...         raise NotImplementedError
         >>>
         >>> type(get_config_parser("custom_config_parser"))
         <class 'CustomConfigParser'>
    """  # noqa: E501

    def_wrapper(config_parser_cls):
        if config_format in _CONFIG_FORMAT_TO_CONFIG_PARSER:
            logger.warning(
                "Config format `%s` is already registered, and will be "
                "overwritten by the new parser class `%s`.",
                config_format,
                config_parser_cls,
            )
        if not issubclass(config_parser_cls, ConfigParserBase):
            raise ValueError(
                "The config parser must be a subclass of `ConfigParserBase`."
            )
        _CONFIG_FORMAT_TO_CONFIG_PARSER[config_format] = config_parser_cls
        logger.info(
            "Registered config parser `%s` with config format `%s`",
            config_parser_cls,
            config_format,
        )
        return config_parser_cls

    return _wrapper
```

## set\_default\_rope\_theta [¶](#vllm.transformers_utils.config.set_default_rope_theta "Permanent link")

```
set_default_rope_theta(
    config: PretrainedConfig, default_theta: float
) -> None
```

Some models may have no rope\_theta in their config but still use RoPE. This function sets a default rope\_theta if it's missing.

Source code in `vllm/transformers_utils/config.py`

```
defset_default_rope_theta(config: PretrainedConfig, default_theta: float) -> None:
"""Some models may have no rope_theta in their config but still use RoPE.
    This function sets a default rope_theta if it's missing."""
    if getattr(config, "rope_parameters", None) is None:
        config.rope_parameters = {"rope_type": "default"}
    if "rope_theta" not in config.rope_parameters:
        config.rope_parameters["rope_theta"] = default_theta
```

## thinker\_uses\_mrope [¶](#vllm.transformers_utils.config.thinker_uses_mrope "Permanent link")

```
thinker_uses_mrope(config: PretrainedConfig) -> bool
```

Detect if the model contains a thinker config and it uses M-ROPE.

Source code in `vllm/transformers_utils/config.py`

```
defthinker_uses_mrope(config: PretrainedConfig) -> bool:
"""Detect if the model contains a thinker config and it uses M-ROPE."""
    thinker_config = getattr(config, "thinker_config", None)
    if thinker_config is None:
        return False

    thinker_text_config = getattr(thinker_config, "text_config", None)
    if thinker_text_config is None:
        return False

    return uses_mrope(thinker_text_config)
```

## uses\_mrope [¶](#vllm.transformers_utils.config.uses_mrope "Permanent link")

```
uses_mrope(config: PretrainedConfig) -> bool
```

Detect if the model with this config uses M-ROPE.

Source code in `vllm/transformers_utils/config.py`

```
defuses_mrope(config: PretrainedConfig) -> bool:
"""Detect if the model with this config uses M-ROPE."""
    return (
        _uses_mrope(config)
        or _uses_mrope(config.get_text_config())
        or thinker_uses_mrope(config)
    )
```

## uses\_xdrope\_dim [¶](#vllm.transformers_utils.config.uses_xdrope_dim "Permanent link")

```
uses_xdrope_dim(config: PretrainedConfig) -> int
```

Detect if the model with this config uses XD-ROPE.

Source code in `vllm/transformers_utils/config.py`

```
defuses_xdrope_dim(config: PretrainedConfig) -> int:
"""Detect if the model with this config uses XD-ROPE."""
    xdrope_section = getattr(config, "xdrope_section", None)
    if xdrope_section is not None and isinstance(xdrope_section, list):
        return len(xdrope_section)
    rope_scaling = getattr(config, "rope_scaling", None)
    if rope_scaling is None:
        return 0

    if isinstance(rope_scaling, dict) and "xdrope_section" in rope_scaling:
        xdrope_section = rope_scaling["xdrope_section"]
        if xdrope_section is not None and isinstance(xdrope_section, list):
            return len(xdrope_section)

    return 0
```