---
title: tensorizer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/tensorizer/
source: sitemap
fetched_at: 2026-05-07T21:28:50.905730739-03:00
rendered_js: false
word_count: 564
summary: This document defines the TensorizerArgs dataclass, which manages configuration parameters for the tensorizer deserializer in vLLM, including S3 access, encryption, and performance tuning settings.
tags:
    - vllm
    - tensorizer
    - model-loading
    - configuration
    - deserialization
    - s3-integration
category: api
---

## TensorizerArgs `dataclass` [¶](#vllm.model_executor.model_loader.tensorizer.TensorizerArgs "Permanent link")

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
@dataclass
classTensorizerArgs:
    tensorizer_uri: str | None = None
    tensorizer_dir: str | None = None
    encryption_keyfile: str | None = None

    def__init__(self, tensorizer_config: TensorizerConfig):
        for k, v in tensorizer_config.items():
            setattr(self, k, v)
        self.file_obj = tensorizer_config.tensorizer_uri
        self.s3_access_key_id = (
            tensorizer_config.s3_access_key_id or envs.S3_ACCESS_KEY_ID
        )
        self.s3_secret_access_key = (
            tensorizer_config.s3_secret_access_key or envs.S3_SECRET_ACCESS_KEY
        )
        self.s3_endpoint = tensorizer_config.s3_endpoint or envs.S3_ENDPOINT_URL

        self.stream_kwargs = {
            "s3_access_key_id": tensorizer_config.s3_access_key_id,
            "s3_secret_access_key": tensorizer_config.s3_secret_access_key,
            "s3_endpoint": tensorizer_config.s3_endpoint,
            **(tensorizer_config.stream_kwargs or {}),
        }

        self.deserialization_kwargs = {
            "verify_hash": tensorizer_config.verify_hash,
            "encryption": tensorizer_config.encryption_keyfile,
            "num_readers": tensorizer_config.num_readers,
            **(tensorizer_config.deserialization_kwargs or {}),
        }

        if self.encryption_keyfile:
            with open_stream(
                tensorizer_config.encryption_keyfile,
                **self.stream_kwargs,
            ) as stream:
                key = stream.read()
                decryption_params = DecryptionParams.from_key(key)
                self.deserialization_kwargs["encryption"] = decryption_params

    @staticmethod
    defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Tensorizer CLI arguments"""

        # Tensorizer options arg group
        group = parser.add_argument_group(
            "tensorizer options",
            description=(
                "Options for configuring the behavior of the"
                " tensorizer deserializer when "
                "load_format=tensorizer is specified when "
                "initializing an LLMEngine, either via the CLI "
                "when running the vLLM OpenAI inference server "
                "with a JSON string passed to "
                "--model-loader-extra-config or as arguments given "
                "to TensorizerConfig when passed to "
                "model_loader_extra_config in the constructor "
                "for LLMEngine."
            ),
        )

        group.add_argument(
            "--tensorizer-uri",
            type=str,
            help="Path to serialized model tensors. Can be a local file path,"
            " or an HTTP(S) or S3 URI.",
        )
        group.add_argument(
            "--verify-hash",
            action="store_true",
            help="If enabled, the hashes of each tensor will be verified"
            " against the hashes stored in the file metadata. An exception"
            " will be raised if any of the hashes do not match.",
        )
        group.add_argument(
            "--encryption-keyfile",
            type=str,
            default=None,
            help="The file path to a binary file containing a binary key to "
            "use for decryption. Can be a file path or S3 network URI.",
        )
        group.add_argument(
            "--num-readers",
            default=None,
            type=int,
            help="Controls how many threads are allowed to read concurrently "
            "from the source file. Default is `None`, which will dynamically "
            "set the number of readers based on the available resources "
            "and model size. This greatly increases performance.",
        )
        group.add_argument(
            "--s3-access-key-id",
            type=str,
            default=None,
            help="The access key for the S3 bucket. Can also be set via the "
            "S3_ACCESS_KEY_ID environment variable.",
        )
        group.add_argument(
            "--s3-secret-access-key",
            type=str,
            default=None,
            help="The secret access key for the S3 bucket. Can also be set via "
            "the S3_SECRET_ACCESS_KEY environment variable.",
        )
        group.add_argument(
            "--s3-endpoint",
            type=str,
            default=None,
            help="The endpoint for the S3 bucket. Can also be set via the "
            "S3_ENDPOINT_URL environment variable.",
        )

        return parser

    @classmethod
    deffrom_cli_args(cls, args: argparse.Namespace) -> "TensorizerArgs":
        attrs = [attr.name for attr in dataclasses.fields(cls)]
        tensorizer_args = cls(
            **{attr: getattr(args, attr) for attr in attrs if hasattr(args, attr)}
        )
        return tensorizer_args
```

### add\_cli\_args `staticmethod` [¶](#vllm.model_executor.model_loader.tensorizer.TensorizerArgs.add_cli_args "Permanent link")

Tensorizer CLI arguments

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
@staticmethod
defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Tensorizer CLI arguments"""

    # Tensorizer options arg group
    group = parser.add_argument_group(
        "tensorizer options",
        description=(
            "Options for configuring the behavior of the"
            " tensorizer deserializer when "
            "load_format=tensorizer is specified when "
            "initializing an LLMEngine, either via the CLI "
            "when running the vLLM OpenAI inference server "
            "with a JSON string passed to "
            "--model-loader-extra-config or as arguments given "
            "to TensorizerConfig when passed to "
            "model_loader_extra_config in the constructor "
            "for LLMEngine."
        ),
    )

    group.add_argument(
        "--tensorizer-uri",
        type=str,
        help="Path to serialized model tensors. Can be a local file path,"
        " or an HTTP(S) or S3 URI.",
    )
    group.add_argument(
        "--verify-hash",
        action="store_true",
        help="If enabled, the hashes of each tensor will be verified"
        " against the hashes stored in the file metadata. An exception"
        " will be raised if any of the hashes do not match.",
    )
    group.add_argument(
        "--encryption-keyfile",
        type=str,
        default=None,
        help="The file path to a binary file containing a binary key to "
        "use for decryption. Can be a file path or S3 network URI.",
    )
    group.add_argument(
        "--num-readers",
        default=None,
        type=int,
        help="Controls how many threads are allowed to read concurrently "
        "from the source file. Default is `None`, which will dynamically "
        "set the number of readers based on the available resources "
        "and model size. This greatly increases performance.",
    )
    group.add_argument(
        "--s3-access-key-id",
        type=str,
        default=None,
        help="The access key for the S3 bucket. Can also be set via the "
        "S3_ACCESS_KEY_ID environment variable.",
    )
    group.add_argument(
        "--s3-secret-access-key",
        type=str,
        default=None,
        help="The secret access key for the S3 bucket. Can also be set via "
        "the S3_SECRET_ACCESS_KEY environment variable.",
    )
    group.add_argument(
        "--s3-endpoint",
        type=str,
        default=None,
        help="The endpoint for the S3 bucket. Can also be set via the "
        "S3_ENDPOINT_URL environment variable.",
    )

    return parser
