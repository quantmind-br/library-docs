---
title: parameter - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/parameter/
source: sitemap
fetched_at: 2026-05-07T21:33:55.972403801-03:00
rendered_js: false
word_count: 639
summary: This document defines the base classes for handling model layer weights and quantization parameters in vLLM, providing structures for weight loading, tensor parallelism, and memory management during model initialization.
tags:
    - vllm
    - model-loading
    - tensor-parallelism
    - weight-quantization
    - torch-nn-parameter
    - memory-management
category: reference
---

## BasevLLMParameter [¶](#vllm.model_executor.parameter.BasevLLMParameter "Permanent link")

Bases: `Parameter`

Base parameter for vLLM linear layers. Extends the torch.nn.parameter by taking in a linear weight loader. Will copy the loaded weight into the parameter when the provided weight loader is called.

Source code in `vllm/model_executor/parameter.py`

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

### \_\_init\__ [¶](#vllm.model_executor.parameter.BasevLLMParameter.__init__ "Permanent link")

Initialize the BasevLLMParameter

:param data: torch tensor with the parameter data :param weight\_loader: weight loader callable

:returns: a torch.nn.parameter

Source code in `vllm/model_executor/parameter.py`

```
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
```

## BlockQuantScaleParameter [¶](#vllm.model_executor.parameter.BlockQuantScaleParameter "Permanent link")

Bases: `_ColumnvLLMParameter`, `RowvLLMParameter`

Parameter class for weight scales loaded for weights with block-wise quantization. Uses both column and row parallelism.

Source code in `vllm/model_executor/parameter.py`

```
classBlockQuantScaleParameter(_ColumnvLLMParameter, RowvLLMParameter):
"""
    Parameter class for weight scales loaded for weights with
    block-wise quantization. Uses both column and row parallelism.
    """

    pass
```

## ChannelQuantScaleParameter [¶](#vllm.model_executor.parameter.ChannelQuantScaleParameter "Permanent link")

Bases: `_ColumnvLLMParameter`

Parameter class for weight scales loaded for weights with channel-wise quantization. Equivalent to \_ColumnvLLMParameter.

Source code in `vllm/model_executor/parameter.py`

```
classChannelQuantScaleParameter(_ColumnvLLMParameter):
"""
    Parameter class for weight scales loaded for weights with
    channel-wise quantization. Equivalent to _ColumnvLLMParameter.
    """

    pass
```

## GroupQuantScaleParameter [¶](#vllm.model_executor.parameter.GroupQuantScaleParameter "Permanent link")

Bases: `_ColumnvLLMParameter`, `RowvLLMParameter`

Parameter class for weight scales loaded for weights with grouped quantization. Uses both column and row parallelism.

Source code in `vllm/model_executor/parameter.py`

```
classGroupQuantScaleParameter(_ColumnvLLMParameter, RowvLLMParameter):
"""
    Parameter class for weight scales loaded for weights with
    grouped quantization. Uses both column and row parallelism.
    """

    pass
```

## ModelWeightParameter [¶](#vllm.model_executor.parameter.ModelWeightParameter "Permanent link")

Bases: `_ColumnvLLMParameter`, `RowvLLMParameter`

Parameter class for linear layer weights. Uses both column and row parallelism.

Source code in `vllm/model_executor/parameter.py`

```
classModelWeightParameter(_ColumnvLLMParameter, RowvLLMParameter):
"""
    Parameter class for linear layer weights. Uses both column and
    row parallelism.
    """

    pass
```

## PackedColumnParameter [¶](#vllm.model_executor.parameter.PackedColumnParameter "Permanent link")

Bases: `_ColumnvLLMParameter`

Parameter for model parameters which are packed on disk and support column parallelism only. See PackedvLLMParameter for more details on the packed properties.

Source code in `vllm/model_executor/parameter.py`

