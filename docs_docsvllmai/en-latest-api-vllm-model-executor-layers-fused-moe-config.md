---
title: config - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/config/
source: sitemap
fetched_at: 2026-05-07T21:24:32.591248668-03:00
rendered_js: false
word_count: 1454
summary: Defines the parallel configuration parameters and logic for Mixture-of-Experts (MoE) layers, managing tensor, data, and expert parallelism settings within the vLLM framework.
tags:
    - moe
    - parallelism
    - vllm
    - expert-parallelism
    - tensor-parallelism
    - distributed-computing
category: api
---

## FusedMoEParallelConfig `dataclass` [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig "Permanent link")

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
@dataclass
classFusedMoEParallelConfig:
    tp_size: int
    pcp_size: int
    dp_size: int
    ep_size: int
    tp_rank: int
    pcp_rank: int
    dp_rank: int
    ep_rank: int
    sp_size: int

    use_ep: bool  # whether to use EP or not
    all2all_backend: str  # all2all backend for MoE communication
    enable_eplb: bool  # whether to enable expert load balancing

    @property
    defis_sequence_parallel(self) -> bool:
        return self.sp_size > 1

    @property
    defuse_all2all_kernels(self):
        return self.dp_size > 1 and self.use_ep

    @property
    defuse_deepep_ht_kernels(self):
        return (
            self.use_all2all_kernels
            and self.all2all_backend == "deepep_high_throughput"
        )

    @property
    defuse_deepep_ll_kernels(self):
        return self.use_all2all_kernels and self.all2all_backend == "deepep_low_latency"

    @property
    defuse_fi_nvl_two_sided_kernels(self):
        return self.use_all2all_kernels and (
            self.all2all_backend == "flashinfer_all2allv"
            or self.all2all_backend == "flashinfer_nvlink_two_sided"
        )

    @property
    defuse_fi_nvl_one_sided_kernels(self):
        return (
            self.use_all2all_kernels
            and self.all2all_backend == "flashinfer_nvlink_one_sided"
        )

    @property
    defuse_batched_activation_format(self):
        return self.use_deepep_ll_kernels or self.use_nixl_ep_kernels

    @property
    defneeds_round_robin_routing_tables(self):
        return self.use_deepep_ll_kernels or self.use_nixl_ep_kernels

    @property
    defuse_ag_rs_all2all_kernels(self):
        return (
            self.use_all2all_kernels
            and self.all2all_backend == "allgather_reducescatter"
        )

    @property
    defuse_mori_kernels(self):
        return self.use_all2all_kernels and self.all2all_backend == "mori"

    @property
    defuse_nixl_ep_kernels(self):
        return self.use_all2all_kernels and self.all2all_backend == "nixl_ep"

    @staticmethod
    defflatten_tp_across_dp_and_pcp(
        tp_size: int, dp_size: int, dp_rank: int, pcp_size: int, pcp_rank: int
    ) -> tuple[int, int]:
        tp_rank = 0 if tp_size == 1 else get_tensor_model_parallel_rank()
        # There are actually dp_size * pcp_size * tp_size devices.
        # Update tp_size and tp_rank so we shard across all devices.
        flatten_tp_size = dp_size * pcp_size * tp_size
        flatten_tp_rank = dp_rank * pcp_size * tp_size + pcp_rank * tp_size + tp_rank
        return flatten_tp_size, flatten_tp_rank

    @staticmethod
    defmake(
        tp_size_: int,
        pcp_size_: int,
        dp_size_: int,
        sp_size_: int,
        vllm_parallel_config: ParallelConfig,
    ) -> "FusedMoEParallelConfig":
"""
        Determine MoE parallel configuration. Based on the input `tp_size_`,
        `dp_size_` and vllm's parallel config, determine what
        level's of parallelism to use in the fused moe layer.

        Args:
            tp_size_ (int): `tp_size` passed into the FusedMoE constructor.
            pcp_size_ (int): `pcp_size` passed into the FusedMoE constructor.
            dp_size_ (int): `dp_size` passed into the FusedMoE constructor.
            vllm_parallel_config (ParallelConfig): vLLM's parallel config
                object which contains the `enable_expert_parallel` flag.

        Examples:
            When there is no parallelism requested,
            i.e. `tp_size_` = `pcp_size_` = `dp_size_` = 1, we simply return the sizes
            unaltered and the ranks set to 0.

            Expert Parallelism is considered only when either `dp_size_`, `pcp_size_` or
            `tp_size_` is non trivial.

            Note that PCP serves the same function as DP here.

            When TP = 2, DP(PCP) = 1 and EP = False, the configuration on different
            devices:

            - device 0 : TP = {2, 0} DP = {1, 0} EP = {1, 0} //
                legend : {size, rank}
            - device 1 : TP = {2, 1} DP = {1, 0} EP = {1, 0}
            - Comment : Tensors are sharded across 2 devices.

            When TP = 1, DP(PCP) = 2 and EP = False, the configuration on different
                devices:

            - device 0 : TP = {2, 0} DP = {2, 0} EP = {1, 0}
            - device 1 : TP = {2, 1} DP = {2, 1} EP = {1, 0}
            - Comment: There are 2 engine instances and the tensors are sharded
                across 2 decvices.

            When TP = 2, DP(PCP) = 2 and EP = False, the configuration on different
                devices:

            - device 0: TP = {4, 0} DP = {2, 0} EP = {1, 0}
            - device 1: TP = {4, 1} DP = {2, 0} EP = {1, 0}
            - device 2: TP = {4, 2} DP = {2, 1} EP = {1, 0}
            - device 3: TP = {4, 3} DP = {2, 1} EP = {1, 0}
            - Comment: There are 2 engine instances and the tensors are sharded
                across 4 devices.

            When, TP = 2, DP(PCP) = 1 and EP = True, the configuration on different
                devices:

            - device 0: TP = {1, 0} DP = {1, 0} EP = {2, 0}
            - device 1: TP = {1, 0} DP = {1, 0} EP = {2, 1}
            - Comment: The experts are split between the 2 devices.

            When, TP = 1, DP(PCP) = 2 and EP = True, the configuration on different
                devices:

            - device 0: TP = {1, 0} DP = {2, 0} EP = {2, 0}
            - device 1: TP = {1, 0} DP = {2, 1} EP = {2, 1}
            - Comment: There are 2 engine instances and the experts are split
                between the 2 devices.

            When TP = 2, DP(PCP) = 2 and EP = True, the configuration on different
                devices:

            - device 0: TP = {1, 0} DP = {2, 0} EP = {4, 0}
            - device 1: TP = {1, 0} DP = {2, 0} EP = {4, 1}
            - device 2: TP = {1, 0} DP = {2, 1} EP = {4, 2}
            - device 3: TP = {1, 0} DP = {2, 1} EP = {4, 3}
            - Comment: There are 2 engine instances and the experts are split
                between the 4 devices.
        """
        use_ep = (
            dp_size_ * pcp_size_ * tp_size_ > 1
            and vllm_parallel_config.enable_expert_parallel
        )

        dp_size = dp_size_
        dp_rank = get_dp_group().rank_in_group if dp_size > 1 else 0
        pcp_size = pcp_size_
        pcp_rank = get_pcp_group().rank_in_group if pcp_size > 1 else 0
        tp_size, tp_rank = FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp(
            tp_size_, dp_size_, dp_rank, pcp_size_, pcp_rank
        )

        if not use_ep:
            return FusedMoEParallelConfig(
                tp_size=tp_size,
                tp_rank=tp_rank,
                pcp_size=pcp_size,
                pcp_rank=pcp_rank,
                dp_size=dp_size,
                dp_rank=dp_rank,
                ep_size=1,
                ep_rank=0,
                sp_size=sp_size_,
                use_ep=False,
                all2all_backend=vllm_parallel_config.all2all_backend,
                enable_eplb=vllm_parallel_config.enable_eplb,
            )
        # DP + EP / TP + EP / DP + TP + EP
        assert use_ep
        # In EP, each device owns a set of experts fully. There is no tensor
        # parallel update tp_size, tp_rank, ep_size and ep_rank to reflect that.
        ep_size = tp_size
        ep_rank = tp_rank
        return FusedMoEParallelConfig(
            tp_size=1,
            tp_rank=0,
            pcp_size=pcp_size,
            pcp_rank=pcp_rank,
            dp_size=dp_size,
            dp_rank=dp_rank,
            ep_size=ep_size,
            ep_rank=ep_rank,
            sp_size=sp_size_,
            use_ep=True,
            all2all_backend=vllm_parallel_config.all2all_backend,
            enable_eplb=vllm_parallel_config.enable_eplb,
        )

    @classmethod
    defmake_no_parallel(cls) -> "FusedMoEParallelConfig":
