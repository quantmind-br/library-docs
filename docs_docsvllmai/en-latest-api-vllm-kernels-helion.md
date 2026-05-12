---
title: helion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/
source: sitemap
fetched_at: 2026-05-07T21:22:12.047953014-03:00
rendered_js: false
word_count: 350
summary: This document describes the ConfigManager and ConfigSet modules within the vLLM Helion integration, which handle the lifecycle, storage, and retrieval of kernel configuration data.
tags:
    - vllm
    - helion
    - kernel-management
    - configuration-management
    - singleton-pattern
    - python-api
category: api
---

Helion integration for vLLM.

Modules:

Name Description `config_manager`

Configuration management for Helion kernels.

`ops`

Auto-import all Helion op modules to trigger kernel registration.

`register`

vLLM Helion kernel registration with pre-tuned config selection.

`utils`

Utility functions for Helion kernel management.

## ConfigManager [¶](#vllm.kernels.helion.ConfigManager "Permanent link")

File-level configuration management for Helion kernels (global singleton).

Source code in `vllm/kernels/helion/config_manager.py`

```
classConfigManager:
"""File-level configuration management for Helion kernels (global singleton)."""

    _instance: "ConfigManager | None" = None
    _instance_base_dir: Path | None = None

    def__new__(cls, base_dir: str | Path | None = None) -> "ConfigManager":
        resolved_base_dir = cls._resolve_base_dir(base_dir)

        if cls._instance is not None:
            if cls._instance_base_dir != resolved_base_dir:
                raise ValueError(
                    f"ConfigManager singleton already exists with base_dir "
                    f"'{cls._instance_base_dir}', cannot create with different "
                    f"base_dir '{resolved_base_dir}'"
                )
            return cls._instance

        instance = super().__new__(cls)
        cls._instance = instance
        cls._instance_base_dir = resolved_base_dir
        return instance

    def__init__(self, base_dir: str | Path | None = None):
        if hasattr(self, "_base_dir"):
            return

        self._base_dir = self._resolve_base_dir(base_dir)
        logger.debug("ConfigManager initialized with base_dir: %s", self._base_dir)

    @staticmethod
    def_resolve_base_dir(base_dir: str | Path | None) -> Path:
        if base_dir is not None:
            return Path(base_dir).resolve()
        return (Path(__file__).parent / "configs").resolve()

    @classmethod
    defget_instance(cls) -> "ConfigManager":
        if cls._instance is None:
            raise RuntimeError(
                "ConfigManager instance has not been created. "
                "Call ConfigManager(base_dir=...) first to initialize."
            )
        return cls._instance

    @classmethod
    defreset_instance(cls) -> None:
"""For testing purposes only."""
        cls._instance = None
        cls._instance_base_dir = None

    defget_kernel_dir(self, kernel_name: str) -> Path:
        return self._base_dir / kernel_name

    defget_config_file_path(
        self, kernel_name: str, platform: str | None = None
    ) -> Path:
        if platform is not None:
            return self.get_kernel_dir(kernel_name) / f"{platform}.json"
        return self.get_kernel_dir(kernel_name)

    defensure_base_dir_exists(self) -> Path:
        self._base_dir.mkdir(parents=True, exist_ok=True)
        return self._base_dir

    defensure_base_dir_writable(self) -> None:
        self.ensure_base_dir_exists()
        test_file = self._base_dir / ".write_test"
        try:
            test_file.write_text("test")
            test_file.unlink()
        except OSError as e:
            raise OSError(
                f"Config directory '{self._base_dir}' is not writable: {e}"
            ) frome

    def_load_platform_file(self, kernel_name: str, platform: str) -> dict[str, Any]:
        config_path = self.get_config_file_path(kernel_name, platform)
        if not config_path.exists():
            return {}
        try:
            with open(config_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            logger.error("Failed to load config file %s: %s", config_path, e)
            return {}

    defload_config_set(self, kernel_name: str) -> ConfigSet:
        kernel_dir = self.get_kernel_dir(kernel_name)
        if not kernel_dir.is_dir():
            return ConfigSet.from_dict(kernel_name, {})

        data: dict[str, Any] = {}
        for platform_file in sorted(kernel_dir.glob("*.json")):
            platform = platform_file.stem
            try:
                with open(platform_file) as f:
                    platform_data = json.load(f)
                data[platform] = platform_data
            except (json.JSONDecodeError, OSError) as e:
                logger.error("Failed to load config file %s: %s", platform_file, e)

        return ConfigSet.from_dict(kernel_name, data)

    defget_platform_configs(
        self, kernel_name: str, platform: str
    ) -> dict[str, helion.Config]:
        platform_data = self._load_platform_file(kernel_name, platform)
        if not platform_data:
            return {}
        config_set = ConfigSet.from_dict(kernel_name, {platform: platform_data})
        config_keys = config_set.get_config_keys(platform)
        return {
            config_key: config_set.get_config(platform, config_key)
            for config_key in config_keys
        }

    defsave_config_set(self, config_set: ConfigSet) -> Path:
        kernel_dir = self.get_kernel_dir(config_set.kernel_name)
        kernel_dir.mkdir(parents=True, exist_ok=True)

        full_data = config_set.to_dict()
        for platform, platform_data in full_data.items():
            platform_path = kernel_dir / f"{platform}.json"
            with open(platform_path, "w") as f:
                json.dump(platform_data, f, indent=2)
            logger.info("Saved config to: %s", platform_path)

        return kernel_dir

    defsave_configs(
        self,
        kernel_name: str,
        platform: str,
        configs: dict[str, "helion.Config"],
    ) -> Path:
"""Save configs for a kernel/platform, merging with existing."""
        platform_data = self._load_platform_file(kernel_name, platform)
        for config_key, config in configs.items():
            platform_data[config_key] = json.loads(config.to_json())

        platform_path = self.get_config_file_path(kernel_name, platform)
        platform_path.parent.mkdir(parents=True, exist_ok=True)
        with open(platform_path, "w") as f:
            json.dump(platform_data, f, indent=2)

        logger.info("Saved config to: %s", platform_path)
        return platform_path

    defconfig_exists(self, kernel_name: str, platform: str, config_key: str) -> bool:
        platform_data = self._load_platform_file(kernel_name, platform)
        return config_key in platform_data
```