```
classPackedColumnParameter(_ColumnvLLMParameter):
"""
    Parameter for model parameters which are packed on disk
    and support column parallelism only. See PackedvLLMParameter
    for more details on the packed properties.
    """

    def__init__(
        self,
        packed_factor: int | Fraction,
        packed_dim: int,
        marlin_tile_size: int | None = None,
        **kwargs,
    ):
        self._packed_factor = packed_factor
        self._packed_dim = packed_dim
        self._marlin_tile_size = marlin_tile_size
        super().__init__(**kwargs)

    @property
    defpacked_dim(self):
        return self._packed_dim

    @property
    defpacked_factor(self):
        return self._packed_factor

    @property
    defmarlin_tile_size(self):
        return self._marlin_tile_size

    defadjust_shard_indexes_for_packing(self, shard_size, shard_offset):
        return _adjust_shard_indexes_for_packing(
            shard_size=shard_size,
            shard_offset=shard_offset,
            packed_factor=self.packed_factor,
            marlin_tile_size=self.marlin_tile_size,
        )
```

## PackedvLLMParameter [¶](#vllm.model_executor.parameter.PackedvLLMParameter "Permanent link")

Bases: `ModelWeightParameter`

Parameter for model weights which are packed on disk. Example: GPTQ Marlin weights are int4 or int8, packed into int32. Extends the ModelWeightParameter to take in the packed factor, the packed dimension, and optionally, marlin tile size for marlin kernels. Adjusts the shard\_size and shard\_offset for fused linear layers model weight loading by accounting for packing and optionally, marlin tile size.

Source code in `vllm/model_executor/parameter.py`

```
classPackedvLLMParameter(ModelWeightParameter):
"""
    Parameter for model weights which are packed on disk.
    Example: GPTQ Marlin weights are int4 or int8, packed into int32.
    Extends the ModelWeightParameter to take in the
    packed factor, the packed dimension, and optionally, marlin
    tile size for marlin kernels. Adjusts the shard_size and
    shard_offset for fused linear layers model weight loading
    by accounting for packing and optionally, marlin tile size.
    """

    def__init__(
        self,
        packed_factor: int | Fraction,
        packed_dim: int,
        marlin_tile_size: int | None = None,
        **kwargs,
    ):
        self._packed_factor = packed_factor
        self._packed_dim = packed_dim
        self._marlin_tile_size = marlin_tile_size
        super().__init__(**kwargs)

    @property
    defpacked_dim(self):
        return self._packed_dim

    @property
    defpacked_factor(self):
        return self._packed_factor

    @property
    defmarlin_tile_size(self):
        return self._marlin_tile_size

    defadjust_shard_indexes_for_packing(self, shard_size, shard_offset):
        return _adjust_shard_indexes_for_packing(
            shard_size=shard_size,
            shard_offset=shard_offset,
            packed_factor=self.packed_factor,
            marlin_tile_size=self.marlin_tile_size,
        )
```

## PerTensorScaleParameter [¶](#vllm.model_executor.parameter.PerTensorScaleParameter "Permanent link")

Bases: `BasevLLMParameter`

Parameter class for scales where the number of scales is equivalent to the number of logical matrices in fused linear layers (e.g. for QKV, there are 3 scales loaded from disk). This is relevant to weights with per-tensor quantization. Adds functionality to map the scalers to a shard during weight loading.

Note: additional parameter manipulation may be handled for each quantization config specifically, within process\_weights\_after\_loading

Source code in `vllm/model_executor/parameter.py`

