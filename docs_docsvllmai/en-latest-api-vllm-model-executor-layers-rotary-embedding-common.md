---
title: common - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/common/
source: sitemap
fetched_at: 2026-05-07T21:28:13.936904129-03:00
rendered_js: false
word_count: 0
summary: This document defines a custom operator class for applying Rotary Positional Embeddings (RoPE) to input tensors, supporting both native PyTorch computations and hardware-accelerated kernels.
tags:
    - rotary-embeddings
    - pytorch-custom-op
    - deep-learning
    - attention-mechanisms
    - tensor-manipulation
category: api
---

```
@CustomOp.register("apply_rotary_emb")
classApplyRotaryEmb(CustomOp):
    # --8<-- [end:apply_rotary_emb]

    def__init__(
        self,
        enforce_enable: bool = False,
        is_neox_style: bool = True,
        enable_fp32_compute: bool = False,
    ) -> None:
        super().__init__(enforce_enable=enforce_enable)
        self.is_neox_style = is_neox_style
        self.enable_fp32_compute = enable_fp32_compute

        self.apply_rotary_emb_flash_attn = None
        if find_spec("flash_attn") is not None:
            fromflash_attn.ops.triton.rotaryimport apply_rotary

            self.apply_rotary_emb_flash_attn = apply_rotary

    @staticmethod
    defforward_static(
        x: torch.Tensor,
        cos: torch.Tensor,
        sin: torch.Tensor,
        is_neox_style: bool = True,
        enable_fp32_compute: bool = False,
    ) -> torch.Tensor:
"""
        Args:
            x: [batch_size (optional), seq_len, num_heads, head_size]
            cos: [seq_len, head_size // 2]
            sin: [seq_len, head_size // 2]
            is_neox_style: Whether to use the Neox-style or GPT-J-style.
            enable_fp32_compute: Temporarily convert x, cos, sin to FP32 dtype
                                 for higher accuracy.
        """
        origin_dtype = x.dtype
        if enable_fp32_compute:
            x = x.float()

        cos = cos.unsqueeze(-2).to(x.dtype)
        sin = sin.unsqueeze(-2).to(x.dtype)

        if is_neox_style:
            x1, x2 = torch.chunk(x, 2, dim=-1)
        else:
            x1 = x[..., ::2]
            x2 = x[..., 1::2]

        o1 = x1 * cos - x2 * sin
        o2 = x2 * cos + x1 * sin

        if is_neox_style:
            output = torch.cat((o1, o2), dim=-1)
        else:
            output = torch.stack((o1, o2), dim=-1).flatten(-2)

        if enable_fp32_compute:
            output = output.to(origin_dtype)
        return output

    def_pre_process(
        self,
        x: torch.Tensor,
        cos: torch.Tensor,
        sin: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Size, torch.dtype]:
        origin_shape = x.shape
        if len(origin_shape) == 3:
            # x: [seq_len, num_heads, head_size]
            x = x.unsqueeze(0)

        origin_dtype = x.dtype
        if self.enable_fp32_compute:
            x = x.float()
            cos = cos.float()
            sin = sin.float()

        return x, cos, sin, origin_shape, origin_dtype

    def_post_process(
        self,
        output: torch.Tensor,
        origin_shape: torch.Size,
        origin_dtype: torch.dtype,
    ) -> torch.Tensor:
        if len(origin_shape) == 3:
            output = output.squeeze(0)
        if self.enable_fp32_compute:
            output = output.to(origin_dtype)
        return output

    defforward_native(
        self,
        x: torch.Tensor,
        cos: torch.Tensor,
        sin: torch.Tensor,
    ) -> torch.Tensor:
        output = self.forward_static(
            x, cos, sin, self.is_neox_style, self.enable_fp32_compute
        )
        return output

    defforward_cuda(
        self,
        x: torch.Tensor,
        cos: torch.Tensor,
        sin: torch.Tensor,
    ) -> torch.Tensor:
        fromvllm.vllm_flash_attn.layers.rotaryimport apply_rotary_emb

        x, cos, sin, origin_shape, origin_dtype = self._pre_process(x, cos, sin)

"""
        Arguments of apply_rotary_emb() in vllm_flash_attn:
            x: [batch_size, seq_len, nheads, headdim]
            cos, sin: [seqlen_rotary, rotary_dim / 2]
            interleaved: default as False (Neox-style).
            ...
        """
        interleaved = not self.is_neox_style
        output = apply_rotary_emb(x, cos, sin, interleaved)

        output = self._post_process(output, origin_shape, origin_dtype)
        return output

    defforward_hip(
        self,
        x: torch.Tensor,
        cos: torch.Tensor,
        sin: torch.Tensor,
    ) -> torch.Tensor:
        if self.apply_rotary_emb_flash_attn is not None:
            x, cos, sin, origin_shape, origin_dtype = self._pre_process(x, cos, sin)

"""
            Arguments of apply_rotary() in flash_attn:
                x: [batch_size, seq_len, nheads, headdim]
                cos, sin: [seqlen_rotary, rotary_dim / 2]
                interleaved: default as False (Neox-style).
                ...
            """
            interleaved = not self.is_neox_style
            output = self.apply_rotary_emb_flash_attn(
                x, cos, sin, interleaved=interleaved
            ).type_as(x)

            output = self._post_process(output, origin_shape, origin_dtype)
        else:
            # Falling back to PyTorch native implementation.
            output = self.forward_native(x, cos, sin)

        return output

    defforward_cpu(
        self,
        x: torch.Tensor,
        cos: torch.Tensor,
        sin: torch.Tensor,
    ) -> torch.Tensor:
        # TODO (bigPYJ1151): need to enable fused CPU ROPE here
        return self.forward_native(x, cos, sin)

    defextra_repr(self) -> str:
        s = f"is_neox_style={self.is_neox_style}"
        s += f", enable_fp32_compute={self.enable_fp32_compute}"
        return s
```