"""For usage in CI/CD and testing."""
        return FusedMoEParallelConfig(
            tp_size=1,
            tp_rank=0,
            pcp_size=1,
            pcp_rank=0,
            dp_size=1,
            dp_rank=0,
            ep_size=1,
            ep_rank=0,
            sp_size=1,
            use_ep=False,
            all2all_backend="allgather_reducescatter",
            enable_eplb=False,
        )
```

### make `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make "Permanent link")

Determine MoE parallel configuration. Based on the input `tp_size_`, `dp_size_` and vllm's parallel config, determine what level's of parallelism to use in the fused moe layer.

Parameters:

Name Type Description Default `tp_size_` `int`

`tp_size` passed into the FusedMoE constructor.

*required* `pcp_size_` `int`

`pcp_size` passed into the FusedMoE constructor.

*required* `dp_size_` `int`

`dp_size` passed into the FusedMoE constructor.

*required* `vllm_parallel_config` `ParallelConfig`

vLLM's parallel config object which contains the `enable_expert_parallel` flag.

*required*

Examples:

When there is no parallelism requested, i.e. `tp_size_` = `pcp_size_` = `dp_size_` = 1, we simply return the sizes unaltered and the ranks set to 0.

Expert Parallelism is considered only when either `dp_size_`, `pcp_size_` or `tp_size_` is non trivial.

Note that PCP serves the same function as DP here.

When TP = 2, DP(PCP) = 1 and EP = False, the configuration on different devices:

- device 0 : TP = {2, 0} DP = {1, 0} EP = {1, 0} // legend : {size, rank}
- device 1 : TP = {2, 1} DP = {1, 0} EP = {1, 0}
- Comment : Tensors are sharded across 2 devices.

When TP = 1, DP(PCP) = 2 and EP = False, the configuration on different devices:

- device 0 : TP = {2, 0} DP = {2, 0} EP = {1, 0}
- device 1 : TP = {2, 1} DP = {2, 1} EP = {1, 0}
- Comment: There are 2 engine instances and the tensors are sharded across 2 decvices.

When TP = 2, DP(PCP) = 2 and EP = False, the configuration on different devices:

- device 0: TP = {4, 0} DP = {2, 0} EP = {1, 0}
- device 1: TP = {4, 1} DP = {2, 0} EP = {1, 0}
- device 2: TP = {4, 2} DP = {2, 1} EP = {1, 0}
- device 3: TP = {4, 3} DP = {2, 1} EP = {1, 0}
- Comment: There are 2 engine instances and the tensors are sharded across 4 devices.

When, TP = 2, DP(PCP) = 1 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {1, 0} EP = {2, 0}
- device 1: TP = {1, 0} DP = {1, 0} EP = {2, 1}
- Comment: The experts are split between the 2 devices.

When, TP = 1, DP(PCP) = 2 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {2, 0} EP = {2, 0}
- device 1: TP = {1, 0} DP = {2, 1} EP = {2, 1}
- Comment: There are 2 engine instances and the experts are split between the 2 devices.

When TP = 2, DP(PCP) = 2 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {2, 0} EP = {4, 0}
- device 1: TP = {1, 0} DP = {2, 0} EP = {4, 1}
- device 2: TP = {1, 0} DP = {2, 1} EP = {4, 2}
- device 3: TP = {1, 0} DP = {2, 1} EP = {4, 3}
- Comment: There are 2 engine instances and the experts are split between the 4 devices.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
@staticmethod
defmake(
    tp_size_: int,
    pcp_size_: int,
    dp_size_: int,
    sp_size_: int,
    vllm_parallel_config: ParallelConfig,
) -> "FusedMoEParallelConfig":
"""
    Determine MoE parallel configuration. Based on the input `tp_size_`,
    `dp_size_` and vllm's parallel config, determine what
    level's of parallelism to use in the fused moe layer.

    Args:
        tp_size_ (int): `tp_size` passed into the FusedMoE constructor.
        pcp_size_ (int): `pcp_size` passed into the FusedMoE constructor.
        dp_size_ (int): `dp_size` passed into the FusedMoE constructor.
        vllm_parallel_config (ParallelConfig): vLLM's parallel config
            object which contains the `enable_expert_parallel` flag.

    Examples:
        When there is no parallelism requested,
        i.e. `tp_size_` = `pcp_size_` = `dp_size_` = 1, we simply return the sizes
        unaltered and the ranks set to 0.

        Expert Parallelism is considered only when either `dp_size_`, `pcp_size_` or
        `tp_size_` is non trivial.

        Note that PCP serves the same function as DP here.

        When TP = 2, DP(PCP) = 1 and EP = False, the configuration on different
        devices:

        - device 0 : TP = {2, 0} DP = {1, 0} EP = {1, 0} //
            legend : {size, rank}
        - device 1 : TP = {2, 1} DP = {1, 0} EP = {1, 0}
        - Comment : Tensors are sharded across 2 devices.

        When TP = 1, DP(PCP) = 2 and EP = False, the configuration on different
            devices:

        - device 0 : TP = {2, 0} DP = {2, 0} EP = {1, 0}
        - device 1 : TP = {2, 1} DP = {2, 1} EP = {1, 0}
        - Comment: There are 2 engine instances and the tensors are sharded
            across 2 decvices.

        When TP = 2, DP(PCP) = 2 and EP = False, the configuration on different
            devices:

        - device 0: TP = {4, 0} DP = {2, 0} EP = {1, 0}
        - device 1: TP = {4, 1} DP = {2, 0} EP = {1, 0}
        - device 2: TP = {4, 2} DP = {2, 1} EP = {1, 0}
        - device 3: TP = {4, 3} DP = {2, 1} EP = {1, 0}
        - Comment: There are 2 engine instances and the tensors are sharded
            across 4 devices.

        When, TP = 2, DP(PCP) = 1 and EP = True, the configuration on different
            devices:

        - device 0: TP = {1, 0} DP = {1, 0} EP = {2, 0}
        - device 1: TP = {1, 0} DP = {1, 0} EP = {2, 1}
        - Comment: The experts are split between the 2 devices.

        When, TP = 1, DP(PCP) = 2 and EP = True, the configuration on different
            devices:

        - device 0: TP = {1, 0} DP = {2, 0} EP = {2, 0}
        - device 1: TP = {1, 0} DP = {2, 1} EP = {2, 1}
        - Comment: There are 2 engine instances and the experts are split
            between the 2 devices.

        When TP = 2, DP(PCP) = 2 and EP = True, the configuration on different
            devices:

        - device 0: TP = {1, 0} DP = {2, 0} EP = {4, 0}
        - device 1: TP = {1, 0} DP = {2, 0} EP = {4, 1}
        - device 2: TP = {1, 0} DP = {2, 1} EP = {4, 2}
        - device 3: TP = {1, 0} DP = {2, 1} EP = {4, 3}
        - Comment: There are 2 engine instances and the experts are split
            between the 4 devices.
    """
    use_ep = (
        dp_size_ * pcp_size_ * tp_size_ > 1
        and vllm_parallel_config.enable_expert_parallel
    )

    dp_size = dp_size_
    dp_rank = get_dp_group().rank_in_group if dp_size > 1 else 0
    pcp_size = pcp_size_
    pcp_rank = get_pcp_group().rank_in_group if pcp_size > 1 else 0
    tp_size, tp_rank = FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp(
        tp_size_, dp_size_, dp_rank, pcp_size_, pcp_rank
    )

    if not use_ep:
        return FusedMoEParallelConfig(
            tp_size=tp_size,
            tp_rank=tp_rank,
            pcp_size=pcp_size,
            pcp_rank=pcp_rank,
            dp_size=dp_size,
            dp_rank=dp_rank,
            ep_size=1,
            ep_rank=0,
            sp_size=sp_size_,
            use_ep=False,
            all2all_backend=vllm_parallel_config.all2all_backend,
            enable_eplb=vllm_parallel_config.enable_eplb,
        )
    # DP + EP / TP + EP / DP + TP + EP
    assert use_ep
    # In EP, each device owns a set of experts fully. There is no tensor
    # parallel update tp_size, tp_rank, ep_size and ep_rank to reflect that.
    ep_size = tp_size
    ep_rank = tp_rank
    return FusedMoEParallelConfig(
        tp_size=1,
        tp_rank=0,
        pcp_size=pcp_size,
        pcp_rank=pcp_rank,
        dp_size=dp_size,
        dp_rank=dp_rank,
        ep_size=ep_size,
        ep_rank=ep_rank,
        sp_size=sp_size_,
        use_ep=True,
        all2all_backend=vllm_parallel_config.all2all_backend,
        enable_eplb=vllm_parallel_config.enable_eplb,
    )
