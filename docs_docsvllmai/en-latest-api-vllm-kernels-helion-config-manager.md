---
title: config_manager - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/config_manager/
source: sitemap
fetched_at: 2026-05-07T21:22:13.938543556-03:00
rendered_js: false
word_count: 0
summary: This class provides a singleton interface for managing and persisting kernel configuration files within the Helion architecture.
tags:
    - singleton
    - configuration-management
    - python-class
    - json-serialization
    - file-system-operations
category: reference
---

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