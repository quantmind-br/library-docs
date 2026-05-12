---
title: registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/registry/
source: sitemap
fetched_at: 2026-05-07T21:33:10.005531039-03:00
rendered_js: false
word_count: 5
summary: This document defines the ModelRegistry class, which manages the registration, inspection, and resolution of deep learning model architectures within the vLLM framework.
tags:
    - model-registration
    - pytorch-integration
    - architecture-management
    - vllm-framework
    - dynamic-loading
    - transformer-integration
category: api
---

```
@dataclass
class_ModelRegistry:
    # Keyed by model_arch
    models: dict[str, _BaseRegisteredModel] = field(default_factory=dict)

    defget_supported_archs(self) -> Set[str]:
        return self.models.keys()

    defregister_model(
        self,
        model_arch: str,
        model_cls: type[nn.Module] | str,
    ) -> None:
"""
        Register an external model to be used in vLLM.

        `model_cls` can be either:

        - A [`torch.nn.Module`][] class directly referencing the model.
        - A string in the format `<module>:<class>` which can be used to
          lazily import the model. This is useful to avoid initializing CUDA
          when importing the model and thus the related error
          `RuntimeError: Cannot re-initialize CUDA in forked subprocess`.
        """
        if not isinstance(model_arch, str):
            msg = f"`model_arch` should be a string, not a {type(model_arch)}"
            raise TypeError(msg)

        if model_arch in self.models:
            logger.warning(
                "Model architecture %s is already registered, and will be "
                "overwritten by the new model class %s.",
                model_arch,
                model_cls,
            )

        if isinstance(model_cls, str):
            split_str = model_cls.split(":")
            if len(split_str) != 2:
                msg = "Expected a string in the format `<module>:<class>`"
                raise ValueError(msg)

            model = _LazyRegisteredModel(*split_str)
        elif isinstance(model_cls, type) and issubclass(model_cls, nn.Module):
            model = _RegisteredModel.from_model_cls(model_cls)
        else:
            msg = (
                "`model_cls` should be a string or PyTorch model class, "
                f"not a {type(model_arch)}"
            )
            raise TypeError(msg)

        self.models[model_arch] = model

    def_raise_for_unsupported(self, architectures: list[str]):
        all_supported_archs = self.get_supported_archs()

        if any(arch in all_supported_archs for arch in architectures):
            raise ValueError(
                f"Model architectures {architectures} failed "
                "to be inspected. Please check the logs for more details."
            )

        for arch in architectures:
            if arch in _PREVIOUSLY_SUPPORTED_MODELS:
                previous_version = _PREVIOUSLY_SUPPORTED_MODELS[arch]

                raise ValueError(
                    f"Model architecture {arch} was supported in vLLM until "
                    f"v{previous_version}, and is not supported anymore. "
                    "Please use an older version of vLLM if you want to "
                    "use this model architecture."
                )
            if arch in _OOT_SUPPORTED_MODELS:
                plugin_url = _OOT_SUPPORTED_MODELS[arch]

                raise ValueError(
                    f"Model architecture {arch} is not supported in-tree anymore. "
                    f"Please install the plugin at {plugin_url} if you want to "
                    "use this model architecture."
                )

        raise ValueError(
            f"Model architectures {architectures} are not supported for now. "
            f"Supported architectures: {all_supported_archs}"
        )

    def_try_load_model_cls(self, model_arch: str) -> type[nn.Module] | None:
        if model_arch not in self.models:
            return None

        return _try_load_model_cls(model_arch, self.models[model_arch])

    def_try_inspect_model_cls(self, model_arch: str) -> _ModelInfo | None:
        if model_arch not in self.models:
            return None

        return _try_inspect_model_cls(model_arch, self.models[model_arch])

    def_try_resolve_transformers(
        self,
        architecture: str,
        model_config: ModelConfig,
    ) -> str | None:
        if architecture in _TRANSFORMERS_BACKEND_MODELS:
            return architecture

        auto_map: dict[str, str] = (
            getattr(model_config.hf_config, "auto_map", None) or dict()
        )

        # Make sure that config class is always initialized before model class,
        # otherwise the model class won't be able to access the config class,
        # the expected auto_map should have correct order like:
        # "auto_map": {
        #     "AutoConfig": "<your-repo-name>--<config-name>",
        #     "AutoModel": "<your-repo-name>--<config-name>",
        #     "AutoModelFor<Task>": "<your-repo-name>--<config-name>",
        # },
        for prefix in ("AutoConfig", "AutoModel"):
            for name, module in auto_map.items():
                if name.startswith(prefix):
                    try_get_class_from_dynamic_module(
                        module,
                        model_config.model,
                        revision=model_config.revision,
                        trust_remote_code=model_config.trust_remote_code,
                        warn_on_fail=False,
                    )

        model_module = getattr(transformers, architecture, None)

        if model_module is None:
            for name, module in auto_map.items():
                if name.startswith("AutoModel"):
                    model_module = try_get_class_from_dynamic_module(
                        module,
                        model_config.model,
                        revision=model_config.revision,
                        trust_remote_code=model_config.trust_remote_code,
                        warn_on_fail=True,
                    )
                    if model_module is not None:
                        break
            else:
                if model_config.model_impl != "transformers":
                    return None

                raise ValueError(
                    f"Cannot find model module. {architecture!r} is not a "
                    "registered model in the Transformers library (only "
                    "relevant if the model is meant to be in Transformers) "
                    "and 'AutoModel' is not present in the model config's "
                    "'auto_map' (relevant if the model is custom)."
                )

        if not model_module.is_backend_compatible():
            if model_config.model_impl != "transformers":
                return None

            raise ValueError(
                f"The Transformers implementation of {architecture!r} "
                "is not compatible with vLLM."
            )

        return model_config._get_transformers_backend_cls()

    def_normalize_arch(
        self,
        architecture: str,
        model_config: ModelConfig,
    ) -> str:
        if architecture in self.models:
            return architecture

        # This may be called in order to resolve runner_type and convert_type
        # in the first place, in which case we consider the default match
        match = try_match_architecture_defaults(
            architecture,
            runner_type=getattr(model_config, "runner_type", None),
            convert_type=getattr(model_config, "convert_type", None),
        )
        if match:
            suffix, _ = match

            # Get the name of the base model to convert
            for repl_suffix, _ in iter_architecture_defaults():
                base_arch = architecture.replace(suffix, repl_suffix)
                if base_arch in self.models:
                    return base_arch

        return architecture

    definspect_model_cls(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> tuple[_ModelInfo, str]:
        if isinstance(architectures, str):
            architectures = [architectures]
        if not architectures:
            raise ValueError("No model architectures are specified")

        # Require transformers impl
        if model_config.model_impl == "transformers":
            arch = self._try_resolve_transformers(architectures[0], model_config)
            if arch is not None:
                model_info = self._try_inspect_model_cls(arch)
                if model_info is not None:
                    return (model_info, arch)
        elif model_config.model_impl == "terratorch":
            model_info = self._try_inspect_model_cls("Terratorch")
            return (model_info, "Terratorch")

        # Fallback to transformers impl (after resolving convert_type)
        if (
            all(arch not in self.models for arch in architectures)
            and model_config.model_impl == "auto"
            and getattr(model_config, "convert_type", "none") == "none"
        ):
            arch = self._try_resolve_transformers(architectures[0], model_config)
            if arch is not None:
                model_info = self._try_inspect_model_cls(arch)
                if model_info is not None:
                    return (model_info, arch)

        for arch in architectures:
            normalized_arch = self._normalize_arch(arch, model_config)
            model_info = self._try_inspect_model_cls(normalized_arch)
            if model_info is not None:
                return (model_info, arch)

        # Fallback to transformers impl (before resolving runner_type)
        if (
            all(arch not in self.models for arch in architectures)
            and model_config.model_impl == "auto"
        ):
            arch = self._try_resolve_transformers(architectures[0], model_config)
            if arch is not None:
                model_info = self._try_inspect_model_cls(arch)
                if model_info is not None:
                    return (model_info, arch)

        return self._raise_for_unsupported(architectures)

    defresolve_model_cls(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> tuple[type[nn.Module], str]:
        if isinstance(architectures, str):
            architectures = [architectures]
        if not architectures:
            raise ValueError("No model architectures are specified")

        # Require transformers impl
        if model_config.model_impl == "transformers":
            arch = self._try_resolve_transformers(architectures[0], model_config)
            if arch is not None:
                model_cls = self._try_load_model_cls(arch)
                if model_cls is not None:
                    return (model_cls, arch)
        elif model_config.model_impl == "terratorch":
            arch = "Terratorch"
            model_cls = self._try_load_model_cls(arch)
            if model_cls is not None:
                return (model_cls, arch)

        # Fallback to transformers impl (after resolving convert_type)
        if (
            all(arch not in self.models for arch in architectures)
            and model_config.model_impl == "auto"
            and getattr(model_config, "convert_type", "none") == "none"
        ):
            arch = self._try_resolve_transformers(architectures[0], model_config)
            if arch is not None:
                model_cls = self._try_load_model_cls(arch)
                if model_cls is not None:
                    return (model_cls, arch)

        for arch in architectures:
            normalized_arch = self._normalize_arch(arch, model_config)
            model_cls = self._try_load_model_cls(normalized_arch)
            if model_cls is not None:
                return (model_cls, arch)

        # Fallback to transformers impl (before resolving runner_type)
        if (
            all(arch not in self.models for arch in architectures)
            and model_config.model_impl == "auto"
        ):
            arch = self._try_resolve_transformers(architectures[0], model_config)
            if arch is not None:
                model_cls = self._try_load_model_cls(arch)
                if model_cls is not None:
                    return (model_cls, arch)

        return self._raise_for_unsupported(architectures)

    defis_text_generation_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.is_text_generation_model

    defis_pooling_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.is_pooling_model

    defis_multimodal_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.supports_multimodal

    defis_multimodal_raw_input_only_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.supports_multimodal_raw_input_only

    defis_pp_supported_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.supports_pp

    defmodel_has_inner_state(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.has_inner_state

    defis_attention_free_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.is_attention_free

    defis_hybrid_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.is_hybrid

    defis_noops_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.has_noops

    defis_transcription_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.supports_transcription

    defis_transcription_only_model(
        self,
        architectures: str | list[str],
        model_config: ModelConfig,
    ) -> bool:
        model_cls, _ = self.inspect_model_cls(architectures, model_config)
        return model_cls.supports_transcription_only
```