```

### make\_no\_parallel `classmethod` [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make_no_parallel "Permanent link")

```
make_no_parallel() -> FusedMoEParallelConfig
```

For usage in CI/CD and testing.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
@classmethod
defmake_no_parallel(cls) -> "FusedMoEParallelConfig":
"""For usage in CI/CD and testing."""
    return FusedMoEParallelConfig(
        tp_size=1,
        tp_rank=0,
        pcp_size=1,
        pcp_rank=0,
        dp_size=1,
        dp_rank=0,
        ep_size=1,
        ep_rank=0,
        sp_size=1,
        use_ep=False,
        all2all_backend="allgather_reducescatter",
        enable_eplb=False,
    )
```

## FusedMoEQuantConfig `dataclass` [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig "Permanent link")

The FusedMoEQuantConfig contains all the quantization parameters for a single FusedMoEMethodBase operation. It consists of four FusedMoEQuantDescs, one for each activation and set of weights.

Each FusedMoEMethodBase must implement a get\_fused\_moe\_quant\_config method to construct a FusedMoEQuantConfig for use with that class.

FusedMoEQuant configs are only used for modular kernels, fused\_experts (from fused\_moe.py), cutlass\_moe\_fp\[48], rocm\_aiter\_fused\_experts and triton\_kernel\_moe\_forward. Other MoE methods can ignore the FusedMoEQuantConfig (for now) and hardcode it to None.

There are currently some restrictions on what can be expressed: - Most MoE ops only support similar quantization strategies for each parameter, e.g. both weights must have the same GroupShape and both activations must share the same GroupShape. One exception to this is the cutlass moe which allows per channel quantization on the outputs. Note: this restrictions are not always rigorously checked. - Not all fused MoE functions support all the parameters, e.g. zero points, global scales, alphas and biases are not universally supported. - Fully general GroupShapes are not allowed. Activations only support per token, per tensor or K-blocked. - Weights are not required to have a GroupShape since they have already been quantized.

Other notes: - PrecisionConfigs are specific to GPT OSS Triton. - As a follow up it would probably make sense to subclass FusedMoEQuantDesc or FusedMoEQuantConfig for particular FusedMoEMethodBase subclasses so that only the required quantization parameters are used/stored.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
@dataclass
classFusedMoEQuantConfig:
"""
    The FusedMoEQuantConfig contains all the quantization parameters for
    a single FusedMoEMethodBase operation.  It consists of four
    FusedMoEQuantDescs, one for each activation and set of weights.

    Each FusedMoEMethodBase must implement a get_fused_moe_quant_config
    method to construct a FusedMoEQuantConfig for use with that class.

    FusedMoEQuant configs are only used for modular kernels, fused_experts
    (from fused_moe.py), cutlass_moe_fp[48], rocm_aiter_fused_experts and
    triton_kernel_moe_forward.  Other MoE methods can ignore the
    FusedMoEQuantConfig (for now) and hardcode it to None.

    There are currently some restrictions on what can be expressed:
    - Most MoE ops only support similar quantization strategies for
      each parameter, e.g. both weights must have the same GroupShape
      and both activations must share the same GroupShape.  One exception to
      this is the cutlass moe which allows per channel quantization on the
      outputs.  Note: this restrictions are not always rigorously checked.
    - Not all fused MoE functions support all the parameters, e.g. zero points,
      global scales, alphas and biases are not universally supported.
    - Fully general GroupShapes are not allowed.  Activations only support
      per token, per tensor or K-blocked.
    - Weights are not required to have a GroupShape since they have already
      been quantized.

    Other notes:
    - PrecisionConfigs are specific to GPT OSS Triton.
    - As a follow up it would probably make sense to subclass FusedMoEQuantDesc
      or FusedMoEQuantConfig for particular FusedMoEMethodBase subclasses
      so that only the required quantization parameters are used/stored.
    """

    # TODO(bnell) make sure a1_scales/a2_scales don't interfere with chunking
    _a1: FusedMoEQuantDesc
    _a2: FusedMoEQuantDesc
    _w1: FusedMoEQuantDesc
    _w2: FusedMoEQuantDesc
    is_nvfp4_scale_swizzled: bool = True

    # MXFP4-specific TRTLLM parameters for SwiGLU activation clamping.
    # These correspond to gemm1_alpha, gemm1_beta, gemm1_clamp_limit
    # in TrtLlmMxfp4ExpertsBase.
    gemm1_alpha: float | None = None
    gemm1_beta: float | None = None
    gemm1_clamp_limit: float | None = None

    mx_alignment: int = 0

    def__post_init__(self):
        assert not self.per_act_token_quant or self.block_shape is None, (
            "illegal quantization"
        )

    #
    # Convenience accessors for various properties.
    #

    @property
    defquant_dtype(self) -> torch.dtype | str | None:
        return self._a1.dtype

    @property
    defweight_quant_dtype(self) -> torch.dtype | str | None:
        return self._w1.dtype

    @property
    defis_quantized(self) -> bool:
        return self.quant_dtype is not None

    @property
    defis_per_act_token(self) -> bool:
        return self._a1.shape == GroupShape.PER_TOKEN

    @property
    defper_act_token_quant(self) -> bool:
        return self._a1.shape == GroupShape.PER_TOKEN

    @property
    defper_out_ch_quant(self) -> bool:
        return self._w1.shape == GroupShape.PER_TOKEN

    @property
    defis_per_tensor(self) -> bool:
        return self._a1.shape == GroupShape.PER_TENSOR

    @property
    defblock_shape(self) -> list[int] | None:
        if (
            self._a1.shape is not None
            and self._a1.shape != GroupShape.PER_TENSOR
            and self._a1.shape != GroupShape.PER_TOKEN
        ):
            return [self._a1.shape.row, self._a1.shape.col]
        else:
            return None

    @property
    defis_block_quantized(self) -> bool:
        return self.block_shape is not None

    @property
    defa1_scale(self) -> torch.Tensor | None:
        assert self._a1.scale is None or isinstance(self._a1.scale, torch.Tensor)
        return self._a1.scale

    @property
    defa1_gscale(self) -> torch.Tensor | None:
        return self._a1.alpha_or_gscale

    @property
    defa2_scale(self) -> torch.Tensor | None:
        assert self._a2.scale is None or isinstance(self._a2.scale, torch.Tensor)
        return self._a2.scale

    @property
    defa2_gscale(self) -> torch.Tensor | None:
        return self._a2.alpha_or_gscale

    @property
    defw1_scale(self) -> torch.Tensor | None:
        assert self._w1.scale is None or isinstance(self._w1.scale, torch.Tensor)
        return self._w1.scale

    @property
    defw1_zp(self) -> torch.Tensor | None:
        return self._w1.zp

    @property
    defw1_bias(self) -> torch.Tensor | None:
        return self._w1.bias

    @property
    defw1_precision(self) -> "PrecisionConfig | None":
        assert self._w1.scale is None or isinstance(self._w1.scale, PrecisionConfig)
        return self._w1.scale

    @property
    defg1_alphas(self) -> torch.Tensor | None:
        return self._w1.alpha_or_gscale

    @property
    defw2_scale(self) -> torch.Tensor | None:
        assert self._w2.scale is None or isinstance(self._w2.scale, torch.Tensor)
        return self._w2.scale

    @property
    defw2_zp(self) -> torch.Tensor | None:
        return self._w2.zp

    @property
    defw2_bias(self) -> torch.Tensor | None:
        return self._w2.bias

    @property
    defw2_precision(self) -> "PrecisionConfig | None":
        assert self._w2.scale is None or isinstance(self._w2.scale, PrecisionConfig)
        return self._w2.scale

    @property
    defg2_alphas(self) -> torch.Tensor | None:
        return self._w2.alpha_or_gscale

    @property
    defuse_fp8_w8a8(self) -> bool:
        return self.quant_dtype == current_platform.fp8_dtype()

    @property
    defuse_int8_w8a8(self) -> bool:
        return self.quant_dtype == torch.int8

    @property
    defuse_int8_w8a16(self) -> bool:
        return self._a1.dtype is None and self._w1.dtype == torch.int8

    @property
    defuse_fp8_w8a16(self) -> bool:
        return self._a1.dtype is None and self._w1.dtype == current_platform.fp8_dtype()

    @property
    defuse_int4_w4a16(self) -> bool:
        return self._a1.dtype is None and self._w1.dtype == "int4"

    @property
    defuse_nvfp4_w4a16(self) -> bool:
        return self._a1.dtype is None and self._w1.dtype == "nvfp4"

    @property
    defocp_mx_scheme(self) -> str | None:
        if not hasattr(self, "_ocp_mx_scheme"):
            if (self._a1.dtype is not None and not isinstance(self._a1.dtype, str)) or (
                self._w1.dtype is not None and not isinstance(self._w1.dtype, str)
            ):
                self._ocp_mx_scheme = None
            else:
                ocp_mx_scheme = OCP_MX_Scheme.from_quant_dtype(
                    self._a1.dtype, self._w1.dtype
                )

                if ocp_mx_scheme is not None:
                    ocp_mx_scheme = ocp_mx_scheme.value

                self._ocp_mx_scheme = ocp_mx_scheme

        return self._ocp_mx_scheme

    @property
    defuse_mxfp4_w4a16(self) -> bool:
        return self._a1.dtype is None and self._w1.dtype == "mxfp4"

    @property
    defuse_mxfp4_w4a4(self) -> bool:
        return self._a1.dtype == "mxfp4" and self._w1.dtype == "mxfp4"

    @property
    defuse_nvfp4_w4a4(self) -> bool:
        return self.quant_dtype == "nvfp4"

    @property
    defuse_mxfp4_w4a8(self) -> bool:
        return self._a1.dtype == "fp8" and self._w1.dtype == "mxfp4"

    defconfig_name(self, dtype: torch.dtype) -> str | None:
