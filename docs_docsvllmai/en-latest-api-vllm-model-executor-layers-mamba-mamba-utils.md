---
title: mamba_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/mamba_utils/
source: sitemap
fetched_at: 2026-05-07T21:25:58.231706988-03:00
rendered_js: false
word_count: 0
summary: This document defines a utility class for calculating the tensor shapes of recurrent neural network states, specifically for Mamba architectures and gated delta networks in parallelized training environments.
tags:
    - mamba
    - tensor-shapes
    - deep-learning
    - parallel-computing
    - model-architecture
    - distributed-training
category: reference
---

```
classMambaStateShapeCalculator:
    @classmethod
    deflinear_attention_state_shape(
        cls,
        num_heads: int,
        tp_size: int,
        head_dim: int,
    ) -> tuple[tuple[int, int, int], ...]:
        state_shape = (num_heads // tp_size, head_dim, head_dim)
        return (state_shape,)

    @staticmethod
    def_orient_conv_shape(dim: int, state_len: int) -> tuple[int, int]:
"""Return (dim, state_len) for DS layout, (state_len, dim) for SD."""
        if is_conv_state_dim_first():
            return (dim, state_len)
        return (state_len, dim)

    @classmethod
    defmamba1_state_shape(
        cls,
        tp_world_size: int,
        intermediate_size: int,
        state_size: int,
        conv_kernel: int,
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        conv_dim = divide(intermediate_size, tp_world_size)
        conv_state_shape = cls._orient_conv_shape(conv_dim, conv_kernel - 1)

        temporal_state_shape = (divide(intermediate_size, tp_world_size), state_size)

        return conv_state_shape, temporal_state_shape

    @classmethod
    defmamba2_state_shape(
        cls,
        tp_world_size: int,
        intermediate_size: int,
        n_groups: int,
        num_heads: int,
        head_dim: int,
        state_size: int,
        conv_kernel: int,
        num_spec: int = 0,
    ) -> tuple[tuple[int, int], tuple[int, int, int]]:
        # if n_groups is not divisible by world_size, need to extend the shards
        # to ensure all groups needed by a head is sharded along with it
        n_groups = n_groups + cls.extra_groups_for_head_shards(n_groups, tp_world_size)
        # heads and n_groups are TP-ed
        conv_dim = intermediate_size + 2 * n_groups * state_size

        conv_state_shape = cls._orient_conv_shape(
            divide(conv_dim, tp_world_size), conv_kernel - 1 + num_spec
        )

        # These are not TP-ed as they depend on A, dt_bias, D
        # - they are typically small
        #   e.g., (h_heads, head_dim, state_size) = (128, 64, 128)
        temporal_state_shape = (divide(num_heads, tp_world_size), head_dim, state_size)
        return conv_state_shape, temporal_state_shape

    @classmethod
    defshort_conv_state_shape(
        cls,
        tp_world_size: int,
        intermediate_size: int,
        conv_kernel: int,
    ) -> tuple[tuple[int, int]]:
        conv_dim = divide(intermediate_size, tp_world_size)
        conv_state_shape = cls._orient_conv_shape(conv_dim, conv_kernel - 1)
        return (conv_state_shape,)

    @classmethod
    defextra_groups_for_head_shards(cls, ngroups: int, tp_size: int):
"""Compute the increase in group numbers to account for
        replication in order to accompany the head shards."""

        # in the case ngoups % tp_size == 0, this will be zero
        if ngroups % tp_size == 0:
            return 0

        # for n_groups == 1, this is exactly tp_size - n_groups
        return tp_size - ngroups

    @classmethod
    defgated_delta_net_state_shape(
        cls,
        tp_world_size: int,
        num_k_heads: int,
        num_v_heads: int,
        head_k_dim: int,
        head_v_dim: int,
        conv_kernel_size: int,
        num_spec: int = 0,
    ):
        conv_dim = head_k_dim * num_k_heads * 2 + head_v_dim * num_v_heads
        conv_state_shape = cls._orient_conv_shape(
            divide(conv_dim, tp_world_size),
            conv_kernel_size - 1 + num_spec,
        )

        temporal_state_shape = (
            divide(num_v_heads, tp_world_size),
            head_v_dim,
            head_k_dim,
        )
        return conv_state_shape, temporal_state_shape

    @classmethod
    defkda_state_shape(
        cls,
        tp_world_size: int,
        num_heads: int,
        head_dim: int,
        num_k_heads: int | None = None,
        head_k_dim: int | None = None,
        conv_kernel_size: int = 4,
        num_spec: int = 0,
    ) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int, int]]:
        if num_k_heads is None:
            num_k_heads = num_heads
        if head_k_dim is None:
            head_k_dim = head_dim

        proj_size = num_heads * head_dim
        proj_k_size = num_k_heads * head_k_dim

        conv_state_shape = cls._orient_conv_shape(
            divide(proj_size, tp_world_size), conv_kernel_size - 1
        )
        conv_state_k_shape = cls._orient_conv_shape(
            divide(proj_k_size, tp_world_size), conv_kernel_size - 1
        )
        recurrent_state_shape = (divide(num_heads, tp_world_size), head_dim, head_dim)
        return (
            conv_state_shape,
            conv_state_k_shape,
            conv_state_k_shape,
            recurrent_state_shape,
        )
```