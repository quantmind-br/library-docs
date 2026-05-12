---
title: 'Devstral: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/devstral-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:31.432660958-03:00
rendered_js: false
word_count: 942
summary: This document serves as a comprehensive guide and reference for using Devstral-Small-2507, an agentic LLM from Mistral AI. It details how to run the model with recommended settings across different platforms (Ollama and llama.cpp) and explains features like tool-calling support and 128k context window capability.
tags:
    - llm-guide
    - agentic-model
    - mistral-ai
    - devstral
    - ollama
    - llama-cpp
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Devstral: How to Run & Fine-tune

**Devstral-Small-2507** (Devstral 1.1) is Mistral's agentic LLM for software engineering. Finetuned from [Mistral-Small-3.1](https://huggingface.co/unsloth/Mistral-Small-3.1-24B-Instruct-2503-GGUF), it supports 128k context and tool-calling. Scored 53.6% on [SWE-bench verified](https://openai.com/index/introducing-swe-bench-verified/) — #1 open model (July 10, 2025).

Unsloth GGUFs add **tool-calling support** and **chat template fixes**. Works with OpenHands and generalizes to other prompts/environments. Text-only (vision encoder removed); optional vision support available below.

> [!tip] Official downloads
> Download Mistral's official weights or Unsloth GGUFs/dynamic quants for correct implementation (system prompt, chat template). Use `--jinja` in llama.cpp to enable the system prompt.

All Devstral uploads use Unsloth [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) — best performance on 5-shot MMLU and KL Divergence benchmarks. Quantized inference with minimal accuracy loss.

> [!info] Dynamic uploads
> Files with `UD` prefix are Dynamic 2.0. Those without still use the calibration dataset.

### Devstral Quant Downloads