```

## TensorizerConfig `dataclass` [¶](#vllm.model_executor.model_loader.tensorizer.TensorizerConfig "Permanent link")

Bases: `MutableMapping`

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
@dataclass
classTensorizerConfig(MutableMapping):
    tensorizer_uri: str | None = None
    tensorizer_dir: str | None = None
    vllm_tensorized: bool | None = None
    verify_hash: bool | None = None
    num_readers: int | None = None
    encryption_keyfile: str | None = None
    s3_access_key_id: str | None = None
    s3_secret_access_key: str | None = None
    s3_endpoint: str | None = None
    lora_dir: str | None = None
    stream_kwargs: dict[str, Any] | None = None
    serialization_kwargs: dict[str, Any] | None = None
    deserialization_kwargs: dict[str, Any] | None = None
    _extra_serialization_attrs: dict[str, Any] | None = field(init=False, default=None)
    model_class: type[torch.nn.Module] | None = field(init=False, default=None)
    hf_config: PretrainedConfig | None = field(init=False, default=None)
    dtype: str | torch.dtype | None = field(init=False, default=None)
    _is_sharded: bool = field(init=False, default=False)
    _fields: ClassVar[tuple[str, ...]]
    _keys: ClassVar[frozenset[str]]
"""Configuration class for Tensorizer settings.

    These settings configure the behavior of model serialization and 
    deserialization using Tensorizer.

    Attributes:
        tensorizer_uri: Path to serialized model tensors. Can be a local file 
            path or a S3 URI. This is a required field unless lora_dir is 
            provided and the config is meant to be used for the
            `tensorize_lora_adapter` function. Unless a `tensorizer_dir` or 
            `lora_dir` is passed to this object's initializer, this is 
            a required argument.
        tensorizer_dir: Path to a directory containing serialized model tensors,
            and all other potential model artifacts to load the model, such as 
            configs and tokenizer files. Can be passed instead of 
            `tensorizer_uri` where the `model.tensors` file will be assumed 
            to be in this directory.
        vllm_tensorized: If True, indicates that the serialized model is a 
            vLLM model. This is used to determine the behavior of the 
            TensorDeserializer when loading tensors from a serialized model.
            It is far faster to deserialize a vLLM model as it utilizes
            tensorizer's optimized GPU loading. Note that this is now
            deprecated, as serialized vLLM models are now automatically
            inferred as vLLM models.
        verify_hash: If True, the hashes of each tensor will be verified 
            against the hashes stored in the metadata. A `HashMismatchError` 
            will be raised if any of the hashes do not match.
        num_readers: Controls how many threads are allowed to read concurrently
            from the source file. Default is `None`, which will dynamically set
            the number of readers based on the number of available 
            resources and model size. This greatly increases performance.
        encryption_keyfile: File path to a binary file containing a  
            binary key to use for decryption. `None` (the default) means 
            no decryption. See the example script in 
            examples/others/tensorize_vllm_model.py. 
        s3_access_key_id: The access key for the S3 bucket. Can also be set via
            the S3_ACCESS_KEY_ID environment variable.
        s3_secret_access_key: The secret access key for the S3 bucket. Can also
            be set via the S3_SECRET_ACCESS_KEY environment variable.
        s3_endpoint: The endpoint for the S3 bucket. Can also be set via the
            S3_ENDPOINT_URL environment variable.
        lora_dir: Path to a directory containing LoRA adapter artifacts for 
            serialization or deserialization. When serializing LoRA adapters 
            this is the only necessary parameter to pass to this object's 
            initializer.
    """

    def__post_init__(self):
        # check if the configuration is for a sharded vLLM model
        self._is_sharded = (
            isinstance(self.tensorizer_uri, str)
            and re.search(r"%0\dd", self.tensorizer_uri) is not None
        )

        if self.tensorizer_dir and self.lora_dir:
            raise ValueError(
                "Only one of tensorizer_dir or lora_dir may be specified. "
                "Use lora_dir exclusively when serializing LoRA adapters, "
                "and tensorizer_dir or tensorizer_uri otherwise."
            )
        if self.tensorizer_dir and self.tensorizer_uri:
            logger.warning_once(
                "Provided both tensorizer_dir and tensorizer_uri. "
                "Inferring tensorizer_dir from tensorizer_uri as the "
                "latter takes precedence."
            )
            self.tensorizer_dir = os.path.dirname(self.tensorizer_uri)
        if not self.tensorizer_uri:
            if self.lora_dir:
                self.tensorizer_uri = f"{self.lora_dir}/adapter_model.tensors"
            elif self.tensorizer_dir:
                self.tensorizer_uri = f"{self.tensorizer_dir}/model.tensors"
            else:
                raise ValueError(
                    "Unable to resolve tensorizer_uri. "
                    "A valid tensorizer_uri or tensorizer_dir "
                    "must be provided for deserialization, and a "
                    "valid tensorizer_uri, tensorizer_uri, or "
                    "lora_dir for serialization."
                )
        else:
            self.tensorizer_dir = os.path.dirname(self.tensorizer_uri)

        if not self.serialization_kwargs:
            self.serialization_kwargs = {}
        if not self.deserialization_kwargs:
            self.deserialization_kwargs = {}

    defto_serializable(self) -> dict[str, Any]:
        # Due to TensorizerConfig needing to be msgpack-serializable, it needs
        # support for morphing back and forth between itself and its dict
        # representation

        # TensorizerConfig's representation as a dictionary is meant to be
        # linked to TensorizerConfig in such a way that the following is
        # technically initializable:
        # TensorizerConfig(**my_tensorizer_cfg.to_serializable())

        # This means the dict must not retain non-initializable parameters
        # and post-init attribute states

        # Also don't want to retain private and unset parameters, so only retain
        # not None values and public attributes

        raw_tc_dict = asdict(self)
        blacklisted = []

        if "tensorizer_uri" in raw_tc_dict and "tensorizer_dir" in raw_tc_dict:
            blacklisted.append("tensorizer_dir")

        if "tensorizer_dir" in raw_tc_dict and "lora_dir" in raw_tc_dict:
            blacklisted.append("tensorizer_dir")

        tc_dict = {}
        for k, v in raw_tc_dict.items():
            if (
                k not in blacklisted
                and k not in tc_dict
                and not k.startswith("_")
                and v is not None
            ):
                tc_dict[k] = v

        return tc_dict

    def_construct_tensorizer_args(self) -> "TensorizerArgs":
        return TensorizerArgs(self)  # type: ignore

    defverify_with_parallel_config(
        self,
        parallel_config: "ParallelConfig",
    ) -> None:
        if parallel_config.tensor_parallel_size > 1 and not self._is_sharded:
            raise ValueError(
                "For a sharded model, tensorizer_uri should include a"
                " string format template like '%04d' to be formatted"
                " with the rank of the shard"
            )

    defverify_with_model_config(self, model_config: "ModelConfig") -> None:
        if model_config.quantization is not None and self.tensorizer_uri is not None:
            logger.warning(
                "Loading a model using Tensorizer with quantization on vLLM"
                " is unstable and may lead to errors."
            )

    defopen_stream(self, tensorizer_args: "TensorizerArgs | None" = None):
        if tensorizer_args is None:
            tensorizer_args = self._construct_tensorizer_args()

        return open_stream(self.tensorizer_uri, **tensorizer_args.stream_kwargs)

    defkeys(self):
        return self._keys

    def__len__(self):
        return len(fields(self))

    def__iter__(self):
        return iter(self._fields)

    def__getitem__(self, item: str) -> Any:
        if item not in self.keys():
            raise KeyError(item)
        return getattr(self, item)

    def__setitem__(self, key: str, value: Any) -> None:
        if key not in self.keys():
            # Disallow modifying invalid keys
            raise KeyError(key)
        setattr(self, key, value)

    def__delitem__(self, key, /):
        if key not in self.keys():
            raise KeyError(key)
        delattr(self, key)
```

