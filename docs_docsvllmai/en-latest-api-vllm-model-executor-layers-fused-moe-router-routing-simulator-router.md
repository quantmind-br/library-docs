---
title: routing_simulator_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/routing_simulator_router/
source: sitemap
fetched_at: 2026-05-07T21:25:35.389699561-03:00
rendered_js: false
word_count: 0
summary: This document defines a routing strategy that selects model experts for token processing using configurable probability distributions like uniform or normal.
tags:
    - mixture-of-experts
    - routing-strategy
    - probability-distribution
    - tensor-manipulation
    - machine-learning
category: api
---

```
classDistributionBasedRouting(RoutingStrategy):
"""
    Distribution-based random routing strategy with configurable distributions.

    This routing strategy randomly selects experts for each token based on
    different probability distributions. Currently supports uniform and normal
    distributions for testing different routing patterns.
    """

    def__init__(self, distribution: str = "uniform", **distribution_params: Any):
"""
        Initialize distribution-based routing.

        Args:
            distribution: Type of distribution to use for sampling
                - "uniform": Uniform distribution (default)
                - "normal": Normal/Gaussian distribution
            **distribution_params: Parameters specific to the
                chosen distribution
                For "uniform": No additional parameters needed
                For "normal": mean (default: 0.0), std (default: 1.0)
        """
        self.distribution = distribution.lower()
        self.distribution_params = distribution_params

        # Validate distribution and parameters
        self._validate_distribution_params()

    def_validate_distribution_params(self):
"""Validate distribution type and parameters."""
        valid_distributions = ["uniform", "normal"]

        if self.distribution not in valid_distributions:
            raise ValueError(
                f"Unsupported distribution: {self.distribution}. "
                f"Supported distributions: {valid_distributions}"
            )

        # Set default parameters if not provided
        if self.distribution == "normal":
            self.distribution_params.setdefault("mean", 0.0)
            self.distribution_params.setdefault("std", 1.0)

    defroute_tokens(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        top_k: int,
        indices_type: torch.dtype | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""
        Randomly select experts for each token using the specified distribution.

        Args:
            hidden_states: Input hidden states [num_tokens, hidden_size]
            router_logits: Router logits [num_tokens, num_experts]
            top_k: Number of experts to select per token
            indices_type: Data type for expert indices

        Returns:
            tuple of (topk_weights, topk_ids) where:
            - topk_weights: Weights based on distribution sampling
            - topk_ids: Expert indices sampled from the distribution
        """
        num_tokens = hidden_states.shape[0]
        num_experts = router_logits.shape[-1]

        if indices_type is None:
            indices_type = torch.long

        # Generate expert IDs based on the specified distribution
        topk_ids = self._sample_expert_ids(
            num_tokens, num_experts, top_k, hidden_states.device, indices_type
        )

        # Generate weights based on the distribution
        topk_weights = self._generate_weights(num_tokens, top_k, hidden_states.device)

        return topk_weights, topk_ids

    def_sample_expert_ids(
        self,
        num_tokens: int,
        num_experts: int,
        top_k: int,
        device: torch.device,
        indices_type: torch.dtype,
    ) -> torch.Tensor:
"""Sample expert IDs based on the specified distribution."""

        if self.distribution == "uniform":
            # Uniform random sampling
            return torch.randint(
                low=0,
                high=num_experts,
                size=(num_tokens, top_k),
                dtype=indices_type,
                device=device,
            )

        elif self.distribution == "normal":
            # For normal distribution, sample continuous values and map to
            # expert IDs
            continuous_samples = self._sample_continuous_distribution(
                num_tokens, top_k, device
            )

            # Map continuous samples to expert indices
            # Normalize to [0, 1] range and scale to [0, num_experts)
            normalized_samples = self._normalize_samples(continuous_samples)
            expert_ids = (normalized_samples * num_experts).long()
            expert_ids = torch.clamp(expert_ids, 0, num_experts - 1)

            return expert_ids.to(dtype=indices_type)

        else:
            raise ValueError(f"Unsupported distribution: {self.distribution}")

    def_sample_continuous_distribution(
        self, num_tokens: int, top_k: int, device: torch.device
    ) -> torch.Tensor:
"""Sample from continuous distributions."""
        shape = (num_tokens, top_k)

        if self.distribution == "normal":
            mean = self.distribution_params["mean"]
            std = self.distribution_params["std"]
            return torch.normal(mean, std, size=shape, device=device)

        else:
            raise ValueError(
                f"Unsupported continuous distribution: {self.distribution}"
            )

    def_normalize_samples(self, samples: torch.Tensor) -> torch.Tensor:
"""Normalize samples to [0, 1] range."""
        if self.distribution == "normal":
            # Use sigmoid to map normal distribution to [0, 1]
            return torch.sigmoid(samples)

        else:
            raise ValueError(
                f"Unsupported distribution for normalization: {self.distribution}"
            )

    def_generate_weights(
        self, num_tokens: int, top_k: int, device: torch.device
    ) -> torch.Tensor:
"""Generate weights based on the distribution."""
        if self.distribution == "uniform":
            # All-ones weights for uniform distribution
            return torch.ones(
                (num_tokens, top_k),
                dtype=torch.float32,
                device=device,
            )

        elif self.distribution == "normal":
            # For normal distribution, generate weights from the same
            # distribution
            continuous_weights = self._sample_continuous_distribution(
                num_tokens, top_k, device
            )
            # Normalize to positive values and sum to 1
            weights = torch.abs(continuous_weights)
            weights = weights / weights.sum(dim=-1, keepdim=True)
            return weights

        else:
            raise ValueError(
                f"Unsupported distribution for weight generation: {self.distribution}"
            )

    defget_distribution_info(self) -> dict:
"""Get information about the current distribution configuration."""
        return {
            "distribution": self.distribution,
            "parameters": self.distribution_params.copy(),
        }
```