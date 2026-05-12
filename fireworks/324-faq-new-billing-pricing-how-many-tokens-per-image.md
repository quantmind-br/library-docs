---
title: How many tokens per image?
url: https://docs.fireworks.ai/faq-new/billing-pricing/how-many-tokens-per-image
source: sitemap
fetched_at: 2026-04-27T20:18:44.970229187-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
  - billing
  - tokens
  - vision-models
  - qwen
word_count: 87
---
# Token count per image

Image token consumption varies by model and resolution, typically ranging from **1,000 to 2,500 tokens** per image for common resolutions.

## Qwen2.5 VL token counts

| Resolution | Token Count |
|------------|-------------|
| 336×336    | 144         |
| 672×672    | 576         |
| 1024×1024  | 1,369       |
| 1280×720   | 1,196       |
| 1920×1080  | 2,769       |
| 2560×1440  | 4,641       |
| 3840×2160  | 10,549      |

## Calculating exact token count

Process your images through the model's tokenizer. For Qwen2.5 VL:

```python
# Use the tokenizer to get exact token counts
tokens = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True
)
```