### \_keys `class-attribute` [¶](#vllm.model_executor.model_loader.tensorizer.TensorizerConfig._keys "Permanent link")

Configuration class for Tensorizer settings.

These settings configure the behavior of model serialization and deserialization using Tensorizer.

Attributes:

Name Type Description `tensorizer_uri`

Path to serialized model tensors. Can be a local file path or a S3 URI. This is a required field unless lora\_dir is provided and the config is meant to be used for the `tensorize_lora_adapter` function. Unless a `tensorizer_dir` or `lora_dir` is passed to this object's initializer, this is a required argument.

`tensorizer_dir`

Path to a directory containing serialized model tensors, and all other potential model artifacts to load the model, such as configs and tokenizer files. Can be passed instead of `tensorizer_uri` where the `model.tensors` file will be assumed to be in this directory.

`vllm_tensorized`

If True, indicates that the serialized model is a vLLM model. This is used to determine the behavior of the TensorDeserializer when loading tensors from a serialized model. It is far faster to deserialize a vLLM model as it utilizes tensorizer's optimized GPU loading. Note that this is now deprecated, as serialized vLLM models are now automatically inferred as vLLM models.

`verify_hash`

If True, the hashes of each tensor will be verified against the hashes stored in the metadata. A `HashMismatchError` will be raised if any of the hashes do not match.