### reset\_instance `classmethod` [¶](#vllm.kernels.helion.ConfigManager.reset_instance "Permanent link")

For testing purposes only.

Source code in `vllm/kernels/helion/config_manager.py`

```
@classmethod
defreset_instance(cls) -> None:
"""For testing purposes only."""
    cls._instance = None
    cls._instance_base_dir = None
```

### save\_configs [¶](#vllm.kernels.helion.ConfigManager.save_configs "Permanent link")

Save configs for a kernel/platform, merging with existing.

Source code in `vllm/kernels/helion/config_manager.py`

```
defsave_configs(
    self,
    kernel_name: str,
    platform: str,
    configs: dict[str, "helion.Config"],
) -> Path:
"""Save configs for a kernel/platform, merging with existing."""
    platform_data = self._load_platform_file(kernel_name, platform)
    for config_key, config in configs.items():
        platform_data[config_key] = json.loads(config.to_json())

    platform_path = self.get_config_file_path(kernel_name, platform)
    platform_path.parent.mkdir(parents=True, exist_ok=True)
    with open(platform_path, "w") as f:
        json.dump(platform_data, f, indent=2)

    logger.info("Saved config to: %s", platform_path)
    return platform_path
```

## ConfigSet [¶](#vllm.kernels.helion.ConfigSet "Permanent link")

In-memory collection of Helion configs with lookup/query capabilities.

Source code in `vllm/kernels/helion/config_manager.py`