"""
        Return a string used to construct the filename that contains the
        tuning info for a particular quantization scheme.  See
        try_get_optimal_moe_config in fused_moe.py.
        """
        return _get_config_dtype_str(
            use_fp8_w8a8=self.use_fp8_w8a8,
            use_fp8_w8a16=self.use_fp8_w8a16,
            use_int8_w8a16=self.use_int8_w8a16,
            use_int4_w4a16=self.use_int4_w4a16,
            ocp_mx_scheme=self.ocp_mx_scheme,
            dtype=dtype,
        )

    defscale_shape(
        self,
        max_tokens: int,
        hidden_dim: int,
    ) -> tuple[int, int] | None:
"""
        Construct the proper activation scale shape for this
        config.
        """
        if self.is_quantized:
            if self.is_block_quantized:
                assert self.block_shape is not None
                _, block_k = self.block_shape
                k_tiles = cdiv(hidden_dim, block_k)
                return (max_tokens, k_tiles)
            elif self.is_per_act_token:
                return (max_tokens, 1)
            else:
                return (1, 1)
        else:
            return None

    defbatched_scale_shape(
        self,
        num_experts: int,
        max_tokens: int,
        hidden_dim: int,
    ) -> tuple[int, int, int] | None:
"""
        Construct the proper activation batched scale shape for this
        config, e.g. (num experts, *scale_shape).
        """
        if self.is_quantized:
            scale_shape = self.scale_shape(max_tokens, hidden_dim)
            assert scale_shape is not None
            return (num_experts, *scale_shape)
        else:
            return None

    @staticmethod
    defmake(
        quant_dtype: torch.dtype | str | None = None,
        per_act_token_quant: bool = False,
        per_out_ch_quant: bool = False,
        block_shape: list[int] | None = None,
        w1_scale: Union[torch.Tensor, "PrecisionConfig", None] = None,
        w2_scale: Union[torch.Tensor, "PrecisionConfig", None] = None,
        a1_scale: torch.Tensor | None = None,
        a2_scale: torch.Tensor | None = None,
        g1_alphas: torch.Tensor | None = None,
        g2_alphas: torch.Tensor | None = None,
        a1_gscale: torch.Tensor | None = None,
        a2_gscale: torch.Tensor | None = None,
        w1_bias: torch.Tensor | None = None,
        w2_bias: torch.Tensor | None = None,
        w1_zp: torch.Tensor | None = None,
        w2_zp: torch.Tensor | None = None,
        weight_dtype: torch.dtype | str | None = None,
        is_nvfp4_scale_swizzled: bool = True,
        gemm1_alpha: float | None = None,
        gemm1_beta: float | None = None,
        gemm1_clamp_limit: float | None = None,
    ) -> "FusedMoEQuantConfig":
"""
        General builder function for a FusedMoEQuantConfig.
        - quant_dtype: Optional quantization type. None if activations are
          unquantized or quantized prior to calling.  Note: "nvfp4", "mxfp4",
          "mxfp6_e3m2", "mxfp6_e2m3" are the only valid string values
          for quant_dtype.
        - per_act_token_quant: Activations have per token quantization.
        - per_out_ch_quant: Outputs have per channel quantization. (only
          for cutlass).
        - block_shape: Optional block size for block-wise quantization.
          Incompatible with per_act_token and per_out_ch quant.
        - w1_scale: Optional scale to be used for w1.
        - w2_scale: Optional scale to be used for w2.
        - a1_scale: Optional scale to be used for a1.
        - a2_scale: Optional scale to be used for a2.
        - g1_alphas: Optional global quantization scales for w1 (for nvfp4).
                     Optional per-channel scales for w1 (for W4A8 FP8).
                     Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8).
        - g2_alphas: Optional global quantization scales for w2 (for nvfp4).
                     Optional per-channel scales for w2 (for W4A8 FP8).
                     Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8).
        - a1_gscale: Optional global quantization scales for a1 (1.0 /a2_scale).
        - a2_gscale: Optional global quantization scales for a2 (1.0 /a2_scale).

        - w1_bias: Optional biases for w1 (GPT OSS Triton).
        - w2_bias: Optional biases for w1 (GPT OSS Triton).
        - w1_zp: Optional w1 zero points for int4/int8 quantization.
        - w2_zp: Optional w2 zero points for int4/int8 quantization.
        - is_nvfp4_scale_swizzled: Whether to swizzle the nvfp4 scale swizzling.
        - gemm1_alpha: Optional MXFP4 TRTLLM SwiGLU alpha parameter.
        - gemm1_beta: Optional MXFP4 TRTLLM SwiGLU beta parameter.
        - gemm1_clamp_limit: Optional MXFP4 TRTLLM SwiGLU clamp limit.
        """
        assert not isinstance(quant_dtype, str) or quant_dtype in {
            "nvfp4",
            "mxfp4",
            "mxfp6_e3m2",
            "mxfp6_e2m3",
            "mxfp8",
        }
        assert not isinstance(weight_dtype, str) or weight_dtype in {
            "nvfp4",
            "mxfp4",
            "mxfp6_e3m2",
            "mxfp6_e2m3",
            "int4",
            "mxfp8",
        }

        if weight_dtype is None:
            weight_dtype = quant_dtype

        a_shape, w_shape = _quant_flags_to_group_shape(
            quant_dtype, per_act_token_quant, per_out_ch_quant, block_shape
        )
        quant_config = FusedMoEQuantConfig(
            _a1=FusedMoEQuantDesc(quant_dtype, a_shape, a1_scale, a1_gscale),
            _a2=FusedMoEQuantDesc(quant_dtype, a_shape, a2_scale, a2_gscale),
            _w1=FusedMoEQuantDesc(
                weight_dtype, w_shape, w1_scale, g1_alphas, w1_zp, w1_bias
            ),
            _w2=FusedMoEQuantDesc(
                weight_dtype, w_shape, w2_scale, g2_alphas, w2_zp, w2_bias
            ),
            is_nvfp4_scale_swizzled=is_nvfp4_scale_swizzled,
            gemm1_alpha=gemm1_alpha,
            gemm1_beta=gemm1_beta,
            gemm1_clamp_limit=gemm1_clamp_limit,
        )
        assert quant_config.per_act_token_quant == per_act_token_quant
        assert quant_config.per_out_ch_quant == per_out_ch_quant
        assert quant_config.block_shape == block_shape
        return quant_config
