---
title: colbert - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/
source: sitemap
fetched_at: 2026-05-07T21:29:24.014492496-03:00
rendered_js: false
word_count: 44
summary: This document defines the ColBERTMixin class, which provides utility methods for integrating ColBERT late interaction capabilities into existing neural network embedding models.
tags:
    - colbert
    - late-interaction
    - pytorch
    - embedding-models
    - mixin
    - weight-loading
category: reference
---

```
classColBERTMixin(nn.Module, SupportsLateInteraction):
"""Mixin that adds ColBERT late interaction support to any embedding model.

    ColBERT (Contextualized Late Interaction over BERT) uses per-token
    embeddings with a linear projection layer.  This mixin provides:

    - ColBERT linear projection initialisation / lazy creation
    - Weight loading helpers for the projection layer
    - A builder for the token-embedding pooler

    **Integration:**

    1. Inherit from both ``ColBERTMixin`` and ``nn.Module``.
    2. In ``__init__``: call ``super().__init__()``, then
       :meth:`_init_colbert_components`, then create ``self.model``
       (the backbone) and ``self.pooler`` via :meth:`_build_colbert_pooler`.
    3. In ``load_weights``: use :meth:`_load_colbert_weights` to separate
       the ColBERT projection weight, then delegate the rest to the backbone.
    """

    # Set during _init_colbert_components
    colbert_dim: int | None
    colbert_linear: nn.Linear | None
    hidden_size: int
    head_dtype: torch.dtype

    # ------------------------------------------------------------------ init

    def_init_colbert_components(
        self,
        hidden_size: int,
        colbert_dim: int | None,
        head_dtype: torch.dtype,
    ) -> None:
"""Initialise ColBERT projection layer.

        Args:
            hidden_size: Hidden dimension of the encoder backbone.
            colbert_dim: Output dimension for ColBERT embeddings.  If
                ``None``, will be inferred from weights during loading (or
                auto-loaded from sentence-transformers Dense layers).
            head_dtype: Data type for the projection layer.
        """
        self.hidden_size = hidden_size
        self.colbert_dim = colbert_dim
        self.head_dtype = head_dtype

        if colbert_dim is not None:
            self.colbert_linear = self._build_colbert_linear()
        else:
            self.colbert_linear = None

    def_build_colbert_linear(self) -> nn.Linear:
"""Build the ColBERT linear projection layer."""
        if self.colbert_dim is None:
            raise ValueError("colbert_dim must be set before building the linear layer")
        return nn.Linear(
            self.hidden_size,
            self.colbert_dim,
            bias=False,
            dtype=self.head_dtype,
        )

    # ---------------------------------------------------------------- pooler

    def_build_colbert_pooler(self, pooler_config: PoolerConfig) -> Pooler:
"""Build pooler for ColBERT token embeddings.

        When ``colbert_linear`` is set, it is used as the projector.
        Otherwise ``pooler_for_token_embed`` falls back to auto-loading
        sentence-transformers Dense layers (``1_Dense/`` etc.).
        """
        return pooler_for_token_embed(
            pooler_config,
            projector=self.colbert_linear,
        )

    # --------------------------------------------------------- config helper

    @classmethod
    defget_colbert_dim_from_config(cls, hf_config) -> int | None:
"""Extract ColBERT dimension from a HuggingFace config.

        Checks ``colbert_dim``, ``dim`` and ``projection_dim`` in that order.
        """
        return (
            getattr(hf_config, "colbert_dim", None)
            or getattr(hf_config, "dim", None)
            or getattr(hf_config, "projection_dim", None)
        )

    # -------------------------------------------------------- weight loading

    def_load_colbert_weights(
        self,
        weights: Iterable[tuple[str, torch.Tensor]],
        colbert_weight_names: tuple[str, ...] = (
            "linear.weight",
            "colbert_linear.weight",
        ),
    ) -> tuple[list[tuple[str, torch.Tensor]], set[str]]:
"""Separate and load ColBERT projection weights.

        Scans *weights* for entries whose name ends with one of
        *colbert_weight_names*.  The matching weight is loaded into
        ``self.colbert_linear`` (creating it first if ``colbert_dim`` was
        not known at init time).

        Args:
            weights: Iterable of ``(name, tensor)`` weight pairs.
            colbert_weight_names: Suffixes that identify the ColBERT linear
                weight.

        Returns:
            ``(remaining_weights, loaded_names)`` — the weights that were
            **not** consumed and the set of names that were loaded.
        """
        weights_list = list(weights)
        other_weights: list[tuple[str, torch.Tensor]] = []
        colbert_weight: tuple[str, torch.Tensor] | None = None

        for name, weight in weights_list:
            if any(name.endswith(cw) for cw in colbert_weight_names):
                colbert_weight = (name, weight)
            else:
                other_weights.append((name, weight))

        loaded: set[str] = set()
        if colbert_weight is not None:
            _name, weight = colbert_weight
            if weight.dim() == 2:
                # Infer colbert_dim from weight shape if not set
                if self.colbert_dim is None:
                    self.colbert_dim = weight.shape[0]
                    self.colbert_linear = self._build_colbert_linear()
                    # Update the pooler's projector
                    if hasattr(self, "pooler") and hasattr(self.pooler, "head"):
                        self.pooler.head.projector = self.colbert_linear

                assert self.colbert_linear is not None
                # Move to same device as model
                if hasattr(self, "model"):
                    device = next(self.model.parameters()).device
                    self.colbert_linear.to(device)

                weight = weight.to(self.colbert_linear.weight.device)
                self.colbert_linear.weight.data.copy_(weight)
                loaded.add("pooler.head.projector.weight")

        return other_weights, loaded
```