```
classConfigSet:
"""In-memory collection of Helion configs with lookup/query capabilities."""

    # Type alias for nested config structure:
    # platform -> config_key -> helion.Config
    _ConfigDict = dict[str, dict[str, "helion.Config"]]

    def__init__(self, kernel_name: str):
        self._kernel_name = kernel_name
        self._configs: ConfigSet._ConfigDict = {}

    @property
    defkernel_name(self) -> str:
        return self._kernel_name

    defget_config(self, platform: str, config_key: str) -> helion.Config:
        platform_dict = self._configs.get(platform)
        if platform_dict is None:
            avail_platforms = self.get_platforms()
            # TODO(@gmagogsfm): add a CLI/env override flag so users can
            # directly specify a platform name instead of relying on
            # auto-detection, and suggest it in this error message.
            raise KeyError(
                f"Config not found for kernel '{self._kernel_name}': "
                f"platform '{platform}' not found. "
                f"Available platforms: {avail_platformsor'(none)'}. "
                f"If your GPU is a variant of a supported platform, "
                f"consider adding a mapping in _GPU_NAME_ALIASES in "
                f"vllm/kernels/helion/utils.py, or run "
                f"scripts/autotune_helion_kernels.py to generate configs "
                f"for your platform."
            )

        config = platform_dict.get(config_key)
        if config is None:
            avail_keys = self.get_config_keys(platform)
            raise KeyError(
                f"Config not found for kernel '{self._kernel_name}': "
                f"config_key '{config_key}' not found for platform '{platform}'. "
                f"Available config_keys: {avail_keysor'(none)'}"
            )

        return config

    defget_platforms(self) -> list[str]:
        return sorted(self._configs.keys())

    defget_config_keys(self, platform: str) -> list[str]:
        platform_dict = self._configs.get(platform.lower())
        if platform_dict is None:
            return []
        return sorted(platform_dict.keys())

    defto_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}

        for platform, config_keys_dict in self._configs.items():
            result[platform] = {}

            for config_key, config in config_keys_dict.items():
                result[platform][config_key] = json.loads(config.to_json())

        return result

    @classmethod
    deffrom_dict(cls, kernel_name: str, data: dict[str, Any]) -> "ConfigSet":
        config_set = cls(kernel_name)
        count = 0

        for platform, platform_data in data.items():
            if platform not in config_set._configs:
                config_set._configs[platform] = {}

            for config_key, config_data in platform_data.items():
                config = helion.Config(**config_data)
                config_set._configs[platform][config_key] = config
                count += 1

        if count > 0:
            logger.debug(
                "Loaded %d configs for kernel '%s'",
                count,
                kernel_name,
            )

        return config_set

    defset_config(
        self, platform: str, config_key: str, config: "helion.Config"
    ) -> None:
        platform = platform.lower()
        if platform not in self._configs:
            self._configs[platform] = {}
        self._configs[platform][config_key] = config
        logger.debug(
            "Set config for kernel '%s': platform='%s', key='%s'",
            self._kernel_name,
            platform,
            config_key,
        )

    defhas_config(self, platform: str, config_key: str) -> bool:
        platform = platform.lower()
        platform_dict = self._configs.get(platform)
        if platform_dict is None:
            return False
        return config_key in platform_dict
```

## ConfiguredHelionKernel [¶](#vllm.kernels.helion.ConfiguredHelionKernel "Permanent link")

A configured Helion kernel bound to a specific platform.

Source code in `vllm/kernels/helion/register.py`

```
classConfiguredHelionKernel:
"""A configured Helion kernel bound to a specific platform."""

    def__init__(
        self,
        op_name: str,
        config_picker: Callable[[tuple[Any, ...], list[str]], str | None] | None,
        raw_kernel_func: Callable,
        helion_settings: "helion.Settings | None" = None,
    ):
        self.op_name = op_name
        self.config_picker = config_picker
        self.raw_kernel_func = raw_kernel_func
        self.helion_settings = helion_settings
        self._decorated_kernel = self._create_decorated_kernel()

    def__call__(self, *args, **kwargs):
        return self._decorated_kernel(*args, **kwargs)

    def_create_key_computer(self):
"""
        Create a key computer function derived from the config picker.

        The returned function receives kernel arguments unpacked (*args) to match
        Helion's key signature (called as self._key_fn(*args)).
        """
        if self.config_picker is None:
            raise RuntimeError(
                f"No config picker registered for kernel '{self.op_name}'. "
                f"A config_picker must be provided to register_kernel()."
            )

        # After None check, config_picker is guaranteed to be non-None
        assert self.config_picker is not None

        defkey_computer(*args):
            config_keys = list(self.configs.keys())
            # Cast is safe because we checked for None above
            config_picker = cast(
                Callable[[tuple[Any, ...], list[str]], str | None], self.config_picker
            )
            selected_key = config_picker(args, config_keys)
            if selected_key:
                return selected_key
            return "default" if "default" in self.configs else None

        return key_computer

    def_create_config_selector(self, key_computer):
        defconfig_selector(args):
            # args is a tuple; key_computer expects unpacked args
            selected_config_key = key_computer(*args)

            if selected_config_key is None:
                raise ValueError(
                    f"Config picker returned None for kernel '{self.op_name}' "
                    f"with available config keys: {list(self.configs.keys())}"
                )

            if selected_config_key not in self.configs:
                raise ValueError(
                    f"Config picker returned invalid config key "
                    f"'{selected_config_key}' for kernel '{self.op_name}'. "
                    f"Available keys: {list(self.configs.keys())}"
                )

            return self.configs[selected_config_key]

        return config_selector

    def_load_platform_configs(self) -> None:
        fromvllm.kernels.helion.config_managerimport ConfigManager
        fromvllm.kernels.helion.utilsimport get_canonical_gpu_name

        self.platform = get_canonical_gpu_name()
        config_manager = ConfigManager()
        self.configs = config_manager.get_platform_configs(self.op_name, self.platform)

        if not self.configs:
            raise ValueError(
                f"No configs available for kernel '{self.op_name}' "
                f"on platform '{self.platform}'"
            )

    def_create_decorated_kernel(self) -> Callable[..., Any]:
        self._load_platform_configs()

        key_computer = self._create_key_computer()
        config_selector = self._create_config_selector(key_computer)

        extra_kwargs = {
            "autotuner_fn": lambda _, args: PresetConfigSearch(args, config_selector),
            "key": key_computer,
        }

        logger.debug(
            "Creating decorated kernel %s with custom autotuner on platform %s",
            self.op_name,
            self.platform,
        )
        return create_helion_decorated_kernel(
            self.raw_kernel_func, self.helion_settings, extra_kwargs
        )
```