| Devstral 2507 (new)                                                                                                    | Devstral 2505                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| GGUF: [Devstral-Small-2507-GGUF](https://huggingface.co/unsloth/Devstral-Small-2507-GGUF)                              | [Devstral-Small-2505-GGUF](https://huggingface.co/unsloth/Devstral-Small-2505-GGUF)                         |
| 4-bit BnB: [Devstral-Small-2507-unsloth-bnb-4bit](https://huggingface.co/unsloth/Devstral-Small-2507-unsloth-bnb-4bit) | [Devstral-Small-2505-unsloth-bnb-4bit](https://huggingface.co/unsloth/Devstral-Small-2505-unsloth-bnb-4bit) |

## Running Devstral

### Official Recommended Settings

| Parameter     | Value                         |
| ------------- | ----------------------------- |
| Temperature   | 0.0 – 0.15                    |
| Min_P         | 0.01 (llama.cpp default: 0.1) |
| System prompt | Use `--jinja` to enable       |

A system prompt is recommended (derivative of OpenHands). Full system prompt: [SYSTEM_PROMPT.txt](https://huggingface.co/unsloth/Devstral-Small-2505/blob/main/SYSTEM_PROMPT.txt).

```
You are Devstral, a helpful agentic model trained by Mistral AI and using the OpenHands scaffold. You can interact with a computer to solve tasks.

<ROLE>
Your primary role is to assist users by executing commands, modifying code, and solving technical problems effectively. You should be thorough, methodical, and prioritize quality over speed.
* If the user asks a question, like "why is X happening", don't try to fix the problem. Just give an answer to the question.
</ROLE>

.... SYSTEM PROMPT CONTINUES ....
```

## Running Devstral in Ollama

1. Install ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run with dynamic quant. Use `ollama serve &` in another terminal if it fails. Suggested parameters (temperature etc.) are included in `params` in the Hugging Face upload.

3. Enable [KV cache quantization](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-set-the-quantization-type-for-the-kv-cache) — Devstral supports 128K context. 8bit (`q8_0`) saves ~50% memory; `q4_0` also works.

```bash
export OLLAMA_KV_CACHE_TYPE="q8_0"
ollama run hf.co/unsloth/Devstral-Small-2507-GGUF:UD-Q4_K_XL
```

## Running Devstral in llama.cpp

1. Build llama.cpp from [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal (on by default for Mac).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Run directly from Hugging Face:

```bash
./llama.cpp/llama-cli -hf unsloth/Devstral-Small-2507-GGUF:UD-Q4_K_XL --jinja
```

3. **OR** download manually (after `pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Devstral-Small-2507-GGUF",
    local_dir = "unsloth/Devstral-Small-2507-GGUF",
    allow_patterns = ["*Q4_K_XL*", "*mmproj-F16*"], # For Q4_K_XL
)
```

4. Run in conversation mode. Adjust `--n-gpu-layers` if GPU OOM; remove for CPU-only. `--ctx-size 131072` = 128K context.

```bash
./llama.cpp/llama-cli \
    --model unsloth/Devstral-Small-2507-GGUF/Devstral-Small-2507-UD-Q4_K_XL.gguf \
    --threads -1 \
    --ctx-size 131072 \
    --cache-type-k q8_0 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.15 \
    --repeat-penalty 1.0 \
    --min-p 0.01 \
    --top-k 64 \
    --top-p 0.95 \
    --jinja
```

5. Non-conversation mode (e.g. Flappy Bird prompt):

```bash
./llama.cpp/llama-cli \
    --model unsloth/Devstral-Small-2507-GGUF/Devstral-Small-2507-UD-Q4_K_XL.gguf \
    --threads -1 \
    --ctx-size 131072 \
    --cache-type-k q8_0 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.15 \
    --repeat-penalty 1.0 \
    --min-p 0.01 \
    --top-k 64 \
    --top-p 0.95 \
    -no-cnv \
    --prompt "[SYSTEM_PROMPT]You are Devstral, a helpful agentic model trained by Mistral AI and using the OpenHands scaffold. You can interact with a computer to solve tasks.\n\n<ROLE>\nYour primary role is to assist users by executing commands, modifying code, and solving technical problems effectively. You should be thorough, methodical, and prioritize quality over speed.\n* If the user asks a question, like \"why is X happening\", don\'t try to fix the problem. Just give an answer to the question.\n</ROLE>\n\n<EFFICIENCY>\n* Each action you take is somewhat expensive. Wherever possible, combine multiple actions into a single action, e.g. combine multiple bash commands into one, using sed and grep to edit/view multiple files at once.\n* When exploring the codebase, use efficient tools like find, grep, and git commands with appropriate filters to minimize unnecessary operations.\n</EFFICIENCY>\n\n<FILE_SYSTEM_GUIDELINES>\n* When a user provides a file path, do NOT assume it\'s relative to the current working directory. First explore the file system to locate the file before working on it.\n* If asked to edit a file, edit the file directly, rather than creating a new file with a different filename.\n* For global search-and-replace operations, consider using `sed` instead of opening file editors multiple times.\n</FILE_SYSTEM_GUIDELINES>\n\n<CODE_QUALITY>\n* Write clean, efficient code with minimal comments. Avoid redundancy in comments: Do not repeat information that can be easily inferred from the code itself.\n* When implementing solutions, focus on making the minimal changes needed to solve the problem.\n* Before implementing any changes, first thoroughly understand the codebase through exploration.\n* If you are adding a lot of code to a function or file, consider splitting the function or file into smaller pieces when appropriate.\n</CODE_QUALITY>\n\n<VERSION_CONTROL>\n* When configuring git credentials, use \"openhands\" as the user.name and \"openhands@all-hands.dev\" as the user.email by default, unless explicitly instructed otherwise.\n* Exercise caution with git operations. Do NOT make potentially dangerous changes (e.g., pushing to main, deleting repositories) unless explicitly asked to do so.\n* When committing changes, use `git status` to see all modified files, and stage all files necessary for the commit. Use `git commit -a` whenever possible.\n* Do NOT commit files that typically shouldn\'t go into version control (e.g., node_modules/, .env files, build directories, cache files, large binaries) unless explicitly instructed by the user.\n* If unsure about committing certain files, check for the presence of .gitignore files or ask the user for clarification.\n</VERSION_CONTROL>\n\n<PULL_REQUESTS>\n* When creating pull requests, create only ONE per session/issue unless explicitly instructed otherwise.\n* When working with an existing PR, update it with new commits rather than creating additional PRs for the same issue.\n* When updating a PR, preserve the original PR title and purpose, updating description only when necessary.\n</PULL_REQUESTS>\n\n<PROBLEM_SOLVING_WORKFLOW>\n1. EXPLORATION: Thoroughly explore relevant files and understand the context before proposing solutions\n2. ANALYSIS: Consider multiple approaches and select the most promising one\n3. TESTING:\n   * For bug fixes: Create tests to verify issues before implementing fixes\n   * For new features: Consider test-driven development when appropriate\n   * If the repository lacks testing infrastructure and implementing tests would require extensive setup, consult with the user before investing time in building testing infrastructure\n   * If the environment is not set up to run tests, consult with the user first before investing time to install all dependencies\n4. IMPLEMENTATION: Make focused, minimal changes to address the problem\n5. VERIFICATION: If the environment is set up to run tests, test your implementation thoroughly, including edge cases. If the environment is not set up to run tests, consult with the user first before investing time.\n</PROBLEM_SOLVING_WORKFLOW>\n\n<SECURITY>\n* Only use GITHUB_TOKEN and other credentials in ways the user has explicitly requested and would expect.\n* Use APIs to work with GitHub or other platforms, unless the user asks otherwise or your task requires browsing.\n</SECURITY>\n\n<ENVIRONMENT_SETUP>\n* When user asks you to run an application, don\'t stop if the application is not installed. Instead, please install the application and run the command again.\n* If you encounter missing dependencies:\n  1. First, look around in the repository for existing dependency files (requirements.txt, pyproject.toml, package.json, Gemfile, etc.)\n  2. If dependency files exist, use them to install all dependencies at once (e.g., `pip install -r requirements.txt`, `npm install`, etc.)\n  3. Only install individual packages directly if no dependency files are found or if only specific packages are needed\n* Similarly, if you encounter missing dependencies for essential tools requested by the user, install them when possible.\n</ENVIRONMENT_SETUP>\n\n<TROUBLESHOOTING>\n* If you\'ve made repeated attempts to solve a problem but tests still fail or the user reports it\'s still broken:\n  1. Step back and reflect on 5-7 different possible sources of the problem\n  2. Assess the likelihood of each possible cause\n  3. Methodically address the most likely causes, starting with the highest probability\n  4. Document your reasoning process\n* When you run into any major issue while executing a plan from the user, please don\'t try to directly work around it. Instead, propose a new plan and confirm with the user before proceeding.\n</TROUBLESHOOTING>[/SYSTEM_PROMPT][INST]Create a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird\'s shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don\'t hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for error[/INST]"
```

> [!danger] Non-conversation mode
> Remove `<bos>` since Devstral auto-adds it. Use `--jinja` to enable the system prompt.

## Experimental Vision Support

[Xuan-Son](https://x.com/ngxson) (Hugging Face) demonstrated grafting the Mistral 3.1 Instruct vision encoder onto Devstral 2507 via [GGUF repo](https://huggingface.co/ngxson/Devstral-Small-Vision-2505-GGUF). Unsloth uploaded mmproj files:

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/Devstral-Small-2507-GGUF/Devstral-Small-2507-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Devstral-Small-2507-GGUF/mmproj-F16.gguf \
    --threads -1 \
    --ctx-size 131072 \
    --cache-type-k q8_0 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.15
```

| Instruction and output code                                                                                   | Rendered code                                                                                                 |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ![](https://cdn-uploads.huggingface.co/production/uploads/63ca214abedad7e2bf1d1517/HDic53ANsCoJbiWu2eE6K.png) | ![](https://cdn-uploads.huggingface.co/production/uploads/63ca214abedad7e2bf1d1517/onV1xfJIT8gzh81RkLn8J.png) |

## Fine-tuning Devstral with Unsloth

Unsloth supports Devstral fine-tuning (like standard Mistral models): 2x faster training, 70% less VRAM, 8x longer contexts. Fits in 24GB VRAM (L4 GPU).

Exceeds 16GB VRAM — not free on Google Colab. Free fine-tuning available via [Kaggle notebook](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Magistral_\(24B\)-Reasoning-Conversational.ipynb\&accelerator=nvidiaTeslaT4) (dual GPUs). Change model name from Magistral to Devstral.

Install latest Unsloth for local fine-tuning:

```bash
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
```

[^1]: K quantization to reduce memory use. Can be f16, q8_0, q4_0

[^2]: Must use --jinja to enable system prompt

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/devstral-how-to-run-and-fine-tune.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#devstral #mistral-ai #llm-guide #ollama #llama-cpp