```
classPerTensorScaleParameter(BasevLLMParameter):
"""
    Parameter class for scales where the number of scales is
    equivalent to the number of logical matrices in fused linear
    layers (e.g. for QKV, there are 3 scales loaded from disk).
    This is relevant to weights with per-tensor quantization.
    Adds functionality to map the scalers to a shard during
    weight loading.

    Note: additional parameter manipulation may be handled
    for each quantization config specifically, within
    process_weights_after_loading
    """

    def__init__(self, **kwargs):
        super().__init__(**kwargs)

    # For row parallel layers, no sharding needed
    # load weight into parameter as is
    defload_row_parallel_weight(self, *args, **kwargs):
        super().load_row_parallel_weight(*args, **kwargs)

    defload_merged_column_weight(self, *args, **kwargs):
        self._load_into_shard_id(*args, **kwargs)

    defload_qkv_weight(self, *args, **kwargs):
        self._load_into_shard_id(*args, **kwargs)

    defload_column_parallel_weight(self, *args, **kwargs):
        super().load_row_parallel_weight(*args, **kwargs)

    def_load_into_shard_id(
        self, loaded_weight: torch.Tensor, shard_id: str | int, **kwargs
    ):
"""
        Slice the parameter data based on the shard id for
        loading.
        """

        param_data = self.data
        shard_id = self._shard_id_as_int(shard_id)

        # AutoFP8 scales do not have a shape
        # compressed-tensors scales do have a shape
        if len(loaded_weight.shape) != 0:
            assert loaded_weight.shape[0] == 1
            loaded_weight = loaded_weight[0]

        param_data = param_data[shard_id]
        assert param_data.shape == loaded_weight.shape
        param_data.copy_(loaded_weight)
```

### \_load\_into\_shard\_id [¶](#vllm.model_executor.parameter.PerTensorScaleParameter._load_into_shard_id "Permanent link")

```
_load_into_shard_id(
    loaded_weight: Tensor, shard_id: str | int, **kwargs
)
```

Slice the parameter data based on the shard id for loading.

Source code in `vllm/model_executor/parameter.py`

```
def_load_into_shard_id(
    self, loaded_weight: torch.Tensor, shard_id: str | int, **kwargs
):
"""
    Slice the parameter data based on the shard id for
    loading.
    """

    param_data = self.data
    shard_id = self._shard_id_as_int(shard_id)

    # AutoFP8 scales do not have a shape
    # compressed-tensors scales do have a shape
    if len(loaded_weight.shape) != 0:
        assert loaded_weight.shape[0] == 1
        loaded_weight = loaded_weight[0]

    param_data = param_data[shard_id]
    assert param_data.shape == loaded_weight.shape
    param_data.copy_(loaded_weight)
```

## RowvLLMParameter [¶](#vllm.model_executor.parameter.RowvLLMParameter "Permanent link")

Bases: `BasevLLMParameter`

Parameter class defining weight\_loading functionality (load\_row\_parallel\_weight) for parameters being loaded into linear layers with row parallel functionality. Requires an input\_dim to be defined.

Source code in `vllm/model_executor/parameter.py`

```
classRowvLLMParameter(BasevLLMParameter):
"""
    Parameter class defining weight_loading functionality
    (load_row_parallel_weight) for parameters being loaded
    into linear layers with row parallel functionality.
    Requires an input_dim to be defined.
    """

    def__init__(self, input_dim: int, **kwargs):
        self._input_dim = input_dim
        super().__init__(**kwargs)

    @property
    definput_dim(self):
        return self._input_dim

    defload_row_parallel_weight(self, loaded_weight: torch.Tensor):
        shard_size = self.data.shape[self.input_dim]
        loaded_weight = loaded_weight.narrow(
            self.input_dim, self.tp_rank * shard_size, shard_size
        )

        if len(loaded_weight.shape) == 0:
            loaded_weight = loaded_weight.reshape(1)

        assert self.data.shape == loaded_weight.shape
        self.data.copy_(loaded_weight)
```

Bases: `BasevLLMParameter`

Parameter for weights with many shared tensors across a model

For example, when applying transforms to the "gate" and "up" partitions of `MergedColumnParallelLinear`, the transform weights must stay separate tensors in order to allow for tensor memory sharing between layers.

Source code in `vllm/model_executor/parameter.py`