### \_create\_key\_computer [¶](#vllm.kernels.helion.ConfiguredHelionKernel._create_key_computer "Permanent link")

Create a key computer function derived from the config picker.

The returned function receives kernel arguments unpacked (*args) to match Helion's key signature (called as self.\_key\_fn(*args)).

Source code in `vllm/kernels/helion/register.py`

```
def_create_key_computer(self):
"""
    Create a key computer function derived from the config picker.

    The returned function receives kernel arguments unpacked (*args) to match
    Helion's key signature (called as self._key_fn(*args)).
    """
    if self.config_picker is None:
        raise RuntimeError(
            f"No config picker registered for kernel '{self.op_name}'. "
            f"A config_picker must be provided to register_kernel()."
        )

    # After None check, config_picker is guaranteed to be non-None
    assert self.config_picker is not None

    defkey_computer(*args):
        config_keys = list(self.configs.keys())
        # Cast is safe because we checked for None above
        config_picker = cast(
            Callable[[tuple[Any, ...], list[str]], str | None], self.config_picker
        )
        selected_key = config_picker(args, config_keys)
        if selected_key:
            return selected_key
        return "default" if "default" in self.configs else None

    return key_computer
```

## HelionKernelWrapper [¶](#vllm.kernels.helion.HelionKernelWrapper "Permanent link")

Wrapper for Helion kernels with pre-tuned config selection and HOP support.

Source code in `vllm/kernels/helion/register.py`

