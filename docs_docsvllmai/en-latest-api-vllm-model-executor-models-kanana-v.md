---
title: kanana_v - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/kanana_v/
source: sitemap
fetched_at: 2026-05-07T21:31:09.968913808-03:00
rendered_js: false
word_count: 0
summary: This document defines the ClassDynamicCAbstractor, a PyTorch module used for processing visual embeddings in Qwen2-VL, utilizing RegNet blocks and patch merging to transform input features.
tags:
    - pytorch
    - vision-transformer
    - feature-extraction
    - qwen2-vl
    - deep-learning
    - computer-vision
category: reference
---

```
classDynamicCAbstractor(nn.Module):
"""Dynamic C-Abstractor based on RegNet blocks."""

    def__init__(
        self,
        config: Qwen2VLVisionConfig,
        num_input_tokens: int,
    ) -> None:
        super().__init__()
        assert hasattr(config, "merge_size"), "merge_size must be provided."
        self.config = config
        self.merge_size = config.merge_size
        self.pos_emb_size = config.pos_emb_size
        if num_input_tokens == -1:
            num_input_tokens = config.pos_emb_size
        self.num_input_tokens = num_input_tokens
        self.pos_emb = build_pos_embeds(
            config, num_input_tokens, config.encoder_hidden_size
        )
        self.build_net()

    def_load_from_state_dict(self, state_dict, *args, **kwargs) -> None:
        if not state_dict:
            return

        if self.pos_emb is not None:
            key_re = re.compile(r"[\w,.]*abstractor[\w,.]*pos_emb")
            pos_emb_key = None
            for key in state_dict:
                if key_re.match(key):
                    pos_emb_key = key
                    break

            assert pos_emb_key is not None
            # update old ckpt compatible with current code
            pos_emb = state_dict[pos_emb_key]
            if pos_emb.size(1) == self.pos_emb.size(1) + 1:
                # remove obsolete first pos emb (for cls token originally)
                state_dict[pos_emb_key] = pos_emb[:, 1:]

        super()._load_from_state_dict(state_dict, *args, **kwargs)

    defbuild_net(self) -> None:
        encoder_hidden_size = self.config.encoder_hidden_size
        hidden_size = self.config.hidden_size
        output_hidden_size = self.config.output_hidden_size
        depth = self.config.depth
        mlp_depth = self.config.mlp_depth

        RegBlock = partial(
            RegStage,
            stride=1,
            dilation=1,
            act_layer=nn.SiLU,
            norm_layer=LayerNorm2d,
        )

        s1 = RegBlock(
            depth,
            encoder_hidden_size,
            hidden_size,
        )
        sampler = PatchMerge(merge_size=self.merge_size)
        s2 = RegBlock(
            depth,
            self.merge_size**2 * hidden_size,
            hidden_size,
        )

        if depth:
            self.net = nn.ModuleList([s1, sampler, s2])
            self.readout = build_mlp(mlp_depth, hidden_size, output_hidden_size)
        else:
            self.net = sampler
            self.readout = build_mlp(mlp_depth, encoder_hidden_size, output_hidden_size)

    defforward(
        self,
        flattened_visual_embeds: torch.Tensor,
        grid_thw: torch.Tensor,
        **unused_kwargs: object,
    ) -> BaseModelOutput:
"""Apply the dynamic abstractor over flattened visual embeddings."""
        n_token_loc = torch.prod(grid_thw, dim=1)
        split_visual_embeds = torch.split(flattened_visual_embeds, n_token_loc.tolist())

        flattened_visual_embeds = []
        for _visual_embeds, _grid_thw in zip(split_visual_embeds, grid_thw):
            T, H, W = _grid_thw
            assert T == 1, "T must be 1. Video is not supported yet."
            reshaped_visual_embeds = rearrange(
                _visual_embeds, "(t h w) d -> 1 t h w d", t=T, h=H, w=W
            )
            # remove temporal dim
            reshaped_visual_embeds = reshaped_visual_embeds[:, 0]

            if self.pos_emb is not None:
                # interpolate pos emb and add to visual embeds
                _local_pos_emb = resample_abs_pos_embed(
                    posemb=self.pos_emb,
                    old_size=tuple([int(self.pos_emb_size**0.5)] * 2),
                    new_size=(H, W),
                    num_prefix_tokens=0,
                )
                _local_pos_emb = rearrange(
                    _local_pos_emb,
                    "1 (h w) d -> 1 h w d",
                    h=H,
                    w=W,
                )
                reshaped_visual_embeds = reshaped_visual_embeds + _local_pos_emb

            reshaped_visual_embeds = self._forward(
                reshaped_visual_embeds,
                input_size=(H, W),
            )
            flattened_visual_embeds.append(reshaped_visual_embeds)
        reshaped_visual_embeds = torch.cat(flattened_visual_embeds, dim=0)
        return BaseModelOutput(last_hidden_state=reshaped_visual_embeds)

    def_forward(
        self,
        x: torch.Tensor,
        input_size: tuple[int, int],
    ) -> torch.Tensor:
        h, w = input_size
        x = rearrange(x, "1 h w d -> 1 d h w", h=h, w=w)
        if self.config.depth:
            x = self.net[0](x)
            x = self.net[1](x)
            x = self.net[2](x)
        else:
            # When depth=0, self.net is a single PatchMerge module
            x = self.net(x)
        x = rearrange(x, "1 d h w -> (h w) d")
        x = self.readout(x)
        return x
```