```

### batched\_scale\_shape [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.batched_scale_shape "Permanent link")

Construct the proper activation batched scale shape for this config, e.g. (num experts, \*scale\_shape).

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defbatched_scale_shape(
    self,
    num_experts: int,
    max_tokens: int,
    hidden_dim: int,
) -> tuple[int, int, int] | None:
"""
    Construct the proper activation batched scale shape for this
    config, e.g. (num experts, *scale_shape).
    """
    if self.is_quantized:
        scale_shape = self.scale_shape(max_tokens, hidden_dim)
        assert scale_shape is not None
        return (num_experts, *scale_shape)
    else:
        return None
```

### config\_name [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.config_name "Permanent link")

Return a string used to construct the filename that contains the tuning info for a particular quantization scheme. See try\_get\_optimal\_moe\_config in fused\_moe.py.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defconfig_name(self, dtype: torch.dtype) -> str | None:
"""
    Return a string used to construct the filename that contains the
    tuning info for a particular quantization scheme.  See
    try_get_optimal_moe_config in fused_moe.py.
    """
    return _get_config_dtype_str(
        use_fp8_w8a8=self.use_fp8_w8a8,
        use_fp8_w8a16=self.use_fp8_w8a16,
        use_int8_w8a16=self.use_int8_w8a16,
        use_int4_w4a16=self.use_int4_w4a16,
        ocp_mx_scheme=self.ocp_mx_scheme,
        dtype=dtype,
    )
```

### make `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.make "Permanent link")

```
make(
    quant_dtype: dtype | str | None = None,
    per_act_token_quant: bool = False,
    per_out_ch_quant: bool = False,
    block_shape: list[int] | None = None,
    w1_scale: Union[Tensor, PrecisionConfig, None] = None,
    w2_scale: Union[Tensor, PrecisionConfig, None] = None,
    a1_scale: Tensor | None = None,
    a2_scale: Tensor | None = None,
    g1_alphas: Tensor | None = None,
    g2_alphas: Tensor | None = None,
    a1_gscale: Tensor | None = None,
    a2_gscale: Tensor | None = None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    w1_zp: Tensor | None = None,
    w2_zp: Tensor | None = None,
    weight_dtype: dtype | str | None = None,
    is_nvfp4_scale_swizzled: bool = True,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
) -> FusedMoEQuantConfig
```

General builder function for a FusedMoEQuantConfig. - quant\_dtype: Optional quantization type. None if activations are unquantized or quantized prior to calling. Note: "nvfp4", "mxfp4", "mxfp6\_e3m2", "mxfp6\_e2m3" are the only valid string values for quant\_dtype. - per\_act\_token\_quant: Activations have per token quantization. - per\_out\_ch\_quant: Outputs have per channel quantization. (only for cutlass). - block\_shape: Optional block size for block-wise quantization. Incompatible with per\_act\_token and per\_out\_ch quant. - w1\_scale: Optional scale to be used for w1. - w2\_scale: Optional scale to be used for w2. - a1\_scale: Optional scale to be used for a1. - a2\_scale: Optional scale to be used for a2. - g1\_alphas: Optional global quantization scales for w1 (for nvfp4). Optional per-channel scales for w1 (for W4A8 FP8). Optional dq scale i.e. w\_scale * a\_scale (for W8A8 fp8). - g2\_alphas: Optional global quantization scales for w2 (for nvfp4). Optional per-channel scales for w2 (for W4A8 FP8). Optional dq scale i.e. w\_scale * a\_scale (for W8A8 fp8). - a1\_gscale: Optional global quantization scales for a1 (1.0 /a2\_scale). - a2\_gscale: Optional global quantization scales for a2 (1.0 /a2\_scale).

- w1\_bias: Optional biases for w1 (GPT OSS Triton).
- w2\_bias: Optional biases for w1 (GPT OSS Triton).
- w1\_zp: Optional w1 zero points for int4/int8 quantization.
- w2\_zp: Optional w2 zero points for int4/int8 quantization.
- is\_nvfp4\_scale\_swizzled: Whether to swizzle the nvfp4 scale swizzling.
- gemm1\_alpha: Optional MXFP4 TRTLLM SwiGLU alpha parameter.
- gemm1\_beta: Optional MXFP4 TRTLLM SwiGLU beta parameter.
- gemm1\_clamp\_limit: Optional MXFP4 TRTLLM SwiGLU clamp limit.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
@staticmethod
defmake(
    quant_dtype: torch.dtype | str | None = None,
    per_act_token_quant: bool = False,
    per_out_ch_quant: bool = False,
    block_shape: list[int] | None = None,
    w1_scale: Union[torch.Tensor, "PrecisionConfig", None] = None,
    w2_scale: Union[torch.Tensor, "PrecisionConfig", None] = None,
    a1_scale: torch.Tensor | None = None,
    a2_scale: torch.Tensor | None = None,
    g1_alphas: torch.Tensor | None = None,
    g2_alphas: torch.Tensor | None = None,
    a1_gscale: torch.Tensor | None = None,
    a2_gscale: torch.Tensor | None = None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    w1_zp: torch.Tensor | None = None,
    w2_zp: torch.Tensor | None = None,
    weight_dtype: torch.dtype | str | None = None,
    is_nvfp4_scale_swizzled: bool = True,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
) -> "FusedMoEQuantConfig":
"""
    General builder function for a FusedMoEQuantConfig.
    - quant_dtype: Optional quantization type. None if activations are
      unquantized or quantized prior to calling.  Note: "nvfp4", "mxfp4",
      "mxfp6_e3m2", "mxfp6_e2m3" are the only valid string values
      for quant_dtype.
    - per_act_token_quant: Activations have per token quantization.
    - per_out_ch_quant: Outputs have per channel quantization. (only
      for cutlass).
    - block_shape: Optional block size for block-wise quantization.
      Incompatible with per_act_token and per_out_ch quant.
    - w1_scale: Optional scale to be used for w1.
    - w2_scale: Optional scale to be used for w2.
    - a1_scale: Optional scale to be used for a1.
    - a2_scale: Optional scale to be used for a2.
    - g1_alphas: Optional global quantization scales for w1 (for nvfp4).
                 Optional per-channel scales for w1 (for W4A8 FP8).
                 Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8).
    - g2_alphas: Optional global quantization scales for w2 (for nvfp4).
                 Optional per-channel scales for w2 (for W4A8 FP8).
                 Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8).
    - a1_gscale: Optional global quantization scales for a1 (1.0 /a2_scale).
    - a2_gscale: Optional global quantization scales for a2 (1.0 /a2_scale).

    - w1_bias: Optional biases for w1 (GPT OSS Triton).
    - w2_bias: Optional biases for w1 (GPT OSS Triton).
    - w1_zp: Optional w1 zero points for int4/int8 quantization.
    - w2_zp: Optional w2 zero points for int4/int8 quantization.
    - is_nvfp4_scale_swizzled: Whether to swizzle the nvfp4 scale swizzling.
    - gemm1_alpha: Optional MXFP4 TRTLLM SwiGLU alpha parameter.
    - gemm1_beta: Optional MXFP4 TRTLLM SwiGLU beta parameter.
    - gemm1_clamp_limit: Optional MXFP4 TRTLLM SwiGLU clamp limit.
    """
    assert not isinstance(quant_dtype, str) or quant_dtype in {
        "nvfp4",
        "mxfp4",
        "mxfp6_e3m2",
        "mxfp6_e2m3",
        "mxfp8",
    }
    assert not isinstance(weight_dtype, str) or weight_dtype in {
        "nvfp4",
        "mxfp4",
        "mxfp6_e3m2",
        "mxfp6_e2m3",
        "int4",
        "mxfp8",
    }

    if weight_dtype is None:
        weight_dtype = quant_dtype

    a_shape, w_shape = _quant_flags_to_group_shape(
        quant_dtype, per_act_token_quant, per_out_ch_quant, block_shape
    )
    quant_config = FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(quant_dtype, a_shape, a1_scale, a1_gscale),
        _a2=FusedMoEQuantDesc(quant_dtype, a_shape, a2_scale, a2_gscale),
        _w1=FusedMoEQuantDesc(
            weight_dtype, w_shape, w1_scale, g1_alphas, w1_zp, w1_bias
        ),
        _w2=FusedMoEQuantDesc(
            weight_dtype, w_shape, w2_scale, g2_alphas, w2_zp, w2_bias
        ),
        is_nvfp4_scale_swizzled=is_nvfp4_scale_swizzled,
        gemm1_alpha=gemm1_alpha,
        gemm1_beta=gemm1_beta,
        gemm1_clamp_limit=gemm1_clamp_limit,
    )
    assert quant_config.per_act_token_quant == per_act_token_quant
    assert quant_config.per_out_ch_quant == per_out_ch_quant
    assert quant_config.block_shape == block_shape
    return quant_config