```
classSharedWeightParameter(BasevLLMParameter):
"""
    Parameter for weights with many shared tensors across a model

    For example, when applying transforms to the "gate" and "up" partitions of
    `MergedColumnParallelLinear`, the transform weights must stay separate
    tensors in order to allow for tensor memory sharing between layers.
    """

    # global registry for sharing tensors based on passed `data_key`
    # this dict holds weaksrefs to avoid memory leak after model cleanup
    tensors_registry: WeakValueDictionary = WeakValueDictionary()

    # local container for strong references to shared tensors
    # this set compensates for the fact that torch.nn.Parameter
    # and Parameter subclasses do not hold reliable references to tensors
    local_tensors: set[torch.Tensor]

    # dictionary mapping partition indices to associated parameters
    partitions: dict[int, ModelWeightParameter | Parameter]

    def__new__(cls, **kwargs):
        return super().__new__(cls, data=None, **kwargs)

    def__init__(self, input_dim: int = 1, output_dim: int = 0, **kwargs):
        weight_loader: Callable = kwargs.get("weight_loader")  # type: ignore[assignment]
        super().__init__(data=None, weight_loader=weight_loader)

        self.local_tensors = set()
        self.partitions = {}
        self.kwargs = {
            "input_dim": input_dim,
            "output_dim": output_dim,
            "weight_loader": self._fake_weight_loader,
        }

        if self.tp_size > 1:
            raise NotImplementedError(
                f"{self.__class__.__name__} does not "
                "currently support tensor parallelism"
            )

    defadd_partition(self, index: int, data_key: Hashable, *args, **kwargs):
"""
        Add a partition to the weight parameter. Partitions whose `data_key`
        is the same will share tensor data

        :param index: index of partition to add
        :param data_key: hashable key used to key shared tensors
        :param *args: arguments for `torch.empty`
        :param **kwargs: keyword arguments for `torch.empty`
        """
        # load (shared) tensor using `data_key`
        if data_key not in self.tensors_registry:
            data = torch.empty(*args, **kwargs)
            self.tensors_registry[data_key] = data
        else:
            data = self.tensors_registry[data_key]

        # create associated model parameter
        self.partitions[index] = ModelWeightParameter(data=data, **self.kwargs)  # type: ignore[arg-type]

        # hold local reference, since ModelWeightParameter does not
        # see https://github.com/pytorch/pytorch/issues/75932
        self.local_tensors.add(data)

    defload_column_parallel_weight(self, loaded_weight: torch.Tensor):
        assert len(self.partitions) == 1 and 0 in self.partitions
        partition = self.partitions[0]

        ModelWeightParameter.load_column_parallel_weight(partition, loaded_weight)

    defload_row_parallel_weight(self, loaded_weight: torch.Tensor):
        assert len(self.partitions) == 1 and 0 in self.partitions
        partition = self.partitions[0]

        ModelWeightParameter.load_row_parallel_weight(partition, loaded_weight)

    defload_merged_column_weight(self, loaded_weight: torch.Tensor, **kwargs):
        partition_id = kwargs.pop("shard_id")
        partition_id = self._shard_id_as_int(partition_id)
        partition = self.partitions[partition_id]

        input_dim = self.kwargs.get("input_dim")
        shard_size = partition.data.size(input_dim) // self.tp_size
        shard_offset = self.tp_rank * shard_size

        ModelWeightParameter.load_merged_column_weight(
            partition, loaded_weight, shard_offset=shard_offset, shard_size=shard_size
        )

    defload_qkv_weight(self, loaded_weight: torch.Tensor, **kwargs):
        partition_id = self._shard_id_as_int(kwargs.pop("shard_id"))
        partition = self.partitions[partition_id]

        input_dim = self.kwargs.get("input_dim")
        shard_size = partition.data.size(input_dim) // self.tp_size
        shard_offset = self.tp_rank * shard_size
        shard_id = "q"  # fake first partition
        num_heads = kwargs.get("num_heads")

        ModelWeightParameter.load_qkv_weight(
            partition,
            loaded_weight,
            shard_offset=shard_offset,
            shard_size=shard_size,
            shard_id=shard_id,
            num_heads=num_heads,
        )

    defprocess_weights_after_loading(self):
        for key in self.partitions:
            self.partitions[key] = torch.nn.Parameter(
                data=self.partitions[key].data, requires_grad=False
            )

    @property
    defdata(self):
        raise ValueError(
            "Accessing `data` of a `SharedWeightParameter` is not allowed. "
            "Instead, use `get_partition` to get the weight of "
            "the particular partition you want to access"
        )

    def_fake_weight_loader(
        self,
        param: BasevLLMParameter,
        loaded_weight: torch.Tensor,
        loaded_weight_shard_id: str | int | None,
    ):
        raise ValueError(
            "When loading partition weights of "
            f"{self.__class__.__name__}, use methods provided by "
            f"{self.__class__.__name__}, not partition loader"
        )
```

