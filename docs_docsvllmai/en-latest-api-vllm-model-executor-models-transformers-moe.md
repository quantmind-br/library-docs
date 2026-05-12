---
title: moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/moe/
source: sitemap
fetched_at: 2026-05-07T21:33:36.745406214-03:00
rendered_js: false
word_count: 8
summary: This document defines the ClassMoEMixin for handling Mixture-of-Experts (MoE) model architectures, providing methods for managing expert state, weight mapping, and recursive replacement of standard layers with optimized FusedMoE implementations.
tags:
    - mixture-of-experts
    - model-parallelism
    - fused-moe
    - pytorch-mixin
    - weight-loading
    - deep-learning-architecture
category: api
---

```
classMoEMixin(MixtureOfExperts):
    def__init__(self, *, vllm_config: "VllmConfig", prefix: str = ""):
        self.check_version("5.0.0", "MoE models support")
        # Skip MixtureOfExperts.__init__ and call the next class in MRO
        super(MixtureOfExperts, self).__init__(vllm_config=vllm_config, prefix=prefix)

    defset_eplb_state(
        self,
        expert_load_view: torch.Tensor,
        logical_to_physical_map: torch.Tensor,
        logical_replica_count: torch.Tensor,
    ):
        for moe_layer_idx, mlp_layer in enumerate(self.mlp_moe_layers):
            mlp_layer.experts.set_eplb_state(
                moe_layer_idx=moe_layer_idx,
                expert_load_view=expert_load_view,
                logical_to_physical_map=logical_to_physical_map,
                logical_replica_count=logical_replica_count,
            )

    defupdate_physical_experts_metadata(
        self,
        num_physical_experts: int,
        num_local_physical_experts: int,
    ):
        assert self.num_local_physical_experts == num_local_physical_experts
        self.num_physical_experts = num_physical_experts
        self.num_local_physical_experts = num_local_physical_experts
        self.num_redundant_experts = num_physical_experts - self.num_logical_experts
        for mlp in self.mlp_moe_layers:
            mlp.n_local_physical_experts = num_local_physical_experts
            mlp.n_physical_experts = num_physical_experts
            mlp.n_redundant_experts = self.num_redundant_experts
            mlp.experts.update_expert_map()

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
"""
        Params for weights, fp8 weight scales, fp8 activation scales
        (param_name, weight_name, expert_id, shard_id)
        """
        # Models saved with fused experts. These are checkpoints released:
        # - After Transformers v5
        # - Before Transformers v5, but re-saved with save_original_format=False
        # In the fused experts case, we repurpose the expert_id as shard_idx for
        # deconcatenating w1 and w3 in FusedMoE.load_weights.
        expert_mapping = [
            ("experts.w13_weight", "experts.gate_up_proj", 0, "w1"),
            ("experts.w13_weight", "experts.gate_up_proj", 1, "w3"),
            ("experts.w2_weight", "experts.down_proj", 0, "w2"),
        ]
        # Models saved with ModuleList experts
        ckpt_names = [
            # (ckpt_gate_proj_name, ckpt_down_proj_name, ckpt_up_proj_name)
            ("gate_proj", "down_proj", "up_proj"),  # Most common MoE style
            ("w1", "w2", "w3"),  # Granite, Mixtral, Phi MoE style
            ("linear", "linear_1", "linear_v"),  # Grok1 style
        ]
        num_experts = self.model_config.get_num_experts()
        num_redundant_experts = self.parallel_config.eplb_config.num_redundant_experts
        for gate_proj, down_proj, up_proj in ckpt_names:
            expert_mapping.extend(
                fused_moe_make_expert_params_mapping(
                    self,
                    ckpt_gate_proj_name=gate_proj,
                    ckpt_down_proj_name=down_proj,
                    ckpt_up_proj_name=up_proj,
                    num_experts=num_experts,
                    num_redundant_experts=num_redundant_experts,
                )
            )
        return expert_mapping

    defrecursive_replace(self):
"""Initialize the MoE layers."""
        text_config = self.text_config

        # Positional arguments
        num_experts = self.model_config.get_num_experts()
        top_k = getattr_iter(text_config, ["num_experts_per_tok", "top_k"], None)
        assert top_k is not None
        hidden_size = text_config.hidden_size
        intermediate_size = getattr_iter(
            text_config, ["moe_intermediate_size", "intermediate_size"], None
        )
        assert intermediate_size is not None

        num_shared_experts = getattr_iter(
            text_config,
            [
                "n_shared_experts",  # DeepSeek, Docs, GLM
                "moe_num_shared_experts",  # Aria, Ernie
            ],
            0,
        )

        # Unused kwargs since we use custom_routing_function:
        # - `scoring_func` and `e_score_correction_bias` only used for grouped
        #    topk routing inside vLLM and are non-trivial to infer
        #    and hard code `use_grouped_topk=False`
        # - `renormalize` passed anyway because it's easy to infer
        # - `num_expert_group` and `topk_group` used for inferring expert
        #    placement strategy in FusedMoE
        # - `apply_router_weight_on_input` is already applied in Transformers
        renormalize = getattr(text_config, "norm_topk_prob", top_k > 1)
        num_expert_group = getattr(text_config, "n_group", None)
        topk_group = getattr(text_config, "topk_group", None)

        # MoE activation function
        activation = "silu"
        wrapped_arch = self.config.architectures[0].lower()
        if "gptoss" in wrapped_arch:
            activation = "swigluoai"
        elif "grok1" in wrapped_arch:
            activation = "gelu"

        # Expert mapping for `AutoWeightsLoader`
        expert_mapping = self.get_expert_mapping()

        # Expert parallel load balancing kwargs
        enable_eplb = self.parallel_config.enable_eplb
        num_redundant_experts = self.parallel_config.eplb_config.num_redundant_experts

        # MixtureOfExperts mixin settings
        ep_size = get_ep_group().world_size

        self.mlp_moe_layers = []  # Used for MixtureOfExperts methods
        self.moe_layers = []
        self.expert_weights = []
        self.num_moe_layers = 0
        self.num_expert_groups = 1 if num_expert_group is None else num_expert_group
        self.num_logical_experts = num_experts
        self.num_physical_experts = num_experts + num_redundant_experts
        self.num_local_physical_experts = self.num_physical_experts // ep_size
        self.num_routed_experts = num_experts
        self.num_shared_experts = num_shared_experts
        self.num_redundant_experts = num_redundant_experts

        # Recursively fuse MoE layers
        def_recursive_replace(module: nn.Module, prefix: str):
            for child_name, child_module in module.named_children():
                qual_name = maybe_prefix(prefix, child_name)
                # Naive implementations will have experts as ModuleList
                is_modulelist = isinstance(child_module, nn.ModuleList)
                # Packed implementations will have experts as 3D tensors of shapes like:
                # gate_up_proj = (num_experts, 2 * intermediate_size, hidden_size)
                # down_proj = (num_experts, intermediate_size, hidden_size)
                params = list(child_module.parameters())
                is_3d = len(params) > 0 and all(p.ndim == 3 for p in params)
                if child_name == "experts" and (is_modulelist or is_3d):
                    # Alias for readability
                    mlp = module
                    experts = child_module
                    # Do the experts have biases
                    has_bias = False
                    for experts_param_name, _ in experts.named_parameters():
                        if "bias" in experts_param_name:
                            has_bias = True
                            break
                    # If the config does not specify num_shared_experts, but
                    # the model has shared experts, we assume there is one.
                    if self.num_shared_experts == 0:
                        for mlp_param_name, _ in mlp.named_parameters():
                            if "shared_expert" in mlp_param_name:
                                self.num_shared_experts = 1
                                break
                    # Replace experts module with FusedMoE
                    fused_experts = TransformersFusedMoE(
                        num_experts=num_experts,
                        top_k=top_k,
                        hidden_size=hidden_size,
                        intermediate_size=intermediate_size,
                        renormalize=renormalize,
                        # Hard coded because topk happens in Transformers
                        use_grouped_topk=False,
                        num_expert_group=num_expert_group,
                        topk_group=topk_group,
                        quant_config=self.quant_config,
                        prefix=qual_name,
                        activation=activation,
                        enable_eplb=enable_eplb,
                        num_redundant_experts=num_redundant_experts,
                        has_bias=has_bias,
                        expert_mapping=expert_mapping,
                    )
                    mlp.experts = fused_experts
                    log_replacement(qual_name, experts, fused_experts)
                    # Update MixtureOfExperts mixin state
                    self.mlp_moe_layers.append(mlp)
                    self.moe_layers.append(fused_experts)
                    self.expert_weights.append(fused_experts.get_expert_weights())
                    self.num_moe_layers += 1
                else:
                    _recursive_replace(child_module, prefix=qual_name)

        _recursive_replace(self.model, prefix="model")
        # Continue with the replacement of layers in Base
        super().recursive_replace()
```