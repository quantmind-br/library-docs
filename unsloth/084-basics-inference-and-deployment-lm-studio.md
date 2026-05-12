---
title: Deploying models to LM Studio
url: https://unsloth.ai/docs/basics/inference-and-deployment/lm-studio.md
source: llms
fetched_at: 2026-04-27T18:14:48.035758498-03:00
rendered_js: false
word_count: 836
summary: Deploy fine-tuned GGUF models via LM Studio with OpenAI-compatible local API.
tags:
    - lm-studio
    - llm-deployment
    - gguf
    - model-serving
    - unsloth
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Deploying models to LM Studio

Deploy fine-tuned GGUF models (llama.cpp format) via [LM Studio](https://lmstudio.ai/). Workflow: export GGUF -> import -> load/chat -> serve as OpenAI-compatible API.

See the [LM Studio notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/FunctionGemma_\(270M\)-LMStudio.ipynb) or follow steps below.

## 1) Export to GGUF

```python
# Save locally
model.save_pretrained_gguf("my_model_gguf", tokenizer, quantization_method = "q4_k_m")
# model.save_pretrained_gguf("my_model_gguf", tokenizer, quantization_method = "q8_0")
# model.save_pretrained_gguf("my_model_gguf", tokenizer, quantization_method = "f16")

# Or push to Hugging Face Hub
model.push_to_hub_gguf("hf_username/my_model_gguf", tokenizer, quantization_method = "q4_k_m")
```

> [!info] Quantization defaults
> - `q4_k_m` — default for local runs
> - `q8_0` — optimum for near full precision quality
> - `f16` — largest/slowest, original unquantized precision

## 2) Import GGUF into LM Studio

### CLI import (`lms import`)

```bash
lms import /path/to/model.gguf
```

| Flag | Behavior |
|------|----------|
| `--copy` | Keep original file (copy instead of move) |
| `--symbolic-link` | Symlink (useful for large models on dedicated drives) |
| `--user-repo my-user/my-finetuned-models` | Skip prompts, choose target namespace |
| `--dry-run` | Preview without importing |

Model appears under **My Models** after import.

### From Hugging Face

**In-app:** Discover tab -> search `hf_username/repo_name` -> download quant.

**CLI:**

```bash
lms get hf_username/my_model_gguf
lms get hf_username/my_model_gguf@Q4_K_M  # pick quantization
```

### Manual import

Place `.gguf` into LM Studio's expected structure:

```
~/.lmstudio/models/
└── publisher/
    └── model/
        └── model-file.gguf
```

Example:

```
~/.lmstudio/models/
└── my-name/
    └── my-finetune/
        └── my-finetune-Q4_K_M.gguf
```

## 3) Load and chat

1. LM Studio -> **Chat**
2. Open **model loader**
3. Select imported model
4. (Optional) adjust GPU offload, context length, etc.
5. Chat normally

## 4) Serve as local OpenAI-compatible API

### GUI

Load model -> **Developer** tab -> start local server (default: `http://localhost:1234/v1`).

### CLI

```bash
# List models
lms ls

# Load model
lms load <model-identifier> --gpu=auto --context-length=8192
# --gpu=1.0 means 100% GPU offload
# --identifier="my-finetuned-model" sets a stable name

# Start server
lms server start --port 1234
```

### Test

```bash
curl http://localhost:1234/v1/models
```

**Python (OpenAI SDK):**

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)

resp = client.chat.completions.create(
    model="model-identifier-from-lm-studio",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! What did I fine-tune you to do?"},
    ],
    temperature=0.7,
)

print(resp.choices[0].message.content)
```

**cURL:**

```bash
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "model-identifier-from-lm-studio",
    "messages": [
      {"role": "user", "content": "Say this is a test!"}
    ],
    "temperature": 0.7
  }'
```

> [!tip] Debugging
> Inspect raw prompts: `lms log stream`

## Troubleshooting

### Gibberish / repeated output in LM Studio

Almost always a **prompt template / chat template mismatch**. LM Studio auto-detects from GGUF metadata, but custom models may need manual override.

**Fix:**
1. **My Models** -> gear icon next to model
2. Set **Prompt Template** to match training template
3. Or enable **Prompt Template** box in Chat sidebar

### Model not showing in My Models

- Use `lms import /path/to/model.gguf`
- Verify folder structure: `~/.lmstudio/models/publisher/model/model-file.gguf`

### OOM / slow performance

- Use smaller quant (e.g. `Q4_K_M`)
- Reduce context length
- Adjust GPU offload in Per-model defaults / load settings

## Resources

- [LM Studio + Unsloth blog post](https://lmstudio.ai/blog/functiongemma-unsloth) (FunctionGemma walkthrough)
- [Import Models docs](https://lmstudio.ai/docs/app/advanced/import-model)
- [Prompt Template docs](https://lmstudio.ai/docs/app/advanced/prompt-template)
- [OpenAI-compatible API docs](https://lmstudio.ai/docs/developer/openai-compat)

#lm-studio #gguf #deployment #openai-api #model-serving
