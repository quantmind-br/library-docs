---
title: runai_streamer_loader - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/runai_streamer_loader/
source: sitemap
fetched_at: 2026-05-07T21:28:49.195315932-03:00
rendered_js: false
word_count: 30
summary: This document defines a model loader class that manages the retrieval and streaming of model weights from local and cloud storage systems.
tags:
    - model-loading
    - safetensors
    - cloud-storage
    - weight-streaming
    - machine-learning
category: api
---

```
classRunaiModelStreamerLoader(BaseModelLoader):
"""
    Model loader that can load safetensors
    files from local FS, S3, GCS, or Azure Blob Storage.
    """

    def__init__(self, load_config: LoadConfig):
        super().__init__(load_config)

        self._is_distributed: bool = False
        if load_config.model_loader_extra_config:
            extra_config = load_config.model_loader_extra_config

            if isinstance(distributed := extra_config.get("distributed"), bool):
                self._is_distributed = distributed
            if isinstance(concurrency := extra_config.get("concurrency"), int):
                os.environ["RUNAI_STREAMER_CONCURRENCY"] = str(concurrency)
            if isinstance(memory_limit := extra_config.get("memory_limit"), int):
                os.environ["RUNAI_STREAMER_MEMORY_LIMIT"] = str(memory_limit)

            runai_streamer_s3_endpoint = os.getenv("RUNAI_STREAMER_S3_ENDPOINT")
            aws_endpoint_url = os.getenv("AWS_ENDPOINT_URL")
            if runai_streamer_s3_endpoint is None and aws_endpoint_url is not None:
                os.environ["RUNAI_STREAMER_S3_ENDPOINT"] = aws_endpoint_url

    def_prepare_weights(
        self, model_name_or_path: str, revision: str | None
    ) -> list[str]:
"""Prepare weights for the model.

        If the model is not local, it will be downloaded."""

        is_object_storage_path = is_runai_obj_uri(model_name_or_path)
        is_local = os.path.isdir(model_name_or_path)
        safetensors_pattern = "*.safetensors"
        index_file = SAFE_WEIGHTS_INDEX_NAME

        hf_folder = (
            model_name_or_path
            if (is_local or is_object_storage_path)
            else download_weights_from_hf(
                model_name_or_path,
                self.load_config.download_dir,
                [safetensors_pattern],
                revision,
                ignore_patterns=self.load_config.ignore_patterns,
            )
        )
        hf_weights_files = list_safetensors(path=hf_folder)

        if not is_local and not is_object_storage_path:
            download_safetensors_index_file_from_hf(
                model_name_or_path, index_file, self.load_config.download_dir, revision
            )

        if not hf_weights_files:
            raise RuntimeError(
                f"Cannot find any safetensors model weights with `{model_name_or_path}`"
            )

        return hf_weights_files

    def_get_weights_iterator(
        self, model_or_path: str, revision: str | None
    ) -> Generator[tuple[str, torch.Tensor], None, None]:
"""Get an iterator for the model weights based on the load format."""
        hf_weights_files = self._prepare_weights(model_or_path, revision)
        return runai_safetensors_weights_iterator(
            hf_weights_files, self.load_config.use_tqdm_on_load, self._is_distributed
        )

    defdownload_model(self, model_config: ModelConfig) -> None:
"""Download model if necessary"""
        self._prepare_weights(model_config.model, model_config.revision)

    defload_weights(self, model: nn.Module, model_config: ModelConfig) -> None:
"""Load weights into a model."""
        model_weights = model_config.model
        if model_weights_override := model_config.model_weights:
            model_weights = model_weights_override
        model.load_weights(
            self._get_weights_iterator(model_weights, model_config.revision)
        )
```