`num_readers`

Controls how many threads are allowed to read concurrently from the source file. Default is `None`, which will dynamically set the number of readers based on the number of available resources and model size. This greatly increases performance.

`encryption_keyfile`

File path to a binary file containing a  
binary key to use for decryption. `None` (the default) means no decryption. See the example script in examples/others/tensorize\_vllm\_model.py.

`s3_access_key_id`

The access key for the S3 bucket. Can also be set via the S3\_ACCESS\_KEY\_ID environment variable.

`s3_secret_access_key`

The secret access key for the S3 bucket. Can also be set via the S3\_SECRET\_ACCESS\_KEY environment variable.

`s3_endpoint`

The endpoint for the S3 bucket. Can also be set via the S3\_ENDPOINT\_URL environment variable.

`lora_dir`

Path to a directory containing LoRA adapter artifacts for serialization or deserialization. When serializing LoRA adapters this is the only necessary parameter to pass to this object's initializer.

## \_resize\_lora\_embeddings [¶](#vllm.model_executor.model_loader.tensorizer._resize_lora_embeddings "Permanent link")

```
_resize_lora_embeddings(model: Module)
```

Modify LoRA embedding layers to use bigger tensors to allow for adapter added tokens.

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
def_resize_lora_embeddings(model: nn.Module):
"""Modify LoRA embedding layers to use bigger tensors
    to allow for adapter added tokens."""
    for child in model.modules():
        if (
            isinstance(child, VocabParallelEmbedding)
            and child.weight.shape[0] < child.num_embeddings_per_partition
        ):
            new_weight = torch.empty(
                child.num_embeddings_per_partition,
                child.embedding_dim,
                dtype=child.weight.dtype,
                device=child.weight.device,
            )
            new_weight[: child.weight.shape[0]].copy_(child.weight.data)
            new_weight[child.weight.shape[0] :].fill_(0)
            child.weight.data = new_weight
