---
title: Image Generation | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation
source: crawler
fetched_at: 2026-04-24T17:00:08.702948729-03:00
rendered_js: false
word_count: 635
summary: This document serves as a technical reference guide for Hermes Agent's image generation capabilities via FAL.ai, detailing the supported models, configuration methods, aspect ratio mapping, automatic upscaling settings, and internal request workflow.
tags:
    - image-generation
    - fal-ai
    - hermes-agent
    - model-selection
    - api-integration
    - config-yaml
category: reference
---

Hermes Agent generates images from text prompts via FAL.ai. Nine models are supported out of the box, each with different speed, quality, and cost tradeoffs. The active model is user-configurable via `hermes tools` and persists in `config.yaml`.

## Supported Models[​](#supported-models "Direct link to Supported Models")

ModelSpeedStrengthsPrice`fal-ai/flux-2/klein/9b` *(default)*`<1s`Fast, crisp text$0.006/MP`fal-ai/flux-2-pro`~6sStudio photorealism$0.03/MP`fal-ai/z-image/turbo`~2sBilingual EN/CN, 6B params$0.005/MP`fal-ai/nano-banana-pro`~8sGemini 3 Pro, reasoning depth, text rendering$0.15/image (1K)`fal-ai/gpt-image-1.5`~15sPrompt adherence$0.034/image`fal-ai/gpt-image-2`~20sSOTA text rendering + CJK, world-aware photorealism$0.04–0.06/image`fal-ai/ideogram/v3`~5sBest typography$0.03–0.09/image`fal-ai/recraft/v4/pro/text-to-image`~8sDesign, brand systems, production-ready$0.25/image`fal-ai/qwen-image`~12sLLM-based, complex text$0.02/MP

Prices are FAL's pricing at time of writing; check [fal.ai](https://fal.ai/) for current numbers.

## Setup[​](#setup "Direct link to Setup")

Nous Subscribers

If you have a paid [Nous Portal](https://portal.nousresearch.com) subscription, you can use image generation through the [**Tool Gateway**](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway) without a FAL API key. Your model selection persists across both paths.

If the managed gateway returns `HTTP 4xx` for a specific model, that model isn't yet proxied on the portal side — the agent will tell you so, with remediation steps (set `FAL_KEY` for direct access, or pick a different model).

### Get a FAL API Key[​](#get-a-fal-api-key "Direct link to Get a FAL API Key")

1. Sign up at [fal.ai](https://fal.ai/)
2. Generate an API key from your dashboard

### Configure and Pick a Model[​](#configure-and-pick-a-model "Direct link to Configure and Pick a Model")

Run the tools command:

Navigate to **🎨 Image Generation**, pick your backend (Nous Subscription or FAL.ai), then the picker shows all supported models in a column-aligned table — arrow keys to navigate, Enter to select:

```text
  Model                          Speed    Strengths                    Price
  fal-ai/flux-2/klein/9b         <1s      Fast, crisp text             $0.006/MP   ← currently in use
  fal-ai/flux-2-pro              ~6s      Studio photorealism          $0.03/MP
  fal-ai/z-image/turbo           ~2s      Bilingual EN/CN, 6B          $0.005/MP
  ...
```

Your selection is saved to `config.yaml`:

```yaml
image_gen:
model: fal-ai/flux-2/klein/9b
use_gateway:false# true if using Nous Subscription
```

### GPT-Image Quality[​](#gpt-image-quality "Direct link to GPT-Image Quality")

The `fal-ai/gpt-image-1.5` and `fal-ai/gpt-image-2` request quality is pinned to `medium` (~$0.034–$0.06/image at 1024×1024). We don't expose the `low` / `high` tiers as a user-facing option so that Nous Portal billing stays predictable across all users — the cost spread between tiers is 3–22×. If you want a cheaper option, pick Klein 9B or Z-Image Turbo; if you want higher quality, use Nano Banana Pro or Recraft V4 Pro.

## Usage[​](#usage "Direct link to Usage")

The agent-facing schema is intentionally minimal — the model picks up whatever you've configured:

```text
Generate an image of a serene mountain landscape with cherry blossoms
```

```text
Create a square portrait of a wise old owl — use the typography model
```

```text
Make me a futuristic cityscape, landscape orientation
```

## Aspect Ratios[​](#aspect-ratios "Direct link to Aspect Ratios")

Every model accepts the same three aspect ratios from the agent's perspective. Internally, each model's native size spec is filled in automatically:

Agent inputimage\_size (flux/z-image/qwen/recraft/ideogram)aspect\_ratio (nano-banana-pro)image\_size (gpt-image-1.5)image\_size (gpt-image-2)`landscape``landscape_16_9``16:9``1536x1024``landscape_4_3` (1024×768)`square``square_hd``1:1``1024x1024``square_hd` (1024×1024)`portrait``portrait_16_9``9:16``1024x1536``portrait_4_3` (768×1024)

GPT Image 2 maps to 4:3 presets rather than 16:9 because its minimum pixel count is 655,360 — the `landscape_16_9` preset (1024×576 = 589,824) would be rejected.

This translation happens in `_build_fal_payload()` — agent code never has to know about per-model schema differences.

## Automatic Upscaling[​](#automatic-upscaling "Direct link to Automatic Upscaling")

Upscaling via FAL's **Clarity Upscaler** is gated per-model:

ModelUpscale?Why`fal-ai/flux-2-pro`✓Backward-compat (was the pre-picker default)All others✗Fast models would lose their sub-second value prop; hi-res models don't need it

When upscaling runs, it uses these settings:

SettingValueUpscale factor2×Creativity0.35Resemblance0.6Guidance scale4Inference steps18

If upscaling fails (network issue, rate limit), the original image is returned automatically.

## How It Works Internally[​](#how-it-works-internally "Direct link to How It Works Internally")

1. **Model resolution** — `_resolve_fal_model()` reads `image_gen.model` from `config.yaml`, falls back to the `FAL_IMAGE_MODEL` env var, then to `fal-ai/flux-2/klein/9b`.
2. **Payload building** — `_build_fal_payload()` translates your `aspect_ratio` into the model's native format (preset enum, aspect-ratio enum, or GPT literal), merges the model's default params, applies any caller overrides, then filters to the model's `supports` whitelist so unsupported keys are never sent.
3. **Submission** — `_submit_fal_request()` routes via direct FAL credentials or the managed Nous gateway.
4. **Upscaling** — runs only if the model's metadata has `upscale: True`.
5. **Delivery** — final image URL returned to the agent, which emits a `MEDIA:<url>` tag that platform adapters convert to native media.

## Debugging[​](#debugging "Direct link to Debugging")

Enable debug logging:

```bash
exportIMAGE_TOOLS_DEBUG=true
```

Debug logs go to `./logs/image_tools_debug_<session_id>.json` with per-call details (model, parameters, timing, errors).

## Platform Delivery[​](#platform-delivery "Direct link to Platform Delivery")

PlatformDelivery**CLI**Image URL printed as markdown `![](url)` — click to open**Telegram**Photo message with the prompt as caption**Discord**Embedded in a message**Slack**URL unfurled by Slack**WhatsApp**Media message**Others**URL in plain text

## Limitations[​](#limitations "Direct link to Limitations")

- **Requires FAL credentials** (direct `FAL_KEY` or Nous Subscription)
- **Text-to-image only** — no inpainting, img2img, or editing via this tool
- **Temporary URLs** — FAL returns hosted URLs that expire after hours/days; save locally if needed
- **Per-model constraints** — some models don't support `seed`, `num_inference_steps`, etc. The `supports` filter silently drops unsupported params; this is expected behavior