```
classHelionKernelWrapper:
"""Wrapper for Helion kernels with pre-tuned config selection and HOP support."""

    def__init__(
        self,
        raw_kernel_func: Callable,
        op_name: str,
        fake_impl: Callable,
        config_picker: Callable[[tuple[Any, ...], list[str]], str | None],
        helion_settings: "helion.Settings | None" = None,
        input_generator: Callable[[], dict[str, tuple[Any, ...]]] | None = None,
    ):
        # Validate helion_settings doesn't conflict with our custom autotuner
        validate_helion_settings(helion_settings, op_name)

        self.raw_kernel_func = raw_kernel_func
        self.op_name = op_name
        self._fake_impl = fake_impl
        self.helion_settings = helion_settings
        self._config_picker = config_picker
        self._input_generator = input_generator
        self._configured_kernel: ConfiguredHelionKernel | None = None
        # TODO(@gmagogsfm): Remove this disable flag once integrated with vLLM IR,
        # which handles op enablement/disablement.
        self._disabled = False
        self._disabled_reason: str | None = None

        try:
            if not _HOP_AVAILABLE:
                self._get_or_register_custom_op()
            else:
                self.get_configured_op()
        except ValueError as e:
            self._disabled = True
            self._disabled_reason = str(e)
            logger.warning(
                "Helion kernel '%s' is disabled: %s",
                op_name,
                self._disabled_reason,
            )

    def__call__(self, *args, **kwargs):
        if self._disabled:
            raise RuntimeError(
                f"Helion kernel '{self.op_name}' is disabled: {self._disabled_reason}"
            )
        if not _HOP_AVAILABLE:
            op = getattr(torch.ops.vllm_helion, self.op_name)
            return op(*args, **kwargs)
        assert self._configured_kernel is not None, (
            f"Kernel '{self.op_name}' was not initialized. "
            "Please open an issue on GitHub."
        )

        # During Dynamo tracing, this call will be intercepted by our custom
        # HelionKernelWrapperVariable and handled via proper HOP emission.
        # During eager execution, call the kernel directly.
        return self._configured_kernel(*args, **kwargs)

    defget_inputs(self) -> dict[str, tuple[Any, ...]]:
        if self._input_generator is None:
            raise NotImplementedError(
                f"No input generator registered for kernel '{self.op_name}'. "
                f"Use register_kernel(..., input_generator=...) to register one."
            )
        return self._input_generator()

    defrun_autotune(
        self,
        inputs: tuple[Any, ...],
        autotune_effort: str = "quick",
    ) -> Config:
"""Run autotuning for a single input configuration."""
        extra_kwargs = {
            "autotune_effort": autotune_effort,
            "autotune_ignore_errors": True,
        }
        autotune_kernel = create_helion_decorated_kernel(
            self.raw_kernel_func, self.helion_settings, extra_kwargs
        )
        return autotune_kernel.autotune(inputs)

    defget_configured_op(self) -> ConfiguredHelionKernel:
        if self._disabled:
            raise RuntimeError(
                f"Helion kernel '{self.op_name}' is disabled: {self._disabled_reason}"
            )
        if self._configured_kernel is None:
            self._configured_kernel = ConfiguredHelionKernel(
                op_name=self.op_name,
                config_picker=self._config_picker,
                raw_kernel_func=self.raw_kernel_func,
                helion_settings=self.helion_settings,
            )
        return self._configured_kernel

    def_get_or_register_custom_op(self) -> Any:
        if hasattr(torch.ops.vllm_helion, self.op_name):
            return getattr(torch.ops.vllm_helion, self.op_name)

        configured_kernel = self.get_configured_op()

        logger.info("Registering op: vllm_helion::%s", self.op_name)
        direct_register_custom_op(
            op_name=self.op_name,
            op_func=configured_kernel._decorated_kernel,
            mutates_args=None,
            fake_impl=self._fake_impl,
            target_lib=vllm_helion_lib,
        )
        return getattr(torch.ops.vllm_helion, self.op_name)
```

### run\_autotune [¶](#vllm.kernels.helion.HelionKernelWrapper.run_autotune "Permanent link")

```
run_autotune(
    inputs: tuple[Any, ...], autotune_effort: str = "quick"
) -> Config
```

Run autotuning for a single input configuration.

Source code in `vllm/kernels/helion/register.py`

```
defrun_autotune(
    self,
    inputs: tuple[Any, ...],
    autotune_effort: str = "quick",
) -> Config:
"""Run autotuning for a single input configuration."""
    extra_kwargs = {
        "autotune_effort": autotune_effort,
        "autotune_ignore_errors": True,
    }
    autotune_kernel = create_helion_decorated_kernel(
        self.raw_kernel_func, self.helion_settings, extra_kwargs
    )
    return autotune_kernel.autotune(inputs)
```

## canonicalize\_gpu\_name [¶](#vllm.kernels.helion.canonicalize_gpu_name "Permanent link")

```
canonicalize_gpu_name(name: str) -> str
```

Canonicalize GPU name for use as a platform identifier.

Converts to lowercase, replaces spaces and hyphens with underscores, and maps known variant names to their canonical form via \_GPU\_NAME\_ALIASES. e.g., "NVIDIA H100 80GB HBM3" -&gt; "nvidia\_h100" "NVIDIA A100-SXM4-80GB" -&gt; "nvidia\_a100" "AMD Instinct MI300X" -&gt; "amd\_instinct\_mi300x"

Source code in `vllm/kernels/helion/utils.py`

```
defcanonicalize_gpu_name(name: str) -> str:
"""
    Canonicalize GPU name for use as a platform identifier.

    Converts to lowercase, replaces spaces and hyphens with underscores,
    and maps known variant names to their canonical form via _GPU_NAME_ALIASES.
    e.g., "NVIDIA H100 80GB HBM3" -> "nvidia_h100"
          "NVIDIA A100-SXM4-80GB" -> "nvidia_a100"
          "AMD Instinct MI300X"   -> "amd_instinct_mi300x"
    """
    if not name or not name.strip():
        raise ValueError("GPU name cannot be empty")
    name = name.lower()
    name = name.replace(" ", "_")
    name = name.replace("-", "_")
    if name in _GPU_NAME_ALIASES:
        return _GPU_NAME_ALIASES[name]
    return name
```

## register\_kernel [¶](#vllm.kernels.helion.register_kernel "Permanent link")

