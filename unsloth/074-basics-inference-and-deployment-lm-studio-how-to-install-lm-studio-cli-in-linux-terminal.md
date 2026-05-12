---
title: How to install LM Studio CLI in Linux Terminal
url: https://unsloth.ai/docs/basics/inference-and-deployment/lm-studio/how-to-install-lm-studio-cli-in-linux-terminal.md
source: llms
fetched_at: 2026-04-27T18:14:49.781221223-03:00
rendered_js: false
word_count: 389
summary: This document provides a comprehensive step-by-step guide on how to install and utilize the LM Studio CLI on a Linux terminal environment. It covers downloading the AppImage, handling common startup errors like sandboxing issues or missing X servers, importing models, and finally running the local server for use via an OpenAI-compatible endpoint.
tags:
    - lm-studio
    - linux-cli
    - installation-guide
    - model-importing
    - terminal-setup
    - openai-endpoint
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# How to install LM Studio CLI in Linux Terminal

1. Download LM Studio AppImage (~1GB):

```bash
wget https://lmstudio.ai/download/latest/linux/x64?format=AppImage -O 'LM_Studio.AppImage'
chmod u+x ./LM_Studio.AppImage
```

2. Run it:

```bash
./LM_Studio.AppImage
```

> [!warning] SUID sandbox error
> If you see `FATAL:sandbox/linux/suid/client/setuid_sandbox_host.cc:166 ... aborting now`, run with `--no-sandbox`:

```bash
./LM_Studio.AppImage --no-sandbox
```

> [!warning] Missing X server (headless/cloud)
> If you see `Missing X server or $DISPLAY` + `Segmentation fault`, install xvfb:

```bash
sudo apt-get install xvfb
```

3. Launch with xvfb:

```bash
xvfb-run --auto-servernum ./LM_Studio.AppImage --no-sandbox
```

4. Bootstrap the LM Studio CLI (`lms`) in another terminal (or after `Ctrl+B+D` in tmux):

```bash
~/.lmstudio/bin/lms bootstrap
```

5. Run `lms` in a **new** terminal:

```bash
lms
```

> [!tip] If `-bash: lms: command not found`, run `lms` in a new terminal window.

6. Download a model (e.g. [[019-models-qwen3-coder-next|Qwen3-Coder-Next]]). If downloads stall, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|Hugging Face Hub XET debugging]].

```bash
pip install -U huggingface_hub
hf download unsloth/Qwen3-Coder-Next-GGUF \
    --local-dir unsloth/Qwen3-Coder-Next-GGUF \
    --include "*UD-Q4_K_XL*"
```

7. Import the model into LM Studio:

```bash
lms import \
    unsloth/Qwen3-Coder-Next-GGUF/Qwen3-Coder-Next-UD-Q4_K_XL.gguf \
    --symbolic-link --user-repo "unsloth/Qwen3-Coder-Next-GGUF" -y
```

> [!info] `EEXIST: file already exists` means the model is already loaded.

List all imported models:

```bash
ls ~/.lmstudio/models
```

8. Alternatively, download directly via `lms get`:

```bash
lms get https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF@Q4_K_XL
```

Then load:

```bash
lms load qwen3-coder-next
```

9. Start the LM Studio server:

```bash
lms server start --port 8001 --bind 127.0.0.1
```

10. Use via OpenAI-compatible endpoint:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "null",
)
model_name = next(iter(openai_client.models.list())).id
print(model_name)
completion = openai_client.chat.completions.create(
    model = model_name,
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

#lm-studio #linux-cli #local-llm #gguf #openai-endpoint