```

### scale\_shape [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.scale_shape "Permanent link")

Construct the proper activation scale shape for this config.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defscale_shape(
    self,
    max_tokens: int,
    hidden_dim: int,
) -> tuple[int, int] | None:
"""
    Construct the proper activation scale shape for this
    config.
    """
    if self.is_quantized:
        if self.is_block_quantized:
            assert self.block_shape is not None
            _, block_k = self.block_shape
            k_tiles = cdiv(hidden_dim, block_k)
            return (max_tokens, k_tiles)
        elif self.is_per_act_token:
            return (max_tokens, 1)
        else:
            return (1, 1)
    else:
        return None
```

## FusedMoEQuantDesc `dataclass` [¶](#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantDesc "Permanent link")

A quantization descriptor for fused MoE ops. This class can describe either activations or weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
@dataclass
classFusedMoEQuantDesc:
"""
    A quantization descriptor for fused MoE ops. This class can describe
    either activations or weights.
    """

    # The quantized type of this parameters.  None means unquantized or
    # already quantized.
    # TODO (bnell): use scalar_type instead of Union.
    dtype: torch.dtype | str | None = None

    # A field that describes the quantization group shape, from quant_utils.py.
    #  * (-1, -1)   for per-tensor quantization
    #  * (1, -1)    for per-row quantization
    #  * (-1, 1)    for per-column quantization
    #  * (128, 128) for 128x128 deepseek style block quantization
    #  * (1, 128)   for deepseek style activation quantization
    #               (i.e. per-token-per-group)
    shape: GroupShape | None = None

    # Quantization scales.
    # TODO(bnell): maybe put PrecisionConfigs in subclass of QuantDesc?
    scale: Union[torch.Tensor, "PrecisionConfig", None] = None

    # Quantization alphas or gscales, used for nvfp4 types.
    # W4A8 FP8: used for per-channel scales
    # TODO(bnell): put some of these in subclasses
    alpha_or_gscale: torch.Tensor | None = None

    # Zero points for int4/int8 types
    zp: torch.Tensor | None = None

    # Biases for GPT triton MoE
    bias: torch.Tensor | None = None
```

## \_get\_config\_dtype\_str [¶](#vllm.model_executor.layers.fused_moe.config._get_config_dtype_str "Permanent link")

```
_get_config_dtype_str(
    dtype: dtype,
    use_fp8_w8a8: bool = False,
    use_fp8_w8a16: bool = False,
    use_int8_w8a16: bool = False,
    use_int4_w4a16: bool = False,
    ocp_mx_scheme: str | None = None,
) -> str | None
```

Return a string used to construct the filename that contains the tuning info for a particular quantization scheme. See try\_get\_optimal\_moe\_config in fused\_moe.py.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
def_get_config_dtype_str(
    dtype: torch.dtype,
    use_fp8_w8a8: bool = False,
    use_fp8_w8a16: bool = False,
    use_int8_w8a16: bool = False,
    use_int4_w4a16: bool = False,
    ocp_mx_scheme: str | None = None,
) -> str | None:
"""
    Return a string used to construct the filename that contains the
    tuning info for a particular quantization scheme.  See
    try_get_optimal_moe_config in fused_moe.py.
    """
    if use_fp8_w8a8:
        return "fp8_w8a8"
    elif use_fp8_w8a16:
        return "fp8_w8a16"
    elif use_int8_w8a16:
        return "int8_w8a16"
    elif use_int4_w4a16:
        return "int4_w4a16"
    elif ocp_mx_scheme is not None:
        # The output of this function is passed to `try_get_optimal_moe_config`,
        # and as we only simulate OCP MX execution in fused_moe for now,
        # we will NOT look for `*,dtype=w_mxfp4_a_mxfp4.json` for now.
        return None
    elif dtype == torch.float:
        # avoiding cases where kernel fails when float32 MoE
        # use fp16/bfloat16 configs
        return "float32"
    return None
```

## \_quant\_flags\_to\_group\_shape [¶](#vllm.model_executor.layers.fused_moe.config._quant_flags_to_group_shape "Permanent link")

Convert MoE quantization flags into more generic GroupShapes.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
def_quant_flags_to_group_shape(
    quant_dtype: torch.dtype | str | None,
    per_act_token_quant: bool,
    per_out_ch_quant: bool,
    block_shape: list[int] | None,
) -> tuple[GroupShape | None, GroupShape | None]:
"""
    Convert MoE quantization flags into more generic GroupShapes.
    """
    a_shape: GroupShape | None
    w_shape: GroupShape | None
    if block_shape is not None:
        assert not per_act_token_quant
        assert not per_out_ch_quant
        # TODO(bnell): this is not quite right for activations since first
        # dim should be 1.
        a_shape = GroupShape(row=block_shape[0], col=block_shape[1])
        w_shape = GroupShape(row=block_shape[0], col=block_shape[1])
    else:
        w_shape = None
        a_shape = None if quant_dtype is None else GroupShape.PER_TENSOR

        if per_act_token_quant:
            a_shape = GroupShape.PER_TOKEN

        if per_out_ch_quant:
            w_shape = GroupShape.PER_TOKEN

    return a_shape, w_shape
```

## awq\_marlin\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.awq_marlin_moe_quant_config "Permanent link")

Construct a quant config for awq marlin quantization.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defawq_marlin_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    w1_zp: torch.Tensor | None,
    w2_zp: torch.Tensor | None,
    weight_bits: int,
    group_size: int,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for awq marlin quantization.
    """
    fromvllm.model_executor.layers.quantization.utils.quant_utilsimport GroupShape

    w_shape = None if group_size == -1 else GroupShape(row=1, col=group_size)

    # Activations are NOT quantized for AWQ (fp16/bf16)
    a_shape = w_shape  # Same as weight shape for alignment

    # Determine weight dtype
    if weight_bits == 4:
        weight_dtype = "int4"
    elif weight_bits == 8:
        weight_dtype = torch.int8
    else:
        raise ValueError(f"Unsupported weight_bits: {weight_bits}")

    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(dtype=None, shape=a_shape),
        _a2=FusedMoEQuantDesc(dtype=None, shape=a_shape),
        _w1=FusedMoEQuantDesc(weight_dtype, w_shape, w1_scale, None, w1_zp, w1_bias),
        _w2=FusedMoEQuantDesc(weight_dtype, w_shape, w2_scale, None, w2_zp, w2_bias),
    )
```

## biased\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.biased_moe_quant_config "Permanent link")

```
biased_moe_quant_config(
    w1_bias: Tensor | None, w2_bias: Tensor | None
) -> FusedMoEQuantConfig
```