```
register_kernel(
    op_name: str | None = None,
    *,
    config_picker: Callable[
        [tuple[Any, ...], list[str]], str | None
    ],
    fake_impl: Callable | None = None,
    helion_settings: Settings | None = None,
    input_generator: Callable[
        [], dict[str, tuple[Any, ...]]
    ]
    | None = None,
) -> Callable[[Callable], HelionKernelWrapper]
```

Register a Helion kernel with pre-tuned config selection.

Wraps the kernel function in a HelionKernelWrapper that eagerly builds the configured kernel and (on older PyTorch) registers a custom op.

Parameters:

Name Type Description Default `config_picker` `Callable[[tuple[Any, ...], list[str]], str | None]`

Required. Function with signature `(args: tuple, config_keys: list[str]) -> str | None` that picks the best config key from available options. Return `None` to fall back to `"default"`.

Example::

```
def pick_config(args, config_keys):
    x = args[0]
    hidden_size = x.shape[-1]
    batch_size = x.shape[0]
    for key in config_keys:
        if key == f"hiddensize_{hidden_size}_batchsize_{batch_size}":
            return key
    return "default" if "default" in config_keys else None
```

*required* `input_generator` `Callable[[], dict[str, tuple[Any, ...]]] | None`

Optional. Function that returns `dict[str, tuple]` where each key is a configuration identifier (e.g. `"4096"`, `"hidden_4096"`) and each value is a tuple of arguments to pass to the kernel.

Example::

```
def generate_inputs():
    return {
        "4096": (torch.randn(4096, device="cuda"), 0.5),
        "8192": (torch.randn(8192, device="cuda"), 0.5),
    }
```

`None`

Source code in `vllm/kernels/helion/register.py`

```
defregister_kernel(
    op_name: str | None = None,
    *,
    config_picker: Callable[[tuple[Any, ...], list[str]], str | None],
    fake_impl: Callable | None = None,
    helion_settings: "helion.Settings | None" = None,
    input_generator: Callable[[], dict[str, tuple[Any, ...]]] | None = None,
) -> Callable[[Callable], HelionKernelWrapper]:
"""Register a Helion kernel with pre-tuned config selection.

    Wraps the kernel function in a HelionKernelWrapper that eagerly builds
    the configured kernel and (on older PyTorch) registers a custom op.

    Args:
        config_picker: Required. Function with signature
            ``(args: tuple, config_keys: list[str]) -> str | None``
            that picks the best config key from available options.
            Return ``None`` to fall back to ``"default"``.

            Example::

                def pick_config(args, config_keys):
                    x = args[0]
                    hidden_size = x.shape[-1]
                    batch_size = x.shape[0]
                    for key in config_keys:
                        if key == f"hiddensize_{hidden_size}_batchsize_{batch_size}":
                            return key
                    return "default" if "default" in config_keys else None

        input_generator: Optional. Function that returns
            ``dict[str, tuple]`` where each key is a configuration
            identifier (e.g. ``"4096"``, ``"hidden_4096"``) and each
            value is a tuple of arguments to pass to the kernel.

            Example::

                def generate_inputs():
                    return {
                        "4096": (torch.randn(4096, device="cuda"), 0.5),
                        "8192": (torch.randn(8192, device="cuda"), 0.5),
                    }
    """

    defdecorator(kernel_func: Callable) -> HelionKernelWrapper:
        final_op_name = op_name if op_name else kernel_func.__name__

        if final_op_name in _REGISTERED_KERNELS:
            raise ValueError(
                f"Helion kernel '{final_op_name}' is already registered. "
                f"Use a different op_name or check for duplicate registrations."
            )

        final_fake_impl = fake_impl
        if final_fake_impl is None:
            final_fake_impl = infer_fake_impl(kernel_func, helion_settings)
            logger.debug(
                "Auto-generated fake_impl for Helion kernel '%s'",
                kernel_func.__name__,
            )

        kernel_wrapper = HelionKernelWrapper(
            raw_kernel_func=kernel_func,
            op_name=final_op_name,
            fake_impl=final_fake_impl,
            config_picker=config_picker,
            helion_settings=helion_settings,
            input_generator=input_generator,
        )

        _REGISTERED_KERNELS[final_op_name] = kernel_wrapper

        logger.info(
            "Registered Helion kernel '%s' as HelionKernelWrapper",
            kernel_func.__name__,
        )

        return kernel_wrapper

    return decorator
```