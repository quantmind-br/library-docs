---
title: How to Run Local LLMs with Claude Code
url: https://unsloth.ai/docs/basics/claude-code.md
source: llms
fetched_at: 2026-04-27T18:14:56.442655693-03:00
rendered_js: false
word_count: 1927
summary: This guide provides step-by-step instructions on how to run and deploy various open Large Language Models (LLMs) like Qwen3.5 and GLM-4.7-Flash locally for integration with Claude Code, utilizing the llama.cpp framework.
tags:
    - llm-local
    - claude-code
    - llama-cpp
    - qwen3.5
    - model-deployment
    - gguf-quantization
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:33:00Z
---

# How to Run Local LLMs with Claude Code

Connect open LLMs to Claude Code locally via `llama.cpp`. Uses [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5) and [GLM-4.7-Flash](https://unsloth.ai/docs/models/glm-4.7-flash) (strongest 35B MoE agentic/coding models as of Mar 2026, fits 24GB). Swap in any model from [[050-models-tutorials|tutorials]] -- update model names in scripts. Uses Unsloth [Dynamic GGUFs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for quantization.

> [!info]
> Claude Code has changed significantly since Jan 2026. Additional settings and toggles are required.

## LLM Setup Tutorials

Models are served via `llama-server` (part of `llama.cpp`) on port 8001 with an OpenAI-compatible endpoint.

### Qwen3.5 Tutorial

Uses [Qwen3.5-35B-A3B](https://unsloth.ai/docs/models/qwen3.5). If insufficient VRAM or smarter model needed, use **Qwen3.5-27B** (~2x slower). Other variants: 9B, 4B, 2B.

> [!info]
> Use **Qwen3.5-27B** for smarter output or lower VRAM (~2x slower). Or use [Qwen3-Coder-Next](https://unsloth.ai/docs/models/qwen3-coder-next) if you have enough VRAM.

#### Install llama.cpp

Follow official build instructions for correct GPU bindings. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev git-all -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

#### Download and use models locally

Requires `pip install huggingface_hub hf_transfer`. Uses **UD-Q4_K_XL** quant (best size/accuracy balance). All Unsloth GGUF uploads: [[114-get-started-unsloth-model-catalog|Collection]]. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

```bash
hf download unsloth/Qwen3.5-35B-A3B-GGUF \
    --local-dir unsloth/Qwen3.5-35B-A3B-GGUF \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

> [!tip]
> You can use any variant like `unsloth/Qwen3-Coder-Next-GGUF` instead.

#### Start the Llama-server

Uses [Qwen's recommended sampling parameters](https://unsloth.ai/docs/models/qwen3.5#recommended-settings) for thinking mode. Run in a new terminal (`tmux`). Fits 24GB GPU (RTX 4090, uses 23GB). `--fit on` auto-offloads; reduce `--ctx-size` if performance is bad.

> [!danger]
> Uses `--cache-type-k q8_0 --cache-type-v q8_0` for KV cache quantization (less VRAM). For full precision: `--cache-type-k bf16 --cache-type-v bf16`. **Do not use f16** -- Qwen3.5 degrades accuracy with f16 KV cache (also llama.cpp default). bf16 may be slightly slower on some machines.

```bash
./llama.cpp/llama-server \
    --model unsloth/Qwen3.5-35B-A3B-GGUF/Qwen3.5-35B-A3B-UD-Q4_K_XL.gguf \
    --alias "unsloth/Qwen3.5-35B-A3B" \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001 \
    --kv-unified \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --flash-attn on --fit on \
    --ctx-size 131072 # change as required
```

> [!tip]
> Disable thinking for faster agentic coding. Add to llama-server command: `--chat-template-kwargs "{\"enable_thinking\": false}"`

### GLM-4.7-Flash Tutorial

#### Install llama.cpp

Same as Qwen3.5 installation above.

#### Download and use models locally

Same prerequisites as Qwen3.5. Uses Python `huggingface_hub` with `hf_transfer` enabled.

```python
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id = "unsloth/GLM-4.7-Flash-GGUF",
    local_dir = "unsloth/GLM-4.7-Flash-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

> [!tip]
> Can use `unsloth/Qwen3-Coder-Next-GGUF` or any other model instead.

#### Start the Llama-server

Uses Z.ai recommended sampling (`temp 1.0`, `top_p 0.95`). Fits 24GB GPU (RTX 4090, uses 23GB).

> [!danger]
> Uses `q8_0` KV cache. If quality drops, switch to bf16 (doubles VRAM): `--cache-type-k bf16 --cache-type-v bf16`.

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf \
    --alias "unsloth/GLM-4.7-Flash" \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --port 8001 \
    --kv-unified \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --flash-attn on --fit on \
    --batch-size 4096 --ubatch-size 1024 \
    --ctx-size 131072 #change as required
```

> [!tip]
> Disable thinking for GLM-4.7-Flash: add `--chat-template-kwargs "{\"enable_thinking\": false}"`

## Claude Code Tutorial

> [!danger]
> After installing, apply the [KV Cache fix](#fixing-90-slower-inference-in-claude-code) below -- local models are 90% slower without it due to attribution header invalidating cache.

Claude Code is Anthropic's agentic coding CLI tool. Redirect it to your local llama.cpp server.

### Install Claude Code

**Mac / Linux:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
# Or via Homebrew: brew install --cask claude-code
```

```bash
export ANTHROPIC_BASE_URL="http://localhost:8001"
export ANTHROPIC_API_KEY='sk-no-key-required' ## or 'sk-1234'
```

**Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

```powershell
$env:ANTHROPIC_BASE_URL="http://localhost:8001"
```

**Persistence:**
- Mac/Linux: add `export` lines to `~/.bashrc` or `~/.zshrc`
- Windows: run `setx ANTHROPIC_BASE_URL "http://localhost:8001"` once, or add `$env:` line to `$PROFILE`

> [!warning]
> `Unable to connect to API (ConnectionRefused)` -- unset `ANTHROPIC_BASE_URL` via `unset ANTHROPIC_BASE_URL`

> [!info]
> If Claude Code asks to sign in on first run, add `"hasCompletedOnboarding": true` and `"primaryApiKey": "sk-dummy-key"` to `~/.claude.json`. For VS Code extension, enable **Disable Login Prompt** or add `"claudeCode.disableLoginPrompt": true` to `settings.json`.

### Fixing 90% slower inference in Claude Code

Claude Code prepends an attribution header that **invalidates KV Cache, making local model inference 90% slower**. ([LocalLlama discussion](https://www.reddit.com/r/LocalLLaMA/comments/1r47fz0/claude_code_with_local_models_full_prompt/))

> [!danger]
> `export CLAUDE_CODE_ATTRIBUTION_HEADER=0` **DOES NOT** work. Must be set in `~/.claude/settings.json`.

Edit `~/.claude/settings.json` -- add `"CLAUDE_CODE_ATTRIBUTION_HEADER" : "0"` to the `"env"` section:

```json
{
  "promptSuggestionEnabled": false,
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "0",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_ATTRIBUTION_HEADER" : "0"
  },
  "attribution": {
    "commit": "",
    "pr": ""
  },
  "plansDirectory" : "./plans",
  "prefersReducedMotion" : true,
  "terminalProgressBarEnabled" : false,
  "effortLevel" : "high"
}
```

### Running Claude Code locally

> [!tip]
> Works with `unsloth/GLM-4.7-Flash` or `unsloth/Qwen3.5-35B-A3B` (change `--model` flag).

> [!danger]
> Apply the [KV Cache fix](#fixing-90-slower-inference-in-claude-code) first.

```bash
claude --model unsloth/GLM-4.7-Flash
# or: claude --model unsloth/Qwen3.5-35B-A3B
```

Skip all permission prompts (execute code without approvals):

```bash
claude --model unsloth/GLM-4.7-Flash --dangerously-skip-permissions
```

**Sample prompt for Unsloth finetuning:**

```
You can only work in the cwd project/. Do not search for CLAUDE.md - this is it. Install Unsloth via a virtual environment via uv. Use `python -m venv unsloth_env` then `source unsloth_env/bin/activate` if possible. See https://unsloth.ai/docs/get-started/install/pip-install on how (get it and read). Then do a simple Unsloth finetuning run described in https://github.com/unslothai/unsloth. You have access to 1 GPU.
```

### IDE Extension (VS Code / Cursor)

- [Install for VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
- [Install for Cursor](cursor:extension/anthropic.claude-code)
- [Claude Code in VS Code docs](https://code.claude.com/docs/en/vs-code)
- Or: `Ctrl+Shift+X` (Win/Linux) / `Cmd+Shift+X` (Mac) -> search **Claude Code** -> Install

#moe #llm-local #claude-code #llama-cpp #gguf