```

## is\_vllm\_tensorized [¶](#vllm.model_executor.model_loader.tensorizer.is_vllm_tensorized "Permanent link")

```
is_vllm_tensorized(
    tensorizer_config: TensorizerConfig,
) -> bool
```

Infer if the model is a vLLM model by checking the weights for a vLLM tensorized marker.

Parameters:

Name Type Description Default `tensorizer_config` `TensorizerConfig`

The TensorizerConfig object containing the tensorizer\_uri to the serialized model.

*required*

Returns:

Name Type Description `bool` `bool`

True if the model is a vLLM model, False otherwise.

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
defis_vllm_tensorized(tensorizer_config: "TensorizerConfig") -> bool:
"""
    Infer if the model is a vLLM model by checking the weights for
    a vLLM tensorized marker.

    Args:
        tensorizer_config: The TensorizerConfig object containing the
            tensorizer_uri to the serialized model.

    Returns:
        bool: True if the model is a vLLM model, False otherwise.
    """
    tensorizer_args = tensorizer_config._construct_tensorizer_args()
    deserializer = TensorDeserializer(
        open_stream(tensorizer_args.tensorizer_uri, **tensorizer_args.stream_kwargs),
        **tensorizer_args.deserialization_kwargs,
        lazy_load=True,
    )
    if tensorizer_config.vllm_tensorized:
        logger.warning(
            "Please note that newly serialized vLLM models are automatically "
            "inferred as vLLM models, so setting vllm_tensorized=True is "
            "only necessary for models serialized prior to this change."
        )
        return True
    return ".vllm_tensorized_marker" in deserializer
```

## tensorize\_lora\_adapter [¶](#vllm.model_executor.model_loader.tensorizer.tensorize_lora_adapter "Permanent link")

```
tensorize_lora_adapter(
    lora_path: str, tensorizer_config: TensorizerConfig
)
```