### add\_partition [¶](#vllm.model_executor.parameter.SharedWeightParameter.add_partition "Permanent link")

```
add_partition(
    index: int, data_key: Hashable, *args, **kwargs
)
```

Add a partition to the weight parameter. Partitions whose `data_key` is the same will share tensor data

:param index: index of partition to add :param data\_key: hashable key used to key shared tensors :param *args: arguments for `torch.empty` :param* \*kwargs: keyword arguments for `torch.empty`

Source code in `vllm/model_executor/parameter.py`

```
defadd_partition(self, index: int, data_key: Hashable, *args, **kwargs):
"""
    Add a partition to the weight parameter. Partitions whose `data_key`
    is the same will share tensor data

    :param index: index of partition to add
    :param data_key: hashable key used to key shared tensors
    :param *args: arguments for `torch.empty`
    :param **kwargs: keyword arguments for `torch.empty`
    """
    # load (shared) tensor using `data_key`
    if data_key not in self.tensors_registry:
        data = torch.empty(*args, **kwargs)
        self.tensors_registry[data_key] = data
    else:
        data = self.tensors_registry[data_key]

    # create associated model parameter
    self.partitions[index] = ModelWeightParameter(data=data, **self.kwargs)  # type: ignore[arg-type]

    # hold local reference, since ModelWeightParameter does not
    # see https://github.com/pytorch/pytorch/issues/75932
    self.local_tensors.add(data)
```

## \_ColumnvLLMParameter [¶](#vllm.model_executor.parameter._ColumnvLLMParameter "Permanent link")

Bases: `BasevLLMParameter`

Private class defining weight loading functionality (load\_merged\_column\_weight, load\_qkv\_weight) for parameters being loaded into linear layers with column parallelism. This includes QKV and MLP layers which are not already fused on disk. Requires an output dimension to be defined. Called within the weight loader of each of the column parallel linear layers.

Source code in `vllm/model_executor/parameter.py`

```
class_ColumnvLLMParameter(BasevLLMParameter):
"""
    Private class defining weight loading functionality
    (load_merged_column_weight, load_qkv_weight)
    for parameters being loaded into linear layers with column
    parallelism. This includes QKV and MLP layers which are
    not already fused on disk. Requires an output dimension
    to be defined. Called within the weight loader of
    each of the column parallel linear layers.
    """

    def__init__(self, output_dim: int, **kwargs):
        self._output_dim = output_dim
        super().__init__(**kwargs)

    @property
    defoutput_dim(self):
        return self._output_dim

    defload_column_parallel_weight(self, loaded_weight: torch.Tensor):
        shard_size = self.data.shape[self.output_dim]
        loaded_weight = loaded_weight.narrow(
            self.output_dim, self.tp_rank * shard_size, shard_size
        )
        assert self.data.shape == loaded_weight.shape
        self.data.copy_(loaded_weight)

    defload_merged_column_weight(self, loaded_weight: torch.Tensor, **kwargs):
        shard_offset: int = kwargs["shard_offset"]
        shard_size: int = kwargs["shard_size"]

        # TODO: move these to PackedColumnParameter and PackedvLLMParameter
        if (
            isinstance(self, (PackedColumnParameter, PackedvLLMParameter))
            and self.packed_dim == self.output_dim
        ):
            shard_size, shard_offset = self.adjust_shard_indexes_for_packing(
                shard_offset=shard_offset, shard_size=shard_size
            )

        param_data = self.data

        param_data = param_data.narrow(self.output_dim, shard_offset, shard_size)
        loaded_weight = loaded_weight.narrow(
            self.output_dim, self.tp_rank * shard_size, shard_size
        )
        assert param_data.shape == loaded_weight.shape
        param_data.copy_(loaded_weight)

    defload_qkv_weight(self, loaded_weight: torch.Tensor, **kwargs):
        shard_offset: int = kwargs["shard_offset"]
        shard_size: int = kwargs["shard_size"]
        shard_id: str = kwargs["shard_id"]
        num_heads: int = kwargs["num_heads"]

        # TODO: move these to PackedColumnParameter and PackedvLLMParameter
        if (
            isinstance(self, (PackedColumnParameter, PackedvLLMParameter))
            and self.output_dim == self.packed_dim
        ):
            shard_size, shard_offset = self.adjust_shard_indexes_for_packing(
                shard_offset=shard_offset, shard_size=shard_size
            )

        param_data = self.data
        shard_id_int = self.tp_rank if shard_id == "q" else self.tp_rank // num_heads
        param_data = param_data.narrow(self.output_dim, shard_offset, shard_size)
        loaded_weight = loaded_weight.narrow(
            self.output_dim, shard_id_int * shard_size, shard_size
        )

        assert param_data.shape == loaded_weight.shape
        param_data.copy_(loaded_weight)
```

