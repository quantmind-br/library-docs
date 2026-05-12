---
title: model_executor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/
source: sitemap
fetched_at: 2026-05-07T21:23:12.639881896-03:00
rendered_js: false
word_count: 5
summary: This document defines the BasevLLMParameter class, a custom PyTorch parameter implementation designed to handle efficient weight loading and synchronization for linear layers in the vLLM framework.
tags:
    - vllm
    - pytorch
    - weight-loading
    - model-parallelism
    - tensor-management
category: reference
---

```
classBasevLLMParameter(Parameter):
"""
    Base parameter for vLLM linear layers. Extends the torch.nn.parameter
    by taking in a linear weight loader. Will copy the loaded weight
    into the parameter when the provided weight loader is called.
    """

    def__new__(cls, data: torch.Tensor | None, **kwargs):
        return super().__new__(cls, data=data, requires_grad=False)

    def__init__(self, data: torch.Tensor, weight_loader: Callable):
"""
        Initialize the BasevLLMParameter

        :param data: torch tensor with the parameter data
        :param weight_loader: weight loader callable

        :returns: a torch.nn.parameter
        """

        # During weight loading, we often do something like:
        # narrowed_tensor = param.data.narrow(0, offset, len)
        # narrowed_tensor.copy_(real_weight)
        # expecting narrowed_tensor and param.data to share the same storage.
        # However, on TPUs, narrowed_tensor will lazily propagate to the base
        # tensor, which is param.data, leading to the redundant memory usage.
        # This sometimes causes OOM errors during model loading. To avoid this,
        # we sync the param tensor after its weight loader is called.
        fromvllm.platformsimport current_platform

        if current_platform.use_sync_weight_loader():
            weight_loader = current_platform.make_synced_weight_loader(weight_loader)

        self._weight_loader = weight_loader
        self.tp_rank = get_tensor_model_parallel_rank()
        self.tp_size = get_tensor_model_parallel_world_size()

    @property
    defweight_loader(self) -> Callable:
        # NOTE(@ksayers) some models such as mamba_mixer2 override the
        # weight loader to support custom loading. In the future, model-specific
        # weight loading should be implemented via Model.load_weights. In the
        # meantime, support deleting and overriding `weight_loader` attribute
        if self._weight_loader is None:
            raise AttributeError(
                f"{self.__class__.__name__} weight_loader attribute has been deleted"
            )
        return self._weight_loader

    @weight_loader.setter
    defweight_loader(self, value: Callable):
        self._weight_loader = value

    @weight_loader.deleter
    defweight_loader(self):
        self._weight_loader = None  # type: ignore[assignment]

    def_is_1d_and_scalar(self, loaded_weight: torch.Tensor):
        cond1 = self.data.ndim == 1 and self.data.numel() == 1
        cond2 = loaded_weight.ndim == 0 and loaded_weight.numel() == 1
        return cond1 and cond2

    def_assert_and_load(self, loaded_weight: torch.Tensor):
        assert self.data.shape == loaded_weight.shape or self._is_1d_and_scalar(
            loaded_weight
        )
        self.data.copy_(loaded_weight)

    defload_column_parallel_weight(self, loaded_weight: torch.Tensor):
        self._assert_and_load(loaded_weight)

    defload_row_parallel_weight(self, loaded_weight: torch.Tensor):
        self._assert_and_load(loaded_weight)

    defload_merged_column_weight(self, loaded_weight: torch.Tensor, **kwargs):
        self._assert_and_load(loaded_weight)

    defload_qkv_weight(self, loaded_weight: torch.Tensor, **kwargs):
        self._assert_and_load(loaded_weight)

    def_shard_id_as_int(self, shard_id: str | int) -> int:
        if isinstance(shard_id, int):
            return shard_id

        # if not int, assume shard_id for qkv
        # map to int and return
        qkv_idxs = {"q": 0, "k": 1, "v": 2}
        assert isinstance(shard_id, str)
        assert shard_id in qkv_idxs
        return qkv_idxs[shard_id]

    @classmethod
    def__torch_function__(cls, func, types, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        return super().__torch_function__(func, types, args, kwargs)
```