Uses tensorizer to serialize a LoRA adapter. Assumes that the files needed to load a LoRA adapter are a safetensors-format file called adapter\_model.safetensors and a json config file called adapter\_config.json.

Serializes the files in the tensorizer\_config.tensorizer\_dir

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
deftensorize_lora_adapter(lora_path: str, tensorizer_config: TensorizerConfig):
"""
    Uses tensorizer to serialize a LoRA adapter. Assumes that the files
    needed to load a LoRA adapter are a safetensors-format file called
    adapter_model.safetensors and a json config file called adapter_config.json.

    Serializes the files in the tensorizer_config.tensorizer_dir
    """
    importsafetensors

    fromvllm.lora.utilsimport get_adapter_absolute_path

    lora_dir = get_adapter_absolute_path(lora_path)

    tensor_path = config_path = ""

    for file in os.listdir(lora_dir):
        if file.startswith("adapter_model"):
            tensor_path = lora_dir + "/" + file
        if file.startswith("adapter_config"):
            config_path = lora_dir + "/" + file
        if tensor_path and config_path:
            break

    if tensor_path.endswith(".safetensors"):
        tensors = safetensors.torch.load_file(tensor_path)
    elif tensor_path.endswith(".bin"):
        tensors = torch.load(tensor_path, weights_only=True)
    else:
        raise ValueError(
            f"Unsupported adapter model file: {tensor_path}. "
            f"Must be a .safetensors or .bin file."
        )

    with open(config_path) as f:
        config = json.load(f)

    tensorizer_args = tensorizer_config._construct_tensorizer_args()

    with open_stream(
        f"{tensorizer_config.tensorizer_dir}/adapter_config.json",
        mode="wb+",
        **tensorizer_args.stream_kwargs,
    ) as f:
        f.write(json.dumps(config).encode("utf-8"))

    lora_uri = f"{tensorizer_config.tensorizer_dir}/adapter_model.tensors"
    with open_stream(lora_uri, mode="wb+", **tensorizer_args.stream_kwargs) as f:
        serializer = TensorSerializer(f)
        serializer.write_state_dict(tensors)
        serializer.close()

    logger.info(
        "Successfully serialized LoRA files to %s",
        str(tensorizer_config.tensorizer_dir),
    )
```

## tensorize\_vllm\_model [¶](#vllm.model_executor.model_loader.tensorizer.tensorize_vllm_model "Permanent link")

```
tensorize_vllm_model(
    engine_args: EngineArgs,
    tensorizer_config: TensorizerConfig,
    generate_keyfile: bool = True,
)
```

Utility to load a model and then serialize it with Tensorizer

Intended to be used separately from running a vLLM server since it creates its own Engine instance.

Source code in `vllm/model_executor/model_loader/tensorizer.py`

```
deftensorize_vllm_model(
    engine_args: "EngineArgs",
    tensorizer_config: TensorizerConfig,
    generate_keyfile: bool = True,
):
"""Utility to load a model and then serialize it with Tensorizer

    Intended to be used separately from running a vLLM server since it
    creates its own Engine instance.
    """
    engine_config = engine_args.create_engine_config()
    tensorizer_config.verify_with_model_config(engine_config.model_config)
    tensorizer_config.verify_with_parallel_config(engine_config.parallel_config)

    # generate the encryption key before creating the engine to support sharding
    if (
        generate_keyfile
        and (keyfile := tensorizer_config.encryption_keyfile) is not None
    ):
        encryption_params = EncryptionParams.random()
        with open_stream(
            keyfile,
            mode="wb+",
            s3_access_key_id=tensorizer_config.s3_access_key_id,
            s3_secret_access_key=tensorizer_config.s3_secret_access_key,
            s3_endpoint=tensorizer_config.s3_endpoint,
        ) as stream:
            stream.write(encryption_params.key)

    fromvllm.v1.engine.llm_engineimport LLMEngine

    engine = LLMEngine.from_vllm_config(engine_config)
    engine.collective_rpc(
        "save_tensorized_model",
        kwargs={"tensorizer_config": tensorizer_config.to_serializable()},
    )
```