Construct a quant config for unquantized activations with biases.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defbiased_moe_quant_config(
    w1_bias: torch.Tensor | None,
    w2_bias: torch.Tensor | None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for unquantized activations with biases.
    """
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(),
        _a2=FusedMoEQuantDesc(),
        _w1=FusedMoEQuantDesc(bias=w1_bias),
        _w2=FusedMoEQuantDesc(bias=w2_bias),
    )
```

## fp8\_w8a16\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.fp8_w8a16_moe_quant_config "Permanent link")

```
fp8_w8a16_moe_quant_config(
    w1_scale: Tensor,
    w2_scale: Tensor,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig
```

Construct a quant config for 16-bit float activations and fp8 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
deffp8_w8a16_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for 16-bit float activations and fp8 weights.
    """
    group_shape = GroupShape(*block_shape) if block_shape is not None else None
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(),
        _a2=FusedMoEQuantDesc(),
        _w1=FusedMoEQuantDesc(
            current_platform.fp8_dtype(), group_shape, w1_scale, None, None
        ),
        _w2=FusedMoEQuantDesc(
            current_platform.fp8_dtype(), group_shape, w2_scale, None, None
        ),
    )
```

## fp8\_w8a8\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.fp8_w8a8_moe_quant_config "Permanent link")

```
fp8_w8a8_moe_quant_config(
    w1_scale: Tensor,
    w2_scale: Tensor,
    a1_scale: Tensor | None = None,
    a2_scale: Tensor | None = None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    per_act_token_quant: bool = False,
    per_out_ch_quant: bool = False,
    block_shape: list[int] | None = None,
    a1_gscale: Tensor | None = None,
    a2_gscale: Tensor | None = None,
    g1_alphas: Tensor | None = None,
    g2_alphas: Tensor | None = None,
) -> FusedMoEQuantConfig
```

Construct a quant config for fp8 activations and fp8 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
deffp8_w8a8_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    a1_scale: torch.Tensor | None = None,
    a2_scale: torch.Tensor | None = None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    per_act_token_quant: bool = False,
    per_out_ch_quant: bool = False,
    block_shape: list[int] | None = None,
    a1_gscale: torch.Tensor | None = None,
    a2_gscale: torch.Tensor | None = None,
    g1_alphas: torch.Tensor | None = None,
    g2_alphas: torch.Tensor | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for fp8 activations and fp8 weights.
    """
    return FusedMoEQuantConfig.make(
        current_platform.fp8_dtype(),
        w1_scale=w1_scale,
        g1_alphas=g1_alphas,
        w2_scale=w2_scale,
        g2_alphas=g2_alphas,
        w1_bias=w1_bias,
        w2_bias=w2_bias,
        a1_scale=a1_scale,
        a1_gscale=a1_gscale,
        a2_scale=a2_scale,
        a2_gscale=a2_gscale,
        per_act_token_quant=per_act_token_quant,
        per_out_ch_quant=per_out_ch_quant,
        block_shape=block_shape,
    )
```

## gptq\_marlin\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.gptq_marlin_moe_quant_config "Permanent link")

```
gptq_marlin_moe_quant_config(
    w1_scale: Tensor,
    w2_scale: Tensor,
    weight_bits: int,
    group_size: int,
    w1_zp: Tensor | None = None,
    w2_zp: Tensor | None = None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
)
```

Construct a quant config for gptq marlin quantization.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defgptq_marlin_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    weight_bits: int,
    group_size: int,
    w1_zp: torch.Tensor | None = None,
    w2_zp: torch.Tensor | None = None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
):
"""
    Construct a quant config for gptq marlin quantization.
    """
    fromvllm.model_executor.layers.quantization.utils.quant_utilsimport GroupShape

    w_shape = None if group_size == -1 else GroupShape(row=1, col=group_size)

    # Activations are NOT quantized for GPTQ (fp16/bf16)
    a_shape = w_shape  # Same as weight shape for alignment

    # Determine weight dtype
    if weight_bits == 4:
        weight_dtype = "int4"
    elif weight_bits == 8:
        weight_dtype = torch.int8
    else:
        raise ValueError(f"Unsupported weight_bits: {weight_bits}")

    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(dtype=None, shape=a_shape),
        _a2=FusedMoEQuantDesc(dtype=None, shape=a_shape),
        _w1=FusedMoEQuantDesc(weight_dtype, w_shape, w1_scale, None, w1_zp, w1_bias),
        _w2=FusedMoEQuantDesc(weight_dtype, w_shape, w2_scale, None, w2_zp, w2_bias),
    )
```

## int4\_w4a16\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.int4_w4a16_moe_quant_config "Permanent link")

Construct a quant config for 16-bit float activations and int4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defint4_w4a16_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    w1_zp: torch.Tensor | None,
    w2_zp: torch.Tensor | None,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for 16-bit float activations and int4 weights.
    """
    group_shape = GroupShape(*block_shape) if block_shape is not None else None
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(shape=group_shape),
        _a2=FusedMoEQuantDesc(shape=group_shape),
        _w1=FusedMoEQuantDesc("int4", group_shape, w1_scale, None, w1_zp),
        _w2=FusedMoEQuantDesc("int4", group_shape, w2_scale, None, w2_zp),
    )
```

## int4\_w4afp8\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.int4_w4afp8_moe_quant_config "Permanent link")

```
int4_w4afp8_moe_quant_config(
    w1_scale: Tensor,
    w2_scale: Tensor,
    g1_alphas: Tensor,
    g2_alphas: Tensor,
    per_act_token_quant: bool = False,
    per_out_ch_quant: bool = False,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig
```

Construct a quant config for fp8 activations and int4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defint4_w4afp8_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    g1_alphas: torch.Tensor,
    g2_alphas: torch.Tensor,
    per_act_token_quant: bool = False,
    per_out_ch_quant: bool = False,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for fp8 activations and int4 weights.
    """
    return FusedMoEQuantConfig.make(
        torch.float8_e4m3fn,  # quant dtype for activations
        w1_scale=w1_scale,
        w2_scale=w2_scale,
        g1_alphas=g1_alphas,
        g2_alphas=g2_alphas,
        per_act_token_quant=per_act_token_quant,
        per_out_ch_quant=per_out_ch_quant,
        block_shape=block_shape,
        weight_dtype="int4",  # weight dtype for weights
    )
```

## int8\_w8a16\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.int8_w8a16_moe_quant_config "Permanent link")

Construct a quant config for 16-bit float activations and int8 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defint8_w8a16_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    w1_zp: torch.Tensor | None,
    w2_zp: torch.Tensor | None,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for 16-bit float activations and int8 weights.
    """
    group_shape = GroupShape(*block_shape) if block_shape is not None else None
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(shape=group_shape),
        _a2=FusedMoEQuantDesc(shape=group_shape),
        _w1=FusedMoEQuantDesc(torch.int8, group_shape, w1_scale, None, w1_zp),
        _w2=FusedMoEQuantDesc(torch.int8, group_shape, w2_scale, None, w2_zp),
    )
```

## int8\_w8a8\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.int8_w8a8_moe_quant_config "Permanent link")

```
int8_w8a8_moe_quant_config(
    w1_scale: Tensor,
    w2_scale: Tensor,
    a1_scale: Tensor | None,
    a2_scale: Tensor | None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    per_act_token_quant: bool = False,
) -> FusedMoEQuantConfig
```

Construct a quant config for int8 activations and int8 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defint8_w8a8_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    a1_scale: torch.Tensor | None,
    a2_scale: torch.Tensor | None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    per_act_token_quant: bool = False,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for int8 activations and int8 weights.
    """
    return FusedMoEQuantConfig.make(
        torch.int8,
        w1_scale=w1_scale,
        w2_scale=w2_scale,
        a1_scale=a1_scale,
        a2_scale=a2_scale,
        w1_bias=w1_bias,
        w2_bias=w2_bias,
        per_act_token_quant=per_act_token_quant,
        per_out_ch_quant=False,
        block_shape=None,
    )
```

## mxfp4\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.mxfp4_moe_quant_config "Permanent link")

