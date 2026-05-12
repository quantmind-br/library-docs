---
title: activation - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/activation/
source: sitemap
fetched_at: 2026-05-07T21:23:56.140757394-03:00
rendered_js: false
word_count: 13
summary: This document defines a custom PyTorch operation class that implements the xIELU activation function, supporting both a native Python fallback and an experimental CUDA-optimized version.
tags:
    - pytorch
    - activation-function
    - custom-op
    - cuda-optimization
    - deep-learning
    - xielu
category: api
---

```
@CustomOp.register("xielu")
classXIELU(CustomOp):
"""
    Applies the xIELU activation function introduced in https://arxiv.org/abs/2411.13010
    If the user has installed the nickjbrowning/XIELU, we import xIELU CUDA
    Otherwise, we emit a single warning and use xIELU Python
    """

    # --8<-- [end:xielu]

    def__init__(
        self,
        alpha_p_init: float = 0.8,
        alpha_n_init: float = 0.8,
        beta: float = 0.5,
        eps: float = -1e-6,
        dtype: torch.dtype = torch.bfloat16,
        with_vector_loads: bool = False,
    ):
        super().__init__()
        self.alpha_p = nn.Parameter(
            torch.log(torch.exp(torch.tensor(alpha_p_init, dtype=dtype)) - 1).unsqueeze(
                0
            )
        )
        self.alpha_n = nn.Parameter(
            torch.log(
                torch.exp(torch.tensor(alpha_n_init - beta, dtype=dtype)) - 1
            ).unsqueeze(0)
        )
        self.register_buffer("beta", torch.tensor(beta, dtype=dtype))
        self.register_buffer("eps", torch.tensor(eps, dtype=dtype))
        self.with_vector_loads = with_vector_loads
        # Temporary until xIELU CUDA fully implemented
        self._beta_scalar = float(self.beta.detach().cpu().float().item())
        self._eps_scalar = float(self.eps.detach().cpu().float().item())

        self._xielu_cuda_obj = None
        try:
            importxielu.ops  # noqa: F401

            self._xielu_cuda_obj = torch.classes.xielu.XIELU()
            msg = "Using experimental xIELU CUDA."
            try:
                fromtorch._dynamoimport allow_in_graph

                self._xielu_cuda_fn = allow_in_graph(self._xielu_cuda)
                msg += " Enabled torch._dynamo for xIELU CUDA."
            except Exception as err:
                msg += (
                    f" Could not enable torch._dynamo for xIELU ({err}) - "
                    "this may result in slower performance."
                )
                self._xielu_cuda_fn = self._xielu_cuda
            logger.warning_once(msg)
        except Exception as err:
            logger.warning_once(
                "CUDA-fused xIELU not available (%s) –"
                " falling back to a Python version.\n"
                "For CUDA xIELU (experimental), `pip install git+https://github.com/nickjbrowning/XIELU`",
                str(err),
            )

    def_xielu_python(self, x: torch.Tensor) -> torch.Tensor:
        alpha_p = nn.functional.softplus(self.alpha_p)
        alpha_n = self.beta + nn.functional.softplus(self.alpha_n)
        return torch.where(
            x > 0,
            alpha_p * x * x + self.beta * x,
            (torch.expm1(torch.min(x, self.eps)) - x) * alpha_n + self.beta * x,
        )

    def_xielu_cuda(self, x: torch.Tensor) -> torch.Tensor:
"""Firewall function to prevent torch.compile from seeing .item()"""
        assert self._xielu_cuda_obj is not None, "XIELU CUDA object must not be None"
        original_shape = x.shape
        # CUDA kernel expects 3D tensors, reshape if needed
        while x.dim() < 3:
            x = x.unsqueeze(0)
        if x.dim() > 3:
            x = x.view(-1, 1, x.size(-1))
        if original_shape != x.shape:
            logger.warning_once(
                "Warning: xIELU input tensor expects 3 dimensions"
                " but got (shape: %s). Reshaping to (shape: %s).",
                original_shape,
                x.shape,
            )
        result = self._xielu_cuda_obj.forward(
            x,
            self.alpha_p,
            self.alpha_n,
            # Temporary until xIELU CUDA fully implemented ->
            # self.{beta,eps}.item()
            self._beta_scalar,
            self._eps_scalar,
            self.with_vector_loads,
        )
        return result.view(original_shape)

    defforward_native(self, input: torch.Tensor) -> torch.Tensor:
        if self._xielu_cuda_obj is not None and input.is_cuda:
            if not torch._dynamo.is_compiling():
                return self._xielu_cuda_fn(input)
            else:
                logger.warning_once(
                    "torch._dynamo is compiling, using Python version of xIELU."
                )
        return self._xielu_python(input)

    defforward_cuda(self, input: torch.Tensor) -> torch.Tensor:
        return self.forward_native(input)
```