## permute\_param\_layout_ [¶](#vllm.model_executor.parameter.permute_param_layout_ "Permanent link")

```
permute_param_layout_(
    param: BasevLLMParameter,
    input_dim: int,
    output_dim: int,
    **kwargs,
) -> BasevLLMParameter
```

Permute a parameter's layout to the specified input and output dimensions, useful for forcing the parameter into a known layout, for example, if I need a packed (quantized) weight matrix to be in the layout {input\_dim = 0, output\_dim = 1, packed\_dim = 0} then I can call: permute\_param\_layout\_(x, input\_dim=0, output\_dim=1, packed\_dim=0) to ensure x is in the correct layout (permuting it to the correct layout if required, asserting if it cannot get it to the correct layout)

Source code in `vllm/model_executor/parameter.py`

```
defpermute_param_layout_(
    param: BasevLLMParameter, input_dim: int, output_dim: int, **kwargs
) -> BasevLLMParameter:
"""
    Permute a parameter's layout to the specified input and output dimensions,
    useful for forcing the parameter into a known layout, for example, if I need
    a packed (quantized) weight matrix to be in the layout
        {input_dim = 0, output_dim = 1, packed_dim = 0}
    then I can call:
        permute_param_layout_(x, input_dim=0, output_dim=1, packed_dim=0)
    to ensure x is in the correct layout (permuting it to the correct layout if
    required, asserting if it cannot get it to the correct layout)
    """

    curr_input_dim = getattr(param, "input_dim", None)
    curr_output_dim = getattr(param, "output_dim", None)

    if curr_input_dim is None or curr_output_dim is None:
        assert param.data.dim() == 2, (
            "permute_param_layout_ only supports 2D parameters when either "
            "input_dim or output_dim is not set"
        )

    # if one of the dimensions is not set, set it to the opposite of the other
    #  we can only do this since we asserted the parameter is 2D above
    if curr_input_dim is None:
        assert curr_output_dim is not None, "either input or output dim must be set"
        curr_input_dim = (curr_output_dim + 1) % 2
    if curr_output_dim is None:
        assert curr_input_dim is not None, "either input or output dim must be set"
        curr_output_dim = (curr_input_dim + 1) % 2

    # create permutation from the current layout to the layout with
    # self.input_dim at input_dim and self.output_dim at output_dim preserving
    # other dimensions
    perm = [
        i for i in range(param.data.dim()) if i not in [curr_input_dim, curr_output_dim]
    ]
    perm.insert(input_dim, curr_input_dim)
    perm.insert(output_dim, curr_output_dim)

    if "packed_dim" in kwargs:
        assert (
            hasattr(param, "packed_dim")
            and param.packed_dim == perm[kwargs["packed_dim"]]
        ), "permute_param_layout_ currently doesn't support repacking"

    param.data = param.data.permute(*perm)
    if hasattr(param, "_input_dim"):
        param._input_dim = input_dim
    if hasattr(param, "_output_dim"):
        param._output_dim = output_dim
    if "packed_dim" in kwargs and hasattr(param, "_packed_dim"):
        param._packed_dim = kwargs["packed_dim"]

    return param
```