Construct a quant config for MXFP4 x MXFP4 MoE. MXFP4 uses block scaling only (E8M0 scales, 32-element groups), with no separate alphas / global activation scales in this config.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defmxfp4_moe_quant_config(
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for MXFP4 x MXFP4 MoE.
    MXFP4 uses block scaling only (E8M0 scales, 32-element groups), with no
    separate alphas / global activation scales in this config.
    """
    return FusedMoEQuantConfig.make(
        "mxfp4",
        w1_scale=w1_scale,
        w2_scale=w2_scale,
        per_act_token_quant=False,
        per_out_ch_quant=False,
        block_shape=None,
    )
```

## mxfp4\_mxfp8\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.mxfp4_mxfp8_moe_quant_config "Permanent link")

```
mxfp4_mxfp8_moe_quant_config(
    w1_scale: Union[Tensor, PrecisionConfig],
    w2_scale: Union[Tensor, PrecisionConfig],
    a1_scale: Tensor | None = None,
    a2_scale: Tensor | None = None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    block_shape: list[int] | None = None,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
    mx_alignment: int = 0,
) -> FusedMoEQuantConfig
```

Construct a quant config for mxfp4 activations and mxfp4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defmxfp4_mxfp8_moe_quant_config(
    w1_scale: Union[torch.Tensor, "PrecisionConfig"],
    w2_scale: Union[torch.Tensor, "PrecisionConfig"],
    a1_scale: torch.Tensor | None = None,
    a2_scale: torch.Tensor | None = None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    block_shape: list[int] | None = None,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
    mx_alignment: int = 0,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for mxfp4 activations and mxfp4 weights.
    """
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc("mxfp8"),
        _a2=FusedMoEQuantDesc("mxfp8"),
        _w1=FusedMoEQuantDesc("mxfp4", None, w1_scale, None, None, w1_bias),
        _w2=FusedMoEQuantDesc("mxfp4", None, w2_scale, None, None, w2_bias),
        gemm1_alpha=gemm1_alpha,
        gemm1_beta=gemm1_beta,
        gemm1_clamp_limit=gemm1_clamp_limit,
        mx_alignment=mx_alignment,
    )
```

## mxfp4\_w4a16\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.mxfp4_w4a16_moe_quant_config "Permanent link")

```
mxfp4_w4a16_moe_quant_config(
    w1_scale: Union[Tensor, PrecisionConfig],
    w2_scale: Union[Tensor, PrecisionConfig],
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
) -> FusedMoEQuantConfig
```

Construct a quant config for unquantized activations and mxfp4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defmxfp4_w4a16_moe_quant_config(
    w1_scale: Union[torch.Tensor, "PrecisionConfig"],
    w2_scale: Union[torch.Tensor, "PrecisionConfig"],
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for unquantized activations and mxfp4 weights.
    """
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc(),
        _a2=FusedMoEQuantDesc(),
        _w1=FusedMoEQuantDesc("mxfp4", None, w1_scale, None, None, w1_bias),
        _w2=FusedMoEQuantDesc("mxfp4", None, w2_scale, None, None, w2_bias),
        gemm1_alpha=gemm1_alpha,
        gemm1_beta=gemm1_beta,
        gemm1_clamp_limit=gemm1_clamp_limit,
    )
```

## mxfp4\_w4a8\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.mxfp4_w4a8_moe_quant_config "Permanent link")

```
mxfp4_w4a8_moe_quant_config(
    w1_scale: Union[Tensor, PrecisionConfig],
    w2_scale: Union[Tensor, PrecisionConfig],
    a1_scale: Tensor | None = None,
    a2_scale: Tensor | None = None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig
```

Construct a quant config for fp8 activations and mxfp4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defmxfp4_w4a8_moe_quant_config(
    w1_scale: Union[torch.Tensor, "PrecisionConfig"],
    w2_scale: Union[torch.Tensor, "PrecisionConfig"],
    a1_scale: torch.Tensor | None = None,
    a2_scale: torch.Tensor | None = None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    block_shape: list[int] | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for fp8 activations and mxfp4 weights.
    """
    return FusedMoEQuantConfig(
        _a1=FusedMoEQuantDesc("fp8", None, a1_scale, None, None, None),
        _a2=FusedMoEQuantDesc("fp8", None, a2_scale, None, None, None),
        _w1=FusedMoEQuantDesc("mxfp4", None, w1_scale, None, None, w1_bias),
        _w2=FusedMoEQuantDesc("mxfp4", None, w2_scale, None, None, w2_bias),
    )
```

## nvfp4\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.nvfp4_moe_quant_config "Permanent link")

Construct a quant config for mxfp4 activations and nvp4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defnvfp4_moe_quant_config(
    g1_alphas: torch.Tensor,
    g2_alphas: torch.Tensor,
    a1_gscale: torch.Tensor,
    a2_gscale: torch.Tensor,
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    is_nvfp4_scale_swizzled: bool = True,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for mxfp4 activations and nvp4 weights.
    """
    return FusedMoEQuantConfig.make(
        "nvfp4",
        w1_scale=w1_scale,
        w2_scale=w2_scale,
        w1_bias=w1_bias,
        w2_bias=w2_bias,
        a1_gscale=a1_gscale,
        a2_gscale=a2_gscale,
        g1_alphas=g1_alphas,
        g2_alphas=g2_alphas,
        per_act_token_quant=False,
        per_out_ch_quant=False,
        block_shape=None,
        is_nvfp4_scale_swizzled=is_nvfp4_scale_swizzled,
    )
```

## nvfp4\_w4a16\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.nvfp4_w4a16_moe_quant_config "Permanent link")

Construct a quant config for 16-but activations and nvp4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defnvfp4_w4a16_moe_quant_config(
    g1_alphas: torch.Tensor,
    g2_alphas: torch.Tensor,
    w1_scale: torch.Tensor,
    w2_scale: torch.Tensor,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for 16-but activations and nvp4 weights.
    """
    return FusedMoEQuantConfig.make(
        quant_dtype=None,
        w1_scale=w1_scale,
        w2_scale=w2_scale,
        g1_alphas=g1_alphas,
        g2_alphas=g2_alphas,
        weight_dtype="nvfp4",
    )
```

## ocp\_mx\_moe\_quant\_config [¶](#vllm.model_executor.layers.fused_moe.config.ocp_mx_moe_quant_config "Permanent link")

```
ocp_mx_moe_quant_config(
    quant_dtype: str,
    w1_scale: Union[Tensor, PrecisionConfig],
    w2_scale: Union[Tensor, PrecisionConfig],
    weight_dtype: str | None = None,
    a1_scale: Tensor | None = None,
    a2_scale: Tensor | None = None,
    w1_bias: Tensor | None = None,
    w2_bias: Tensor | None = None,
    block_shape: list[int] | None = None,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
) -> FusedMoEQuantConfig
```

Construct a quant config for mxfp4 activations and mxfp4 weights.

Source code in `vllm/model_executor/layers/fused_moe/config.py`

```
defocp_mx_moe_quant_config(
    quant_dtype: str,
    w1_scale: Union[torch.Tensor, "PrecisionConfig"],
    w2_scale: Union[torch.Tensor, "PrecisionConfig"],
    weight_dtype: str | None = None,
    a1_scale: torch.Tensor | None = None,
    a2_scale: torch.Tensor | None = None,
    w1_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
    block_shape: list[int] | None = None,
    gemm1_alpha: float | None = None,
    gemm1_beta: float | None = None,
    gemm1_clamp_limit: float | None = None,
) -> FusedMoEQuantConfig:
"""
    Construct a quant config for mxfp4 activations and mxfp4 weights.
    """
    assert quant_dtype in OCP_MX_DTYPES
    return FusedMoEQuantConfig.make(
        quant_dtype=quant_dtype,
        weight_dtype=weight_dtype,
        w1_scale=w1_scale,
        w2_scale=w2_scale,
        a1_scale=a1_scale,
        a2_scale=a2_scale,
        w1_bias=w1_bias,
        w2_bias=w2_bias,
        per_act_token_quant=False,
        per_out_ch_quant=False,
        block_shape=block_shape,
        gemm1_alpha=gemm1_alpha,
        gemm1_beta=gemm1_beta,
        gemm1_clamp_limit=gemm1_clamp_limit,
    )
```